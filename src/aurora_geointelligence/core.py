"""Transparent CPU-first image analysis baseline for Aurora GeoIntelligence XAI.

The default output is unsupervised color clustering, not semantic land-cover
classification. Spectral indices are computed only when the user explicitly
selects bands; they are not interpreted as ground truth.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import tempfile
import zipfile

import numpy as np
from PIL import Image, ImageOps
from sklearn.cluster import MiniBatchKMeans

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff"}
MAX_UPLOAD_BYTES = 100 * 1024 * 1024
MAX_PIXELS = 50_000_000
PREVIEW_MAX_SIDE = 768
PALETTE = np.array([
    [24, 202, 166], [31, 145, 232], [243, 181, 63], [211, 91, 152],
    [157, 126, 245], [238, 105, 72], [109, 194, 82], [92, 105, 125],
], dtype=np.uint8)


@dataclass
class RasterData:
    bands: np.ndarray  # H x W x C, float32
    preview: Image.Image
    metadata: dict


def _stretch(band: np.ndarray) -> np.ndarray:
    values = np.asarray(band, dtype=np.float32)
    valid = np.isfinite(values)
    if not valid.any():
        return np.zeros(values.shape, dtype=np.uint8)
    low, high = np.percentile(values[valid], [2, 98])
    if not math.isfinite(float(low)) or not math.isfinite(float(high)) or high <= low:
        low, high = float(np.min(values[valid])), float(np.max(values[valid]))
    if high <= low:
        return np.zeros(values.shape, dtype=np.uint8)
    stretched = np.clip((values - low) / (high - low), 0, 1)
    stretched[~valid] = 0
    return (stretched * 255).astype(np.uint8)


def _make_preview(bands: np.ndarray) -> Image.Image:
    if bands.ndim != 3 or bands.shape[2] == 0:
        raise ValueError("A imagem não contém bandas utilizáveis.")
    if bands.shape[2] >= 3:
        rgb = np.stack([_stretch(bands[:, :, i]) for i in range(3)], axis=-1)
    else:
        gray = _stretch(bands[:, :, 0])
        rgb = np.repeat(gray[:, :, None], 3, axis=2)
    image = Image.fromarray(rgb)
    image.thumbnail((PREVIEW_MAX_SIDE, PREVIEW_MAX_SIDE), Image.Resampling.LANCZOS)
    return image


def load_raster(path: str | os.PathLike) -> RasterData:
    """Load a bounded-size image and return pixels, display stretch and metadata."""
    source = Path(path)
    if not source.is_file():
        raise ValueError("Arquivo não encontrado.")
    if source.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError("Formato não permitido. Use PNG, JPEG ou TIFF/GeoTIFF.")
    size = source.stat().st_size
    if size <= 0 or size > MAX_UPLOAD_BYTES:
        raise ValueError("O arquivo está vazio ou excede o limite de 100 MB.")

    data = None
    metadata: dict = {
        "file_name": source.name,
        "file_size_bytes": size,
        "crs": None,
        "bounds": None,
        "resolution": None,
        "acquisition_date": None,
        "band_count": None,
        "width": None,
        "height": None,
        "source_tags": {},
    }
    if source.suffix.lower() in {".tif", ".tiff"}:
        try:
            import rasterio
            with rasterio.open(source) as dataset:
                if dataset.width * dataset.height > MAX_PIXELS:
                    raise ValueError("A imagem excede o limite de 50 milhões de pixels.")
                raw = dataset.read(out_dtype="float32")
                data = np.moveaxis(raw, 0, -1)
                tags = dataset.tags()
                metadata.update({
                    "crs": str(dataset.crs) if dataset.crs else None,
                    "bounds": list(dataset.bounds),
                    "resolution": list(dataset.res),
                    "band_count": dataset.count,
                    "width": dataset.width,
                    "height": dataset.height,
                    "source_tags": {str(k): str(v) for k, v in tags.items()},
                    "nodata": dataset.nodata,
                })
                metadata["acquisition_date"] = tags.get("TIFFTAG_DATETIME") or tags.get("DATE_ACQUIRED")
        except ImportError:
            data = None
        except (ValueError, OSError):
            raise
        except Exception as exc:
            raise ValueError(f"Não foi possível ler o TIFF: {exc}") from exc

    if data is None:
        try:
            with Image.open(source) as im:
                im = ImageOps.exif_transpose(im)
                if im.width * im.height > MAX_PIXELS:
                    raise ValueError("A imagem excede o limite de 50 milhões de pixels.")
                data = np.asarray(im).astype(np.float32)
                if data.ndim == 2:
                    data = data[:, :, None]
                elif data.ndim == 3 and data.shape[2] == 4:
                    data = data[:, :, :3]
                metadata.update({"band_count": int(data.shape[2]), "width": im.width, "height": im.height})
                exif = im.getexif()
                date = exif.get(36867) or exif.get(306)
                metadata["acquisition_date"] = str(date) if date else None
        except ValueError:
            raise
        except Exception as exc:
            raise ValueError(f"Arquivo de imagem inválido ou não suportado: {exc}") from exc

    if data.ndim != 3 or data.shape[0] < 1 or data.shape[1] < 1:
        raise ValueError("Dimensões de imagem inválidas.")
    if not np.isfinite(data).any():
        raise ValueError("A imagem não contém valores numéricos válidos.")
    metadata.setdefault("band_count", int(data.shape[2]))
    metadata.setdefault("width", int(data.shape[1]))
    metadata.setdefault("height", int(data.shape[0]))
    return RasterData(data, _make_preview(data), metadata)


def _downsample(array: np.ndarray, max_side: int = PREVIEW_MAX_SIDE) -> np.ndarray:
    h, w = array.shape[:2]
    if max(h, w) <= max_side:
        return array
    scale = max_side / max(h, w)
    nh, nw = max(1, round(h * scale)), max(1, round(w * scale))
    image = Image.fromarray(array)
    return np.asarray(image.resize((nw, nh), Image.Resampling.BILINEAR))


def cluster_image(preview: Image.Image, n_clusters: int = 5) -> tuple[Image.Image, dict]:
    """Run reproducible MiniBatchKMeans over display RGB pixels; labels are arbitrary."""
    if not 2 <= int(n_clusters) <= 8:
        raise ValueError("Escolha entre 2 e 8 grupos.")
    rgb = np.asarray(preview.convert("RGB"), dtype=np.uint8)
    pixels = rgb.reshape(-1, 3).astype(np.float32)
    distinct = np.unique(pixels, axis=0)
    k = min(int(n_clusters), len(distinct))
    if k < 2:
        raise ValueError("A imagem é uniforme; não foi possível formar grupos distintos.")
    model = MiniBatchKMeans(n_clusters=k, random_state=42, n_init=3, batch_size=2048, max_iter=80)
    labels = model.fit_predict(pixels).reshape(rgb.shape[:2])
    mask_rgb = PALETTE[labels % len(PALETTE)]
    counts = np.bincount(labels.ravel(), minlength=k)
    stats = []
    for index in range(k):
        selected = rgb[labels == index]
        stats.append({
            "cluster_id": index,
            "pixel_share": round(float(counts[index] / labels.size), 6),
            "mean_display_rgb": [round(float(x), 1) for x in selected.mean(axis=0)],
            "interpretation": "Grupo visual não rotulado; não representa uma classe temática validada.",
        })
    return Image.fromarray(mask_rgb), {"algorithm": "scikit-learn MiniBatchKMeans", "random_state": 42, "requested_clusters": int(n_clusters), "effective_clusters": k, "clusters": stats}


def spectral_index(data: RasterData, index_type: str, band_a: int, band_b: int) -> tuple[Image.Image, dict]:
    """Compute a user-defined band index. Band positions are 1-based."""
    kind = (index_type or "").upper()
    formulas = {"NDVI": "(NIR - Red) / (NIR + Red)", "NDWI": "(Green - SWIR) / (Green + SWIR)"}
    if kind not in formulas:
        raise ValueError("Índice não reconhecido.")
    a, b = int(band_a), int(band_b)
    count = data.bands.shape[2]
    if a < 1 or b < 1 or a > count or b > count or a == b:
        raise ValueError(f"Informe duas bandas diferentes entre 1 e {count}.")
    x = data.bands[:, :, a - 1].astype(np.float32)
    y = data.bands[:, :, b - 1].astype(np.float32)
    denom = x + y
    index = np.divide(x - y, denom, out=np.zeros_like(x), where=np.abs(denom) > 1e-8)
    index = np.clip(index, -1.0, 1.0)
    small = _downsample(index)
    scaled = np.clip((small + 1.0) * 127.5, 0, 255).astype(np.uint8)
    # A deterministic cool-to-warm ramp for display, not a causal explanation.
    ramp = np.stack([scaled, np.minimum(255, 2 * np.abs(scaled.astype(np.int16) - 127)).astype(np.uint8), 255 - scaled], axis=-1)
    valid = np.isfinite(index)
    summary = {
        "index": kind,
        "formula": formulas[kind],
        "band_a_1_based": a,
        "band_b_1_based": b,
        "meaning_of_bands": "A semântica das bandas foi definida pelo usuário e não é inferida pelo sistema.",
        "min": round(float(np.nanmin(index)), 5),
        "max": round(float(np.nanmax(index)), 5),
        "mean": round(float(np.nanmean(index)), 5),
        "valid_pixel_fraction": round(float(valid.mean()), 6),
        "caveat": "O índice é uma transformação numérica exploratória; não comprova condição ambiental ou classe de cobertura do solo.",
    }
    return Image.fromarray(ramp), summary


def run_analysis(path: str, n_clusters: int = 5, index_type: str | None = None,
                 band_a: int | None = None, band_b: int | None = None) -> tuple[Image.Image, Image.Image, Image.Image | None, str, str]:
    data = load_raster(path)
    mask, cluster_summary = cluster_image(data.preview, n_clusters)
    overlay = Image.blend(data.preview.convert("RGB"), mask, alpha=0.48)
    index_image = None
    index_summary = None
    if index_type:
        if band_a is None or band_b is None:
            raise ValueError("Para calcular NDVI/NDWI, informe os índices de banda A e B (numeração iniciada em 1).")
        index_image, index_summary = spectral_index(data, index_type, band_a, band_b)
    report = {
        "project": "AURORA GEOINTELLIGENCE XAI",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "input": data.metadata,
        "preprocessing": {"display_bands": "first three bands when available; per-band 2nd–98th percentile stretch", "preview_max_side": PREVIEW_MAX_SIDE},
        "analysis": cluster_summary,
        "spectral_index": index_summary,
        "validation": {"reference_labels_available": False, "scientific_accuracy_claimed": False, "metrics": None},
        "limitations": [
            "Unsupervised clusters are arbitrary visual groups, not semantic land-cover labels.",
            "A validation dataset with reference annotations was not supplied.",
            "Spectral index interpretation depends on correct user-selected bands and calibrated input data.",
            "Attention or overlay visualization is not evidence of causality.",
        ],
    }
    report_json = json.dumps(report, ensure_ascii=False, indent=2)
    temp = tempfile.NamedTemporaryFile(prefix="aurora-analysis-", suffix=".zip", delete=False)
    temp.close()
    with zipfile.ZipFile(temp.name, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("analysis_report.json", report_json)
        from io import BytesIO
        for filename, image in (("cluster_mask.png", mask), ("overlay.png", overlay), ("spectral_index.png", index_image)):
            if image is not None:
                stream = BytesIO()
                image.save(stream, format="PNG")
                archive.writestr(filename, stream.getvalue())
    return data.preview, overlay, index_image, temp.name, report_json

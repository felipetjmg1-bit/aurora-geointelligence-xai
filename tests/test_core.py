from __future__ import annotations
import json
import sys
import zipfile
from pathlib import Path

import numpy as np
import pytest
import rasterio
from PIL import Image
from rasterio.transform import from_origin

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import aurora_geointelligence.core as core
from aurora_geointelligence.core import RasterData, cluster_image, load_raster, run_analysis, spectral_index


def make_image(path: Path) -> Path:
    arr = np.zeros((48, 64, 3), dtype=np.uint8)
    arr[:24, :32] = [20, 100, 180]
    arr[:24, 32:] = [40, 190, 70]
    arr[24:, :32] = [220, 150, 40]
    arr[24:, 32:] = [160, 50, 100]
    Image.fromarray(arr).save(path)
    return path


def test_load_png_and_basic_metadata(tmp_path):
    path = make_image(tmp_path / "sample.png")
    data = load_raster(path)
    assert data.bands.shape == (48, 64, 3)
    assert data.metadata["band_count"] == 3
    assert data.preview.size == (64, 48)


def test_reject_unsupported_file_extension(tmp_path):
    path = tmp_path / "sample.exe"
    path.write_bytes(b"not an image")
    with pytest.raises(ValueError, match="Formato não permitido"):
        load_raster(path)


def test_reject_corrupt_supported_image(tmp_path):
    path = tmp_path / "broken.png"
    path.write_bytes(b"broken")
    with pytest.raises(ValueError):
        load_raster(path)


def test_upload_size_limit(tmp_path, monkeypatch):
    path = make_image(tmp_path / "sample.png")
    monkeypatch.setattr(core, "MAX_UPLOAD_BYTES", 1)
    with pytest.raises(ValueError, match="100 MB"):
        load_raster(path)


def test_upload_pixel_limit(tmp_path, monkeypatch):
    path = make_image(tmp_path / "sample.png")
    monkeypatch.setattr(core, "MAX_PIXELS", 100)
    with pytest.raises(ValueError, match="50 milhões de pixels"):
        load_raster(path)


def test_geotiff_metadata_and_resolution(tmp_path):
    path = tmp_path / "synthetic-georeferenced.tif"
    values = np.zeros((4, 10, 12), dtype=np.uint8)
    values[0] = 20
    values[1] = 60
    values[2] = 120
    values[3] = 200
    with rasterio.open(
        path, "w", driver="GTiff", height=10, width=12, count=4,
        dtype="uint8", crs="EPSG:3857", transform=from_origin(500000, 7000000, 0.5, 0.5),
    ) as dataset:
        dataset.write(values)
        dataset.update_tags(DATE_ACQUIRED="2026-01-02")
    data = load_raster(path)
    assert data.metadata["crs"] == "EPSG:3857"
    assert data.metadata["resolution"] == [0.5, 0.5]
    assert data.metadata["band_count"] == 4
    assert data.metadata["acquisition_date"] == "2026-01-02"


def test_clusters_are_deterministic_and_unlabeled(tmp_path):
    data = load_raster(make_image(tmp_path / "sample.png"))
    mask1, summary1 = cluster_image(data.preview, 4)
    mask2, summary2 = cluster_image(data.preview, 4)
    assert np.array_equal(np.asarray(mask1), np.asarray(mask2))
    assert summary1["effective_clusters"] == 4
    assert all("não representa" in row["interpretation"] for row in summary1["clusters"])
    assert summary1 == summary2


def test_cluster_count_validation(tmp_path):
    data = load_raster(make_image(tmp_path / "sample.png"))
    with pytest.raises(ValueError, match="2 e 8"):
        cluster_image(data.preview, 1)


def test_spectral_index_uses_explicit_one_based_bands():
    bands = np.zeros((4, 5, 4), dtype=np.float32)
    bands[:, :, 3] = 0.8  # band 4, NIR
    bands[:, :, 0] = 0.2  # band 1, red
    data = RasterData(bands, Image.new("RGB", (5, 4)), {"band_count": 4})
    _, summary = spectral_index(data, "NDVI", 4, 1)
    assert summary["index"] == "NDVI"
    assert summary["band_a_1_based"] == 4
    assert summary["mean"] == pytest.approx(0.6, abs=1e-4)
    assert "não é inferida" in summary["meaning_of_bands"]


def test_spectral_index_rejects_invalid_band():
    data = RasterData(np.zeros((2, 2, 3), dtype=np.float32), Image.new("RGB", (2, 2)), {})
    with pytest.raises(ValueError, match="entre 1 e 3"):
        spectral_index(data, "NDVI", 4, 1)


def test_end_to_end_creates_auditable_export(tmp_path):
    input_path = make_image(tmp_path / "scene.png")
    original, overlay, index, archive, report_json = run_analysis(str(input_path), 4)
    report = json.loads(report_json)
    assert original.size == overlay.size
    assert index is None
    assert report["validation"]["scientific_accuracy_claimed"] is False
    with zipfile.ZipFile(archive) as z:
        assert {"analysis_report.json", "cluster_mask.png", "overlay.png"}.issubset(set(z.namelist()))
        bundled = json.loads(z.read("analysis_report.json"))
        assert bundled["analysis"]["effective_clusters"] == 4

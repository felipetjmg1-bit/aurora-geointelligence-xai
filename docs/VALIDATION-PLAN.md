# Validation plan

## Current declared state
CPU-first Gradio MVP for image/raster inspection, visual clustering and optional spectral indices. The default clustering is unsupervised visual grouping. It does not assign semantic land-cover labels and does not establish model accuracy or supervised-model explainability.

## Local reproduction
Use Python 3.11 in a clean virtual environment:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
PYTHONPATH=src python -m pytest -q
python app.py
```

## Required validation before a public release
- [ ] CI workflow `CPU CI` completes successfully on a clean GitHub runner.
- [ ] PNG/JPEG/TIFF/GeoTIFF input paths are tested.
- [ ] CRS, affine transform, nodata and acquisition metadata are checked against synthetic fixtures.
- [ ] Corrupt, oversized, unsupported and adversarial files fail safely.
- [ ] NDVI/NDWI band ordering is explicit and documented for each sensor; no sensor assumptions are silently inferred.
- [ ] Output JSON and archive are deterministic where intended and contain provenance/parameters.
- [ ] Memory and runtime are measured on documented CPU hardware.
- [ ] Demo uses synthetic or openly licensed data with attribution.
- [ ] README, limitations and release notes match observed behavior.

## Evidence record
The repository contains tests and a CI workflow. The workflow has been committed but its result must be inspected in GitHub Actions before claiming CI is green. No benchmark or external scientific validation is claimed by this document.

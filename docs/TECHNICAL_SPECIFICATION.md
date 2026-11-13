# Technical specification / Especificação técnica

## Português

- **Runtime:** Python 3.11 ou superior; dependências registradas em `requirements.txt`.
- **Interface:** Gradio 5.x, compatível com navegador móvel e desktop.
- **Formatos:** PNG, JPEG, TIFF e GeoTIFF; limite de 100 MB por arquivo e 50 milhões de pixels por imagem.
- **Leitura geoespacial:** Rasterio é usado para TIFF quando disponível; CRS, limites, resolução, tags e no-data são registrados quando acessíveis.
- **Preview:** RGB das três primeiras bandas ou banda única replicada; alongamento percentil 2–98; tamanho máximo de preview 768 px de lado.
- **Baseline:** scikit-learn MiniBatchKMeans em RGB do preview, 2–8 clusters, `random_state=42`.
- **Índices opcionais:** NDVI e NDWI com bandas 1-based explicitamente escolhidas. Sem inferência do tipo do sensor ou da ordem espectral.
- **Saída:** preview, sobreposição visual, mapa opcional de índice e ZIP com JSON + PNG.
- **Execução:** CPU; não exige GPU, token, banco de dados ou serviço pago.

A implementação não faz poligonização georreferenciada, modelagem temporal, detecção de mudança entre cenas, análise hiperespectral especializada, classificação temática supervisionada nem segmentação semântica. A arquitetura deixa o núcleo como ponto de substituição futura.

## English

- **Runtime:** Python 3.11 or later; dependencies are listed in `requirements.txt`.
- **Interface:** Gradio 5.x for mobile and desktop browsers.
- **Formats:** PNG, JPEG, TIFF and GeoTIFF; 100 MB upload limit and 50 million pixels per image.
- **Geospatial reading:** Rasterio is used for TIFF when available; CRS, bounds, resolution, tags and nodata are recorded when accessible.
- **Preview:** first three bands as RGB or repeated single band; 2nd–98th percentile stretch; maximum preview side of 768 px.
- **Baseline:** scikit-learn MiniBatchKMeans on preview RGB, 2–8 clusters, `random_state=42`.
- **Optional indices:** NDVI and NDWI with explicitly selected 1-based band positions. Sensor type and spectral order are not inferred.
- **Output:** preview, visual overlay, optional index map and ZIP containing JSON + PNG.
- **Execution:** CPU; no GPU, token, database or paid service required.

The implementation does not provide georeferenced polygonization, temporal modeling, between-scene change detection, specialist hyperspectral analysis, supervised thematic classification or semantic segmentation. The core is the intended future substitution point.

# Abstract / Resumo

## Português

O AURORA GEOINTELLIGENCE XAI é um MVP experimental, executável em CPU, para inspeção de imagens geoespaciais e exploração reproduzível. A versão inicial lê imagens PNG, JPEG e TIFF/GeoTIFF, expõe metadados disponíveis, cria uma pré-visualização, agrupa pixels por semelhança de cor com MiniBatchKMeans e permite calcular NDVI ou NDWI quando a pessoa pesquisadora informa explicitamente as bandas. A interface Gradio exporta um pacote com imagens derivadas e relatório JSON rastreável.

Os agrupamentos não são classes de cobertura do solo; NDVI/NDWI não constituem prova de condição ambiental; não há conjunto anotado que sustente métricas de acurácia. O MVP não contém pesos de modelo de sensoriamento remoto, dados STAR.VISION nem integração com o programa OSE. A contribuição demonstrável nesta versão é a composição aberta e auditável desses componentes básicos com limites explicitados, e não uma alegação de inovação mundial.

## English

AURORA GEOINTELLIGENCE XAI is an experimental, CPU-first MVP for geospatial-image inspection and reproducible exploration. The initial version reads PNG, JPEG and TIFF/GeoTIFF imagery, exposes available metadata, creates a preview, groups pixels by color similarity using MiniBatchKMeans, and optionally computes NDVI or NDWI when the researcher explicitly supplies band indices. Its Gradio interface exports derived images and a traceable JSON report.

Clusters are not land-cover classes; NDVI/NDWI are not proof of environmental conditions; and no annotated reference dataset is available to support accuracy metrics. This MVP contains no remote-sensing pretrained model weights, STAR.VISION data, or OSE-program integration. Its demonstrable contribution is an open and auditable composition of basic components with explicit limitations, not a claim of worldwide novelty.

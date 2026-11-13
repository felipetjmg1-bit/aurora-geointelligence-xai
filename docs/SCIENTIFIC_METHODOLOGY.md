# Scientific methodology / Metodologia científica

## Português

### Escopo atual

A demonstração recebe uma única imagem por execução. PNG/JPEG são abertos como imagens comuns; TIFF/GeoTIFF usam Rasterio quando disponível e a leitura tenta preservar CRS, limites, resolução, dimensões, contagem de bandas e tags. O sistema não altera silenciosamente o arquivo fonte. A visualização usa as três primeiras bandas disponíveis (ou replica uma banda) com estiramento independente pelos percentis 2 e 98. Esse estiramento serve à exibição, não à calibração radiométrica.

O baseline analítico usa MiniBatchKMeans do scikit-learn, `random_state=42`, de 2 a 8 grupos e pixels RGB da visualização. Os números de grupo são arbitrários e não têm rótulos ecológicos ou urbanos. Resumos registram participação de pixels e cor RGB média de exibição.

Opcionalmente, o sistema calcula `(A-B)/(A+B)` com índices de bandas informados pela pessoa usuária: para NDVI, A deve ser NIR e B vermelho; para NDWI, A deve ser verde e B SWIR. Entradas precisam ter bandas compatíveis e radiometria apropriada. O programa não detecta automaticamente a semântica das bandas nem converte números digitais em reflectância.

### Reprodutibilidade

Cada exportação contém o nome e tamanho do arquivo, metadados disponíveis, parâmetros, algoritmo, horário UTC, resumo de grupos, fórmula e bandas do índice (quando solicitado) e limitações. A semente dos agrupamentos é fixa. Dependências e testes ficam versionados. Para estudos, pesquisadores devem guardar a fonte, licença, sensor, data, resolução, CRS, pré-processamento e versões do ambiente junto com os dados originais.

### Avaliação

Não se calcula acurácia, precisão, recall, F1 ou IoU sem máscaras ou rótulos de referência alinhados e um protocolo de amostragem independente. Métricas devem ser calculadas em validação espacial/temporal separada para evitar vazamento, com matriz de confusão, unidades, intervalos de incerteza e versões documentadas. O MVP atual é demonstração funcional, não validação experimental nem validação científica independente.

## English

### Current scope

The demo accepts one image per run. PNG/JPEG are read as ordinary images; TIFF/GeoTIFF use Rasterio when available and attempt to preserve CRS, bounds, resolution, dimensions, band count and tags. The source file is not silently modified. The display uses the first three available bands (or replicates a single band) with independent 2nd–98th percentile stretches. This is for visualization, not radiometric calibration.

The analytical baseline uses scikit-learn MiniBatchKMeans with `random_state=42`, between 2 and 8 clusters, on display RGB pixels. Cluster numbers are arbitrary and have no ecological or urban labels. Summaries record pixel share and mean display RGB.

Optionally, the system computes `(A-B)/(A+B)` using band indices explicitly supplied by the user: for NDVI, A must be NIR and B red; for NDWI, A must be green and B SWIR. Inputs need compatible bands and appropriate radiometry. The software does not infer band semantics or convert digital numbers into reflectance.

### Reproducibility and evaluation

Each export records the file name and size, available metadata, parameters, algorithm, UTC time, cluster summary, index formula and bands (if requested), and limitations. The clustering seed is fixed. No accuracy, precision, recall, F1 or IoU is computed without aligned reference labels and an independent sampling protocol. The current MVP is a functional demonstration, not experimental or independent scientific validation.

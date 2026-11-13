# Limitations / Limitações

## Português

Esta versão é um MVP experimental de inspeção e agrupamento visual. KMeans agrupa cores do preview e não reconhece água, floresta, edificações ou uso do solo. Variações de iluminação, sensor, composição, nuvens, no-data e estiramento podem alterar os grupos. Sem referência anotada, não há métricas de acurácia.

NDVI/NDWI só são úteis quando as bandas selecionadas correspondem às regiões espectrais necessárias e os dados têm calibração adequada. A ferramenta não verifica comprimento de onda, sensor, unidades radiométricas ou presença de bandas SWIR/NIR; escolha incorreta torna a interpretação inválida. Valores de índice não provam saúde da vegetação, qualidade da água ou poluição.

Não há modelo supervisionado de sensoriamento remoto, Grad-CAM, busca textual multimodal, ingestão temporal, comparação de cenas, validação independente, cobertura em nuvem, proteção de dados sensíveis por autenticação nem sincronização com catálogos orbitais. A versão não deve ser usada para fiscalização, emergência, decisão ambiental/regulatória ou planejamento operacional sem validação e revisão humana.

A demonstração não inclui imagens reais do STAR.VISION e não declara parceria, endosso, certificação ou integração com STAR.VISION/OSE.

## English

This version is an experimental MVP for image inspection and visual clustering. KMeans groups preview colors; it does not recognize water, forest, buildings or land use. Lighting, sensor, composition, clouds, nodata and display stretch can change clusters. Without annotated reference data, no accuracy metrics are available.

NDVI/NDWI are useful only when selected bands correspond to the required spectral regions and data are appropriately calibrated. The tool does not verify wavelengths, sensor, radiometric units or availability of SWIR/NIR bands; incorrect selection invalidates interpretation. Index values do not prove vegetation health, water quality or pollution.

There is no supervised remote-sensing model, Grad-CAM, multimodal text search, temporal ingestion, scene comparison, independent validation, cloud coverage, sensitive-data access control or synchronization with satellite catalogs. Do not use this version for enforcement, emergencies, environmental/regulatory decisions or operational planning without validation and human review.

The demo includes no STAR.VISION imagery and makes no claim of partnership, endorsement, certification or STAR.VISION/OSE integration.

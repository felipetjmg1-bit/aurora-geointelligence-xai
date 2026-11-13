# Validation protocol / Protocolo de validação

## Português

A versão 0.1 não acompanha dataset de referência anotado e, portanto, não declara desempenho científico. Para uma avaliação futura, registrar por cena: proveniência e licença; sensor; data e hora; resolução espacial; bandas e comprimentos de onda; CRS; processamento; máscaras de referência; critérios de amostragem; partições espaciais/temporais; versão e parâmetros do algoritmo; hardware; tempo; limitações e resultados.

Para classificação temática, reportar matriz de confusão, precisão, recall e F1 por classe, média macro e suporte; para segmentação, IoU por classe e média, mais definições de borda e tratamento de no-data. Manter treino/validação/teste espacialmente independentes. Publicar scripts e configurações para reprodução. Métricas de algoritmos supervisionados não se aplicam aos grupos não rotulados do baseline atual.

Separar explicitamente: (1) demonstração funcional, (2) avaliação experimental com referência e (3) validação científica independente. Não promover visualizações como evidência de causalidade ou como detecção de poluentes químicos.

## English

Version 0.1 ships without an annotated reference dataset and makes no scientific performance claim. A future evaluation should record per scene: provenance and license; sensor; acquisition date/time; spatial resolution; bands and wavelengths; CRS; preprocessing; reference masks; sampling criteria; spatial/temporal splits; algorithm version and parameters; hardware; runtime; limitations and results.

For thematic classification, report a confusion matrix, per-class precision, recall and F1, macro averages and support. For segmentation, report per-class and mean IoU, with boundary and nodata policies. Keep train/validation/test scenes spatially independent. Publish scripts and configurations. Supervised-model metrics do not apply to the current unlabeled clusters.

Distinguish (1) functional demo, (2) reference-based experimental evaluation and (3) independent scientific validation. Do not present visualizations as causal evidence or as chemical-pollutant detection.

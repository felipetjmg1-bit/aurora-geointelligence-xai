# AURORA GEOINTELLIGENCE XAI · fluxo passo a passo

Inspeção geoespacial CPU-first e relatórios reproduzíveis.

## 1. CARREGAR RASTER

Abrir imagem geoespacial e ler metadados com Rasterio.

## 2. SELECIONAR BANDAS

Definir bandas RGB ou bandas necessárias para índices opcionais.

## 3. PROCESSAR PIXELS

Executar agrupamento visual reproduzível com MiniBatchKMeans.

## 4. CALCULAR ÍNDICES

Calcular NDVI ou NDWI quando bandas compatíveis forem informadas.

## 5. GERAR RELATÓRIO

Registrar parâmetros, metadados, resultados e limitações em JSON.

## Resultado e limites

MVP de inspeção visual. Agrupamentos não são classes semânticas ambientais nem diagnóstico automático.

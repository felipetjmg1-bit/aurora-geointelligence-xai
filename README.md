---
title: Aurora Geointelligence XAI — IA geoespacial experimental
emoji: "🛰️"
colorFrom: green
colorTo: blue
sdk: gradio
app_file: app.py
python_version: "3.11"
---

# Aurora GeoIntelligence XAI
**[MVP FUNCIONAL · EXPERIMENTAL]** · Python 3.11+ · Gradio · Rasterio · NumPy · scikit-learn · CPU-first · Apache-2.0

Aplicação de pesquisa para inspeção de imagens e rasters, geração de agrupamentos visuais e relatórios rastreáveis. O processamento principal utiliza CPU e bibliotecas Python abertas. O projeto busca contribuir para capacidades brasileiras em geoinformação e observação da Terra por meio de software reproduzível.

## O que está implementado
- Interface Gradio em `app.py`.
- Leitura de PNG, JPEG, TIFF e GeoTIFF, com limites de tamanho e pixels.
- Rasterio para metadados geoespaciais de TIFF/GeoTIFF quando disponível.
- Agrupamento visual RGB com MiniBatchKMeans do scikit-learn.
- Cálculo opcional de NDVI/NDWI somente quando a pessoa seleciona explicitamente as bandas.
- Exportação de resultados em pacote JSON + PNG.
- Núcleo em `src/aurora_geointelligence/core.py`, testes em `tests/` e documentação em `docs/`.

**Importante:** o agrupamento por cor não é classificação semântica de cobertura do solo. O sistema não infere sensor, calibração ou significado espectral das bandas.

## Executar em cinco minutos
Requer Python 3.11 ou superior.

```bash
git clone https://github.com/felipetjmg1-bit/aurora-geointelligence-xai.git
cd aurora-geointelligence-xai
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```
Abra o endereço local informado pelo Gradio no terminal. Para configurar a porta, defina `PORT` no ambiente, por exemplo `PORT=7860 python app.py`. O arquivo `.env.example` documenta essa configuração; a aplicação lê variáveis de ambiente e não carrega automaticamente o arquivo `.env`.

## Exemplo prático
1. Abra a interface no navegador.
2. Envie `examples/synthetic_scene.png`.
3. Escolha de 2 a 8 grupos visuais e mantenha o índice espectral como “Nenhum” para uma imagem RGB comum.
4. Execute a análise e baixe o pacote JSON + PNG.

O núcleo Python está em `src/aurora_geointelligence/core.py`; a interface Gradio é o fluxo de entrada recomendado.

## Testes
```bash
pytest
```

## Segurança, privacidade e limitações
- O processamento ocorre no processo da aplicação; proteja o serviço e os arquivos temporários.
- Não há autenticação de usuários implementada no app.
- Não use imagens com dados pessoais, localizações privadas ou informações restritas sem autorização e avaliação jurídica.
- NDVI/NDWI dependem da escolha correta de bandas e dos dados de origem; o sistema não valida calibração radiométrica nem identifica automaticamente sensor.
- Não oferece classificação temática supervisionada, segmentação semântica, detecção de mudanças temporais, poligonização georreferenciada ou laudo ambiental.
- Para LGPD, defina finalidade, base legal, minimização, retenção e controles de acesso antes de processar dados pessoais.

## Documentação
Consulte `docs/TECHNICAL_SPECIFICATION.md`, `docs/ARCHITECTURE.md`, `docs/SECURITY.md`, `docs/DATA_GOVERNANCE.md` e `docs/LIMITATIONS.md`.

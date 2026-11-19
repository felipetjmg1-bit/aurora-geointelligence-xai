---
title: Aurora Geointelligence XAI — Experimental Geospatial AI
emoji: ""
colorFrom: green
colorTo: blue
sdk: gradio
app_file: app.py
python_version: "3.11"
---

# AURORA GEOINTELLIGENCE XAI

[![Status: experimental MVP](https://img.shields.io/badge/status-experimental%20MVP-orange?style=flat-square)](docs/ABSTRACT.md)
[![Production: not ready](https://img.shields.io/badge/production-not%20ready-red?style=flat-square)](#what-this-repository-does-not-claim)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square)](requirements.txt)
[![Runtime: CPU-first](https://img.shields.io/badge/runtime-CPU--first-blue?style=flat-square)](docs/TECHNICAL_SPECIFICATION.md)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-brightgreen?style=flat-square)](LICENSE)

> **An open, experimental Python MVP for geospatial image inspection, remote-sensing exploration and traceable analysis reports.** The current baseline uses NumPy, Rasterio, Pillow and scikit-learn; it is not a PyTorch deep-learning engine and is not a production or forensic system.

## Soberania tecnológica e cooperação nacional

A Aurora Geointelligence XAI integra a agenda de pesquisa e desenvolvimento da Impulso Digital, com foco em capacidades brasileiras de inteligência artificial, geoinformação, observação da Terra, transparência técnica e governança responsável de dados.

O projeto adota uma postura colaborativa e institucionalmente respeitosa. Reconhece a importância da cooperação entre governo, universidades, institutos de pesquisa, empresas, laboratórios, comunidades técnicas e sociedade civil para ampliar a capacidade científica e tecnológica do Brasil.

A iniciativa está aberta ao diálogo técnico com órgãos públicos e programas nacionais de ciência, tecnologia e inovação, respeitando seus processos, critérios, competências e instrumentos formais. Este convite não representa parceria, financiamento, aprovação, certificação ou participação institucional já estabelecida.

A soberania tecnológica é tratada aqui como objetivo de longo prazo, construído por pesquisa, formação de pessoas, infraestrutura, interoperabilidade, código aberto, validação independente e colaboração entre instituições brasileiras.

## Technological sovereignty and national cooperation

Aurora Geointelligence XAI is part of Impulso Digital's research and development agenda, focused on Brazilian capabilities in artificial intelligence, geospatial information, Earth observation, technical transparency and responsible data governance.

The project follows a collaborative approach and respects Brazil's public institutions. It recognizes the value of cooperation among government, universities, research institutes, companies, laboratories, technical communities and civil society in strengthening the country's scientific and technological capacity.

The initiative welcomes technical dialogue with public institutions and national science, technology and innovation programs, in accordance with their processes, criteria, mandates and formal instruments. This invitation does not represent an established partnership, grant, endorsement, certification or institutional participation.

Technological sovereignty is treated as a long-term objective supported by research, skills development, infrastructure, interoperability, open source, independent validation and cooperation among Brazilian institutions.

![Visual conceitual da Aurora Geointelligence sobre a América do Sul](assets/aurora-geointelligence-hero.png)

## Project status / estado do projeto

O repositório pertence à iniciativa Impulso Digital Soluções em I.A. Ltda. e publica um **MVP experimental v0.1.0**, executável localmente em CPU. A distinção entre o que funciona, o que é direção de pesquisa e o que ainda não foi validado é parte deliberada do projeto.

| Área | Estado verificável nesta versão |
|---|---|
| Aplicação | Interface Gradio; processamento local no processo da aplicação; upload manual de imagem. |
| Imagens | PNG, JPEG, TIFF e GeoTIFF; limite de 100 MB e 50 milhões de pixels. |
| Dados | Matrizes NumPy `float32`; Rasterio lê metadados geoespaciais disponíveis em TIFF/GeoTIFF. |
| Baseline | scikit-learn `MiniBatchKMeans` determinístico sobre pixels RGB do preview; não é classificação de cobertura do solo. |
| Índices | NDVI/NDWI opcional, com bandas escolhidas pela pessoa usuária; sensor, comprimento de onda e calibração não são inferidos. |
| Saídas | Imagens derivadas e pacote ZIP com `analysis_report.json`, parâmetros e metadados disponíveis. Relatório rastreável não equivale a cadeia de custódia criptográfica. |
| PyTorch | **Não está nas dependências nem no motor desta versão.** Os dados não são `torch.Tensor`; uma avaliação futura está no roadmap. |
| XAI de modelo | **Não implementada nem validada.** Máscara/overlay mostra grupos de cor, não causalidade, atenção, Grad-CAM ou explicação de decisão de um modelo treinado. |
| Produção e uso forense | **Não prontos.** Não há benchmark anotado, validação independente, certificação, controles de produção ou cadeia de custódia para evidência judicial. |
| MLCommons | Nenhum benchmark, certificação, conformidade ou afiliação é declarado neste repositório. |
| Finep/CDTI | Nenhum financiamento, convênio, parceria, seleção ou participação em iniciativa Brasil–Espanha é declarado. Menções são convite aberto, não endosso. |

## What this repository does not claim

- Não é um serviço em produção nem um modelo geoespacial de deep learning.
- Não reivindica conformidade com MLCommons Inference, um padrão de XAI, certificação ou benchmark não publicado.
- Não declara cooperação formal com Finep, CDTI, MCTI, SETAD, Banco Central, MLCommons ou qualquer outro órgão ou organização.
- Não é ferramenta pericial validada, não produz prova judicial e não substitui profissional habilitado. Uma futura utilização em processo judicial exigiria validação independente, proveniência e licença dos dados, integridade e cadeia de custódia, revisão humana e avaliação jurídica adequada.
- Não interpreta automaticamente os clusters como água, vegetação, edificações ou uso do solo, e não comprova condição ambiental.

Badges oficiais ou de parceria só serão incluídos após evidência verificável e autorização apropriada. Os badges acima descrevem o estado atual; não são certificações.

## Technical architecture / arquitetura técnica

```text
Arquivo enviado manualmente
        │
        ├─ PNG/JPEG ── Pillow ─┐
        └─ TIFF/GeoTIFF ─ Rasterio ─ metadados disponíveis
                              │
                     matriz NumPy float32
                              │
             preview RGB (stretch percentil 2–98)
                              │
         MiniBatchKMeans no preview (random_state=42)
                 │                         │
       máscara/overlay visual      NDVI/NDWI opcional
                                  (bandas explícitas)
                 └────────────┬────────────┘
                         ZIP de saída
            JSON de relatório + imagens derivadas
```

O núcleo está em [`src/aurora_geointelligence/core.py`](src/aurora_geointelligence/core.py), a interface em [`app.py`](app.py), e a suíte local em [`tests/`](tests/). O diagrama completo está em [`assets/architecture.mmd`](assets/architecture.mmd).

O alongamento percentil 2–98 serve apenas à visualização do preview. O agrupamento usa RGB do preview, de modo que iluminação, sensor, nuvens e composição podem alterar os grupos. NDVI/NDWI só são úteis quando as bandas e a calibração da imagem são adequadas; essa semântica precisa ser fornecida e verificada pela pessoa usuária. Veja o [protocolo de validação](docs/VALIDATION_PROTOCOL.md) e as [limitações](docs/LIMITATIONS.md).

### Auditoria, explicabilidade e justiça

A versão torna etapas e parâmetros mais inspecionáveis ao registrar metadados disponíveis, configurações, resultados e ressalvas em JSON. Isso ajuda a reproduzir uma exploração, mas **não torna o resultado uma perícia**, não oferece explicação de um modelo aprendido e não assegura admissibilidade ou força probatória. Não há assinatura criptográfica nem cadeia de custódia. Não use o MVP para fiscalização, emergência, decisão ambiental/regulatória ou decisão judicial sem validação científica e revisão humana independentes.

## Dossiê do ecossistema Aurora

Os nomes abaixo compõem uma agenda comum de pesquisa e prototipagem. **Não formam uma plataforma integrada em produção.** O status de cada iniciativa e as evidências observáveis estão detalhados em [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md).

| Projeto | Escopo declarado | O que está público — e o que não deve ser inferido |
|---|---|---|
| **Aurora Geointelligence XAI / Oráculo X-37** | Inspeção geoespacial reproduzível, auditoria de processamento e geoprocessamento transparente. | Este repositório é um MVP de imagens e agrupamento visual. [Oráculo X-37](https://github.com/felipetjmg1-bit/oraculo-x37) é repositório relacionado e independente; não é um motor PyTorch integrado aqui. |
| **Aurora DREX** | Arquitetura proposta de integração soberana e auditável para fluxos de dados/serviços ligados a moedas digitais de Estado. | Não há integração operacional com Drex, Banco Central, rede financeira, piloto, autorização ou parceria declarada. |
| **Projeto Cristal / Quartzo 5D** | Pesquisa conceitual de persistência e armazenamento de longo prazo. | [API demonstrativa](https://github.com/felipetjmg1-bit/cristal-quartzo-aurora) e [simulador web](https://github.com/felipetjmg1-bit/CRISTAL-5D-V.4.0-MODULO-1). Não demonstram gravação ou leitura óptica física em quartzo. |
| **Projeto Ybyrá** | Protótipo educacional de conceitos de biocomputação, codificação inspirada em DNA e criptografia quântica. | [Repositório Ybyrá](https://github.com/felipetjmg1-bit/projeto-ybyra). Software e simulação clássica; sem tecido biológico, hardware quântico, enlace QKD real ou segurança validada para produção. |

## Chamada global: revisão independente e cooperação concreta

Desenvolvedores, pesquisadores de geoinformação e observação da Terra, universidades, institutos de pesquisa, laboratórios de Deep Tech, órgãos públicos, empresas, investidores e parceiros estratégicos estão convidados a conhecer o projeto. **A colaboração técnica, a revisão independente e a avaliação por evidências são essenciais para fortalecer a inovação brasileira.**

Comunidades técnicas internacionais e iniciativas de cooperação Brasil–Europa/Brasil–Espanha são bem-vindas para conhecer o projeto e, havendo interesse e compatibilidade de objetivos, avaliar possibilidades de colaboração. Não se declara participação, reconhecimento, parceria, financiamento ou validação por MLCommons, Finep, CDTI, MCTI/SETAD ou qualquer outra entidade. O fortalecimento da soberania tecnológica depende de capacidade científica e industrial, formação, governança, infraestrutura e soluções que possam ser executadas, avaliadas e auditadas.

Para começar, abra uma issue técnica ou envie um pull request. Propostas de colaboração devem explicitar recursos, responsabilidades, governança de dados e critérios de validação. Não envie dados pessoais, confidenciais ou sem autorização.

## Quickstart / executar localmente

Requer Python 3.11 ou superior. O baseline não exige GPU, token, banco de dados ou serviço pago.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abra `http://localhost:7860`, carregue uma imagem autorizada e selecione **Executar análise**. Para experimentar sem dados reais, use [`examples/synthetic_scene.png`](examples/synthetic_scene.png), uma composição artificial, não uma cena de satélite real.

```bash
pytest -q
```

O CI está ativo em [`.github/workflows/ci.yml`](.github/workflows/ci.yml): executa verificação de sintaxe e testes em Python 3.11 para pushes e pull requests. Consulte a aba [Actions](../../actions) para o histórico atualizado.

## Estrutura do repositório

| Caminho | Conteúdo |
|---|---|
| `app.py` | Interface Gradio. |
| `src/aurora_geointelligence/` | Núcleo de leitura, agrupamento, índices e geração de relatório. |
| `tests/` | Testes do núcleo. |
| `assets/` | Diagramas e arte conceitual, identificados como ilustração. |
| `examples/` | Cena sintética e instruções de demonstração. |
| `docs/` | Arquitetura, especificação, validação, segurança, dados, roadmap, ecossistema e contribuição. |
| `requirements.txt`, `LICENSE`, `CITATION.cff` | Dependências, licença Apache-2.0 e metadados de citação. |

## Documentação

Comece pelo [índice de documentação](docs/README.md). A documentação técnica também inclui [arquitetura](docs/ARCHITECTURE.md), [especificação](docs/TECHNICAL_SPECIFICATION.md), [resumo](docs/ABSTRACT.md), [método científico](docs/SCIENTIFIC_METHODOLOGY.md), [protocolo de validação](docs/VALIDATION_PROTOCOL.md), [limitações](docs/LIMITATIONS.md), [governança de dados](docs/DATA_GOVERNANCE.md), [segurança](docs/SECURITY.md), [roadmap](docs/ROADMAP.md), [novidade e anterioridade](docs/RESEARCH_NOVELTY.md), [ecossistema](docs/ECOSYSTEM.md), [contribuição](docs/CONTRIBUTING.md) e [citação](CITATION.cff).

## English — technical summary

Aurora Geointelligence XAI is an experimental, CPU-first Python MVP for geospatial-image inspection and reproducible exploration. It reads PNG, JPEG, TIFF and GeoTIFF imagery, records available raster metadata, creates a display preview, applies scikit-learn MiniBatchKMeans to preview RGB pixels, optionally computes NDVI/NDWI from user-selected bands, and exports images with a traceable JSON report.

The implementation uses NumPy arrays, Rasterio, Pillow, scikit-learn and Gradio. **It does not use PyTorch, contain pretrained remote-sensing weights, provide validated model-level explainability, claim scientific accuracy, or constitute a production/forensic system.** Clusters are unlabeled visual groups; spectral indices depend on correct sensor bands and calibration. No MLCommons benchmark, Finep/CDTI partnership, institutional endorsement, legal admissibility or operational DREX/Cristal/Ybyrá integration is claimed.

The project welcomes technical review and responsible cooperation with Brazilian and international researchers, institutions and industry partners. Institutional relationships are described only when supported by formal, verifiable evidence.

## License and data governance

O código original é distribuído sob [Apache-2.0](LICENSE); dependências mantêm suas próprias licenças. Não há publicação científica, DOI, certificação ou parceria institucional declarada neste repositório. Revise metadados geográficos e nomes de arquivos antes de compartilhar relatórios. Não envie dados sigilosos ou sujeitos a restrição. Consulte [`docs/DATA_GOVERNANCE.md`](docs/DATA_GOVERNANCE.md).

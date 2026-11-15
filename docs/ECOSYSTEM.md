# Aurora ecosystem dossier / Dossiê do ecossistema Aurora

## Scope and evidence / escopo e evidência

This page connects four initiatives by research direction, not by a claim of one integrated production platform. Each row states what is publicly observable and what remains a proposal, simulation or separate repository. / Esta página conecta quatro iniciativas pela direção de pesquisa, não por uma alegação de plataforma única integrada em produção. Cada seção distingue o que é observável do que permanece proposta, simulação ou repositório independente.

## 1. Aurora Geointelligence XAI and Oráculo X-37

**Research direction.** Transparent geospatial image processing, reproducibility, available-raster metadata and future model-appropriate explanations. The long-term goal is to support review and environmental accountability; this statement does not establish legal or scientific fitness.

**Current evidence.** This repository contains a CPU-first Gradio/Python MVP. Rasterio reads available TIFF/GeoTIFF metadata; NumPy arrays and Pillow handle image data/previews; scikit-learn `MiniBatchKMeans` groups RGB pixels from the display preview. User-selected band indices can be used for exploratory NDVI/NDWI calculations. Outputs include derived images and a JSON report.

**Boundary.** The MVP has no PyTorch model, pretrained remote-sensing weights, validated model-level XAI, annotated benchmark, cryptographic chain of custody or independent scientific validation. Color clusters are not land-cover classes. It is not a forensic tool or court-ready evidence.

[Oráculo X-37](https://github.com/felipetjmg1-bit/oraculo-x37) is a related but separate repository described as a collection of deterministic analysis/classification tools. It is not integrated into this geospatial MVP, and its existence does not demonstrate a trained geospatial model.

## 2. Aurora DREX — sovereign integration architecture

**Research direction.** A conceptual architecture for auditable interoperability around data and services associated with state digital currencies, with attention to governance, traceability, access control and dependency management.

**Boundary.** This repository does not demonstrate operational integration with Drex, Banco Central do Brasil, a financial network or a live pilot. No authorization, certification, regulatory approval, contract or institutional partnership is claimed. Educational Merkle demonstrations elsewhere in the ecosystem are not a production payment system, zero-knowledge proof or central-bank integration.

## 3. Projeto Cristal / Quartzo 5D — long-term persistence

**Research direction.** Explore concepts for durable information preservation and long-horizon storage.

**Public artifacts.** [Cristal de Quartzo Aurora — demonstrative API](https://github.com/felipetjmg1-bit/cristal-quartzo-aurora) and [Cristal 5D — web simulator](https://github.com/felipetjmg1-bit/CRISTAL-5D-V.4.0-MODULO-1).

**Boundary.** The public applications simulate or visualize concepts. They do not demonstrate optical encoding/decoding, physical 5D writing or reading in quartz, measured archival lifetime, or a deployed storage medium. “Quartzo 5D” names a research/prototyping direction, not a currently available physical capability.

## 4. Projeto Ybyrá — biocomputation and cryptography concepts

**Research direction.** Educational software exploring DNA-inspired digital encoding, simple explainability ideas, and concepts associated with quantum cryptography.

**Public artifact.** [Projeto Ybyrá — Árvore-Mãe](https://github.com/felipetjmg1-bit/projeto-ybyra).

**Boundary.** The repository is a software prototype using synthetic/digital data and classical simulation of stages of BB84, plus a Merkle-inclusion demonstration. It does not demonstrate living-tissue computation, biological hardware, a quantum link or real QKD, a verified security proof, or a production-ready security system.

## Independent review and institutional relations

Engineers, Earth-observation researchers, Deep Tech funds and international research groups are welcome to inspect the code, report defects and propose reproducible benchmarks. References to MLCommons, Finep/CDTI, Brazil–Europe cooperation, MCTI/SETAD or other institutions are invitations or contextual references only. **No affiliation, endorsement, funding, certification, participation or partnership is claimed without a separate, publicly verifiable record.**

A future institutional or court-related application would require an independently validated method, documented data rights/provenance, privacy review, integrity controls, appropriate human review and fit-for-purpose legal/scientific assessment. None of those future requirements should be inferred from the existence of this software prototype.

## Português — resumo

O ecossistema Aurora é uma agenda de pesquisa e prototipagem, não uma plataforma integrada em produção. Aurora Geointelligence XAI é hoje um MVP de inspeção e agrupamento visual, sem PyTorch, modelo geoespacial treinado ou XAI de decisão validada. O Aurora DREX é uma proposta, não integração com o Banco Central. Cristal/Quartzo 5D tem API demonstrativa e simulador, não gravação/leitura física em quartzo. Ybyrá é protótipo de software, sem tecido vivo nem enlace quântico real. Menções a MLCommons, Finep/CDTI, cooperação Brasil–Europa ou órgãos públicos não afirmam vínculo institucional, financiamento, certificação ou endosso.

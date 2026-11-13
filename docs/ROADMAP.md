# Roadmap / Roteiro de evolução

## Português

1. **Fase 1 — MVP funcional:** upload, metadados, preview, agrupamento baseline, índices com bandas explícitas, exportação JSON/PNG e testes. Implementação inicial concluída; 11 testes passaram localmente e o Gradio respondeu ao smoke test HTTP em 13/11/2026. O modelo de workflow está documentado em `docs/GITHUB_ACTIONS_WORKFLOW.yml`; a ativação no GitHub aguarda permissão oficial para escrever em `.github/workflows/`.
2. **Fase 1.1 — endurecimento:** revisão de compatibilidade e acessibilidade móvel; perfis de execução para TIFF grandes; execução contínua de CI e correções conforme resultados.
3. **Fase 2 — modelo geoespacial pré-treinado:** comparar pesos públicos por licença, finalidade de treinamento, sensor/bandas, custo de download e inferência em CPU; selecionar somente após avaliação documentada. Manter clustering atual como baseline e fallback honesto.
4. **Fase 3 — ingestão autorizada STAR.VISION/OSE:** somente após documentação oficial, licença, autorização e metadados confirmados; caso contrário, manter importação manual.
5. **Fase 4 — tarefas ambientais e temporais:** dados abertos com licença verificada, rótulos de referência, mudança entre cenas e validação espacial independente.
6. **Fase 5 — módulos especialistas:** água, vegetação e urbanização como modelos separados, com conjuntos de referência e documentação de desempenho; não inferir poluição química apenas de imagem óptica.
7. **Fase 6 — XAI e publicação científica:** explicabilidade apropriada ao modelo, análise de fidelidade, limitações, validação externa e revisão científica.

Os marcos não prometem resultados científicos. Integrações e módulos só serão anunciados depois de implementados e testados.

## English

1. **Phase 1 — functional MVP:** upload, metadata, preview, baseline clustering, explicit-band indices, JSON/PNG export and tests. The initial implementation is complete; 11 tests passed locally and Gradio responded to an HTTP smoke test on 13 Nov 2026. The workflow template is in `docs/GITHUB_ACTIONS_WORKFLOW.yml`; enabling it on GitHub awaits official permission to write under `.github/workflows/`.
2. **Phase 1.1 — hardening:** mobile compatibility/accessibility review, large-TIFF execution profiles, continuous CI and fixes based on results.
3. **Phase 2 — pretrained geospatial model:** compare public weights by license, training purpose, sensor/bands, download cost and CPU inference; select only after documented evaluation. Keep current clustering as an honest baseline/fallback.
4. **Phase 3 — authorized STAR.VISION/OSE ingestion:** only after official documentation, license, authorization and metadata are verified; otherwise retain manual import.
5. **Phase 4 — environmental and temporal tasks:** open licensed data, reference labels, between-scene change analysis and independent spatial validation.
6. **Phase 5 — specialist modules:** water, vegetation and urban models as separate tasks with reference data and performance documentation; do not infer chemical pollution from optical imagery alone.
7. **Phase 6 — XAI and scientific publication:** model-appropriate explanations, fidelity analysis, limitations, external validation and scientific review.

# Matriz de anterioridade tecnológica — MVP Aurora

## Escopo e critério de leitura

Este documento compara somente as informações dos resultados JSON fornecidos. A descrição de Aurora é hipotética e limitada a: organização de imagens geoespaciais e metadados, processamento explicável e interface modular em Gradio. Não foram fornecidos código, demonstração, arquitetura, resultados de testes, inventário de dados ou evidências de implementação do Aurora. Portanto, a matriz distingue capacidades documentadas das soluções citadas de características apenas atribuídas ao MVP; não infere equivalência, desempenho, prioridade, novidade jurídica ou patenteabilidade.

As referências numéricas apontam para as fontes citadas nos resultados fornecidos. Cada afirmação factual da matriz traz as referências pertinentes imediatamente junto à afirmação. “Não descrito nas fontes consultadas” significa apenas que essa capacidade não aparece nos resultados apresentados, não que seja impossível.

## Matriz comparativa

| Tecnologia | Capacidades comprovadas nos resultados fornecidos | Limites e ressalvas comprovados | Relação factual com a descrição do Aurora |
|---|---|---|---|
| **Google Earth Engine (GEE)** | Reúne catálogo público de imagens de satélite e dados geoespaciais, permite incorporar dados do usuário e oferece computação distribuída gerenciada em modos interativo e em lote. Há interfaces Python e JavaScript, ferramentas de visualização, exportação raster/vetorial e recursos de ML para regressão, classificação, segmentação e avaliação de acurácia, com integração ao Vertex AI para fluxos avançados. [1][2] | A plataforma impõe limites de concorrência, solicitações, armazenamento, tarefas, memória, duração, agregações, payload e filas. Projetos não comerciais têm quotas mensais diferenciadas por tier desde 27/04/2026, com implantação gradual; ao esgotá-las, o projeto pode entrar em modo restrito. Uso comercial requer plano comercial sujeito a cobranças; a gratuidade não comercial não equivale a uso comercial gratuito. Os termos diferenciam atividades comerciais e não comerciais. A ressalva sobre recursão no artigo de 2017 é histórica e não comprova indisponibilidade atual. [3][4][5][6] | A sobreposição é em dados geoespaciais, análise e apresentação de resultados. Os resultados descrevem GEE como catálogo amplo e computação gerenciada em escala; descrevem Aurora como organização de conteúdo, processamento explicável e interface Gradio modular. Não há dados fornecidos para comparar implementação, desempenho, fontes de dados ou integrações do Aurora. [1][2][3][4][5][6] |
| **Microsoft Planetary Computer (catálogo público e Pro)** | O catálogo público oferece dados de observação da Terra e ambientais, descoberta STAC com busca espacial/temporal, APIs de metadados, acesso a ativos e ferramentas de visualização. Há tutoriais de análise com ferramentas como Dask, mas para produção a documentação recomenda computação própria próxima aos dados. O produto separado Planetary Computer Pro oferece GeoCatalogs STAC gerenciados, ingestão de dados próprios, Explorer e APIs de mosaico/tiles. [7][8][9][10][11][12] | Nem todas as coleções hospedadas estão indexadas na STAC API; certos ativos exigem SAS, os tokens expiram e pode haver limites de taxa/egress. O catálogo público é descrito como preview nos resultados e os termos suplementares citados preveem disponibilidade “as-is/as-available”, sem compromisso de SLA, podendo ser alterado ou descontinuado. Gratuidade anunciada do catálogo público não se estende automaticamente ao Pro, cobrado por uso Azure. Licenças variam por coleção. Recursos vetoriais e Private Link no Pro são indicados como preview nas fontes fornecidas. [8][11][13][14][15][16][17] | Há sobreposição com descoberta, metadados e visualização geoespacial. Para gestão/ingestão de dados próprios, a aproximação mais direta descrita é com o Pro, que é produto separado do catálogo público. As fontes consultadas não descrevem o catálogo como app Gradio nem como fluxo geral de processamento explicável. A comparação situa Aurora, se implementado como descrito, como possível camada de aplicação/processamento; não prova exclusividade ou superioridade. [7][8][9][10][11][12] |
| **TorchGeo** | Biblioteca Python do ecossistema PyTorch para aprendizado profundo geoespacial. Inclui datasets e benchmarks, composição de datasets por união/interseção, uso de metadados espaciais, amostragem espacial/temporal, transforms, modelos e pesos pré-treinados, além de componentes de treino/avaliação com PyTorch Lightning. O artigo relata benchmarks reproduzíveis e pré-processamento em tempo de execução. [18][19][20][21] | É uma biblioteca e não um aplicativo de catálogo/gestão com interface de usuário. As fontes consultadas não estabelecem módulo geral de explicabilidade; reprodutibilidade do pipeline não equivale a explicar resultados. O código é MIT, mas licenças de datasets variam, e certos datasets/modelos exigem dependências opcionais ou configuração. A versão 0.10.1 citada é uma observação datada. [19][20][21][22][23] | Há sobreposição potencial na composição e processamento programático de imagens geoespaciais, sobretudo em aplicações com PyTorch. O escopo descrito de TorchGeo é uma biblioteca de componentes para pipelines de ML, enquanto Aurora é descrito como aplicação com organização, explicabilidade e interface Gradio modular. Os dados fornecidos não comprovam que Aurora implementa esses elementos ou que supera a biblioteca. [18][19][20][21] |
| **SamGeo / Segment Anything for Geospatial** | Adapta modelos Segment Anything a imagens e fluxos geoespaciais, incluindo GeoTIFF; oferece segmentação por prompts e geração automática de máscaras, exportação de resultados a formatos geoespaciais, visualização em mapas, suporte documentado a séries temporais e API REST. A documentação contempla SAM 3 e recursos de texto para outros fluxos conforme dependências. [24][25][26][27] | Segmentação e scores de máscara não equivalem a gestão de acervo, proveniência explicável ou validação de exatidão. A documentação recomenda GPU potente e pelo menos 8 GB de memória para conjuntos grandes; SAM 3 tem requisitos de instalação e acesso a checkpoints sujeito a solicitação/aprovação. No fluxo SamGeo3, GeoTIFF com mais de três bandas usa por padrão três bandas como RGB, sem consumo automático de todo o espectro. É necessário distinguir a licença MIT do pacote das licenças dos modelos e dependências; SAM 3 usa licença própria. A versão v1.4.2 é o retrato de releases fornecido. [25][26][28][29][30][31][32] | Há sobreposição potencial no processamento de imagens e segmentação, com exportação e API. A descrição fornecida não apresenta SamGeo como sistema de organização e gestão geral de imagens/metadados, nem como explicação geral do processamento ou interface Gradio modular. Isso diferencia escopos descritos, sem demonstrar ausência de funções não listadas ou novidade do Aurora. [24][25][26][27] |
| **NASA-IBM Prithvi (família Prithvi-EO)** | Família de modelos-base de visão Transformer para observação da Terra. EO-2.0 é descrito como pré-treinado por masked autoencoder em 4,2 milhões de amostras globais HLS, com seis bandas e resolução de 30 m; versões de 300M e 600M parâmetros são mencionadas no artigo. Pesos, inferência, demonstração e exemplos de ajuste fino estão disponíveis; tarefas downstream listadas incluem segmentação, classificação e estimativas geoespaciais. [33][34][35][36][37] | É especializado em entradas ópticas HLS e não é universal para qualquer sensor, resolução ou modalidade; formatos e pré-processamento podem exigir adaptação. Desempenhos dependem de tarefas, dados e configurações avaliados e não garantem resultados locais. O modelo em si não é explicação causal/trilha de auditoria nem catálogo ou sistema geral de gestão de metadados. Licenças do checkpoint e do repositório são específicas aos respectivos artefatos e não substituem a verificação de dados, dependências e outros checkpoints. [35][36][37][38] | A sobreposição é potencialmente complementar: Aurora, se implementado como descrito, poderia organizar e apresentar um fluxo e chamar um checkpoint compatível como componente analítico. Embeddings espaço-temporais/geográficos nas variantes TL não são equivalentes a gestão geral de metadados; os materiais fornecidos não descrevem Prithvi como aplicação de gestão, interface Gradio ou sistema de explicabilidade. [33][34][35][36][37] |

## Síntese comparativa

Os resultados fornecidos mostram que capacidades geoespaciais relevantes ao problema já existem em soluções de tipos diferentes: GEE e Planetary Computer oferecem catálogo/descoberta e serviços de acesso ou computação; TorchGeo oferece componentes de biblioteca para pipelines de aprendizado de máquina; SamGeo oferece fluxos de segmentação geoespacial; Prithvi oferece modelos-base reutilizáveis para tarefas de observação da Terra. Essas categorias não são intercambiáveis e apresentam limites distintos de escopo, recursos, acesso, licenciamento e operação. [1][7][8][18][19][24][25][33][35]

Na descrição hipotética, o Aurora combina organização de imagens/metadados, processamento explicável e interface modular em Gradio. Os resultados de terceiros comprovam sobreposições parciais em dados, processamento, ML, segmentação ou apresentação, mas não permitem confirmar se essa combinação está implementada no Aurora, como funciona, se é tecnicamente diferente em aspectos específicos ou se produz resultados melhores. Tampouco permitem concluir que os produtos listados não ofereçam funcionalidades adicionais além das aqui documentadas.

## Conclusão

A matriz identifica anterioridade funcional e técnica em várias partes do espaço de problema: catálogos geoespaciais, computação distribuída, APIs STAC, bibliotecas de pipelines de ML, segmentação de imagens e modelos-base de observação da Terra já são documentados nas fontes fornecidas. Ao mesmo tempo, os materiais descrevem produtos e camadas distintos, com capacidades e limites próprios, e não demonstram equivalência integral com a configuração atribuída ao MVP Aurora.

Assim, a conclusão equilibrada é que existe sobreposição parcial e complementaridade potencial, não uma comparação validada de implementação. Com os dados disponíveis, não se deve alegar ineditismo mundial, inovação, superioridade, equivalência funcional ou patenteabilidade. Uma avaliação mais específica exigiria evidências do próprio Aurora (código/versão, arquitetura, fluxos demonstráveis, dados e testes) e análise apropriada do escopo técnico e jurídico pertinente.

## Referências


[1]: https://developers.google.com/earth-engine/guides "Google Earth Engine, documentação oficial — guias"

[2]: https://doi.org/10.1016/j.rse.2017.06.031 "Gorelick et al. (2017), “Google Earth Engine: Planetary-scale geospatial analysis for everyone”, *Remote Sensing of Environment*"

[3]: https://developers.google.com/earth-engine/guides/usage "Google Earth Engine, quotas e uso"

[4]: https://developers.google.com/earth-engine/guides/noncommercial_tiers "Google Earth Engine, tiers não comerciais"

[5]: https://cloud.google.com/earth-engine/pricing "Google Cloud, preços do Earth Engine"

[6]: https://earthengine.google.com/terms/ "Google Earth Engine, Termos de Serviço"


[7]: https://planetarycomputer.microsoft.com/docs/overview/about/ "Microsoft Planetary Computer, visão geral"

[8]: https://planetarycomputer.microsoft.com/docs/concepts/data-catalog/ "Microsoft Planetary Computer, catálogo de dados"

[9]: https://learn.microsoft.com/en-us/azure/planetary-computer/microsoft-planetary-computer-pro-overview "Microsoft Learn, Planetary Computer Pro: funcionalidades"

[10]: https://learn.microsoft.com/en-us/azure/planetary-computer/whats-new "Microsoft Learn, novidades do Planetary Computer Pro"

[11]: https://planetarycomputer.microsoft.com/docs/reference/stac/ "Microsoft Planetary Computer, documentação da API STAC"

[12]: https://github.com/microsoft/planetary-computer-apis "Microsoft GitHub, APIs do Planetary Computer"

[13]: https://planetarycomputer.microsoft.com/docs/concepts/sas/ "Microsoft Planetary Computer, uso de tokens para acesso a dados"

[14]: https://planetarycomputer.microsoft.com/docs/concepts/computing/ "Microsoft Planetary Computer, computação com o catálogo"

[15]: https://planetarycomputer.microsoft.com/terms "Microsoft Planetary Computer, termos suplementares de preview"

[16]: https://learn.microsoft.com/en-us/azure/planetary-computer/service-usage-meters "Microsoft Learn, métricas de uso e cobrança do Planetary Computer Pro"

[17]: https://planetarycomputer.microsoft.com/catalog "Microsoft Planetary Computer, catálogo e proveniência dos conjuntos"


[18]: https://docs.torchgeo.org/en/stable/ "TorchGeo, documentação oficial estável"

[19]: https://docs.torchgeo.org/en/stable/api/datasets.html "TorchGeo, API de datasets"

[20]: https://docs.torchgeo.org/en/stable/user/installation.html "TorchGeo, instalação e dependências opcionais"

[21]: https://github.com/torchgeo/torchgeo "TorchGeo, repositório oficial"

[22]: https://docs.torchgeo.org/en/stable/user/contributing.html "TorchGeo, licença e orientações de contribuição"

[23]: https://github.com/torchgeo/torchgeo/releases "TorchGeo, releases oficiais"


[24]: https://samgeo.gishub.org/ "SamGeo, documentação oficial"

[25]: https://samgeo.gishub.org/api/ "SamGeo, API"

[26]: https://samgeo.gishub.org/samgeo3/ "SamGeo, documentação SAMGeo3"

[27]: https://github.com/opengeos/segment-geospatial "OpenGeo, repositório oficial segment-geospatial"

[28]: https://github.com/opengeos/segment-geospatial/blob/main/LICENSE "OpenGeo, licença do pacote segment-geospatial"

[29]: https://github.com/opengeos/segment-geospatial/blob/main/pyproject.toml "OpenGeo, dependências e configuração do projeto"

[30]: https://github.com/facebookresearch/segment-anything/blob/main/LICENSE "Meta, repositório do Segment Anything"

[31]: https://github.com/facebookresearch/sam3 "Meta, repositório SAM 3"

[32]: https://github.com/facebookresearch/sam3/blob/main/LICENSE "Meta, licença SAM 3"


[33]: https://science.nasa.gov/science-research/ai-geospatial-model-earth/ "NASA, “Expanded AI Model with Global Data Enhances Earth Science Applications”"

[34]: https://www.earthdata.nasa.gov/news/nasa-ibm-openly-release-geospatial-ai-foundation-model-nasa-earth-observation-data "NASA Earthdata, “NASA and IBM Openly Release Geospatial AI Foundation Model for NASA Earth Observation Data”"

[35]: https://arxiv.org/abs/2412.02732 "Szwarcman et al., “Prithvi-EO-2.0: A Versatile Multi-Temporal Foundation Model for Earth Observation Applications”"

[36]: https://arxiv.org/abs/2310.18660 "Jakubik et al., “Foundation Models for Generalist Geospatial Artificial Intelligence”"

[37]: https://huggingface.co/ibm-nasa-geospatial/Prithvi-EO-2.0-300M-TL "Hugging Face, checkpoint Prithvi-EO-2.0-300M-TL e model card"

[38]: https://github.com/NASA-IMPACT/Prithvi-EO-2.0 "NASA-IMPACT, repositório Prithvi-EO-2.0"

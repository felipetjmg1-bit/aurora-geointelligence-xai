# Governança de IA Explicável (XAI)

**Status:** especificação de governança para o MVP experimental. Este documento não declara que todos os mecanismos descritos já estejam implementados.

## Escopo atual verificável

A versão atual executa agrupamento visual não supervisionado com MiniBatchKMeans sobre pixels RGB de pré-visualização, com semente fixa. Os grupos são identificadores numéricos arbitrários, não classes ambientais. NDVI/NDWI são opcionais e dependem da seleção explícita de bandas pelo usuário. O relatório registra parâmetros e metadados disponíveis.

## Conteúdo mínimo de uma explicação

- Identificador único da execução e versão/commit do software;
- Nome, tamanho e hash criptográfico do arquivo de entrada (hash ainda a implementar no relatório);
- Data/hora UTC, parâmetros, algoritmo, versões de dependências e semente;
- Metadados geoespaciais disponíveis, distinguindo ausência de inferência;
- Número de grupos solicitado e efetivo, proporções e estatísticas descritivas;
- Bandas selecionadas e fórmula, quando houver índice espectral;
- Limitações, avisos e motivo de dados ausentes;
- Artefatos gerados e respectivos hashes (a implementar).

## Linguagem permitida

Use “grupo visual”, “segmentação exploratória” e “índice calculado com as bandas informadas”. Não use “identificou floresta”, “detectou água”, “diagnosticou degradação” ou alegações de acurácia sem modelo semântico, referência e avaliação independente.

## Confiança e incerteza

O MVP não produz probabilidade calibrada, intervalo de confiança estatístico nem confiança semântica. Não converter proporção de pixels ou distância de cluster em probabilidade de classe. Até existir método validado, declarar “confiança não estimada”.

## Supervisão humana

Toda interpretação ambiental deve ser revisada por pessoa qualificada e confrontada com metadados do sensor, resolução espacial, data de aquisição, condições atmosféricas e dados de referência. O software não deve tomar decisões administrativas, regulatórias ou ambientais autonomamente.

## Trilha de auditoria e proteção de dados

Evolução planejada: hashes SHA-256 de entrada e saídas; identificador de execução; manifesto JSON versionado; versão do código e dependências; armazenamento controlado e retenção definida pelo operador. Não registrar conteúdo sensível, credenciais ou caminhos locais desnecessários. O relatório atual não equivale a cadeia de custódia nem a log imutável.

## Matriz de maturidade

| Capacidade | Estado nesta versão | Próxima evidência necessária |
|---|---|---|
| Agrupamento visual determinístico | Implementado | Testes em conjuntos externos |
| Metadados raster | Parcialmente implementado | Testes multi-sensor e casos-limite |
| NDVI/NDWI por bandas explícitas | Implementado | Verificação com dados calibrados |
| Explicação semântica de classes | Não implementado | Modelo validado e protocolo anotado |
| Confiança calibrada | Não implementado | Calibração e avaliação independente |
| Hash de entrada e artefatos | Planejado | Implementação e testes |
| Proveniência de execução/commit | Parcial | Manifesto completo e verificável |
| Revisão humana | Procedimento recomendado | Registro de revisão e critérios |

## Protocolo mínimo de validação

1. Congelar versão do código, dependências e conjunto de dados.
2. Documentar sensor, bandas, resolução, CRS, datas e pré-processamento.
3. Definir hipótese e métricas antes dos testes.
4. Usar dados de referência independentes e separar conjuntos quando houver modelo supervisionado.
5. Reportar resultados por classe, matriz de confusão e incerteza quando aplicável.
6. Publicar limitações, falhas conhecidas e instruções de reprodução.
7. Submeter a revisão técnica independente antes de alegações operacionais.

## Referências

- Núcleo: ../src/aurora_geointelligence/core.py
- Limitações: LIMITATIONS.md
- Segurança: SECURITY.md
- Validação: VALIDATION_PROTOCOL.md

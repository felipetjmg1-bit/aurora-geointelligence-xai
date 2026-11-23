# Evidências de execução e interface

## Escopo

Este fluxo instala as dependências declaradas, executa a suíte de testes, inicia o aplicativo Gradio real e usa Chromium/Playwright para verificar elementos visíveis e capturar a interface em desktop e mobile.

As imagens geradas por este workflow são capturas da interface real do Aurora GeoIntelligence XAI em execução no runner do GitHub Actions. Elas não são capturas do portal de portfólio nem evidência de implantação pública.

## O que a execução comprova

- O ambiente de CI conseguiu instalar as dependências.
- Os testes automatizados existentes passaram, se o job terminar com sucesso.
- O servidor Gradio iniciou e respondeu HTTP 200.
- Os elementos principais da interface foram encontrados pelo Playwright.
- Foram geradas capturas desktop e mobile do aplicativo iniciado no próprio job.

## O que não comprova

- Disponibilidade pública, autenticação, isolamento multiusuário ou prontidão para produção.
- Validação científica independente, acurácia de classificação ou desempenho em hardware de campo.
- Correção de interpretação de bandas para qualquer sensor sem configuração e validação específicas.
- Segurança completa ou conformidade regulatória.

## Como consultar

Abra a execução do workflow **Aurora GeoIntelligence interface evidence** em GitHub Actions e baixe o artefato `aurora-geointelligence-real-interface`. O artefato contém as capturas e o log de inicialização.

O resultado deve ser considerado válido somente quando o workflow estiver concluído com estado `success` e o artefato estiver presente.

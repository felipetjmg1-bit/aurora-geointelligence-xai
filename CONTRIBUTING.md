# Como Contribuir

Obrigado pelo interesse no Aurora GeoIntelligence XAI.

## Princípios

- Preserve o foco CPU-first e não adicione dependência de GPU sem proposta técnica explícita.
- Não descreva grupos visuais como classes ambientais validadas.
- Não inclua dados pessoais, imagens protegidas ou credenciais.
- Mantenha documentação e testes coerentes com o comportamento real.

## Fluxo recomendado

1. Abra uma issue descrevendo problema, motivação e impacto.
2. Crie branch específica a partir de main.
3. Faça mudanças pequenas e verificáveis.
4. Adicione ou atualize testes para o comportamento alterado.
5. Execute python -m compileall -q src app.py tests e python -m pytest.
6. Atualize documentação e informe limitações remanescentes.
7. Abra pull request com resumo, testes executados e riscos conhecidos.

## Critérios de aceite

- Mudança reproduzível e compatível com Python 3.11.
- Sem segredos ou dados sensíveis.
- Testes relevantes adicionados ou atualizados.
- Afirmações de desempenho e XAI acompanhadas de evidência verificável.

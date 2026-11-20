# Política de Segurança

## Escopo

Esta política cobre o MVP experimental Aurora GeoIntelligence XAI.

## Reporte responsável

Não publique detalhes de vulnerabilidades não corrigidas em issues públicas. Encaminhe um relato privado ao mantenedor pelo canal de contato disponível no perfil GitHub do proprietário. Inclua versão/commit afetado, passos para reproduzir, impacto observado e evidências sem dados pessoais ou segredos.

## Dados e credenciais

- Nunca envie tokens, senhas, chaves privadas ou arquivos .env reais ao repositório.
- Use apenas valores fictícios em .env.example.
- Não carregue dados pessoais, sigilosos ou imagens sem autorização.
- Revise dependências e permissões antes de implantar em ambiente compartilhado.

## Limitações atuais

A interface Gradio não implementa autenticação multiusuário nem controle de acesso por perfil. Não a exponha como serviço público para dados sensíveis sem autenticação, isolamento, limites operacionais, monitoramento e política de retenção.

## Resposta a incidentes

1. Preserve logs e commit hashes relevantes sem copiar segredos.
2. Avalie escopo, dados potencialmente expostos e versões afetadas.
3. Revogue credenciais comprometidas no provedor correspondente.
4. Corrija em branch isolada, adicione teste de regressão e documente a correção.
5. Publique aviso coordenado após mitigação, quando necessário.

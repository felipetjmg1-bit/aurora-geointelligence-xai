# Security / Segurança

## Português

O núcleo limita extensões, bytes e número de pixels e delega a decodificação a Pillow/Rasterio. Trate uploads como não confiáveis; mantenha dependências atualizadas, limite recursos de processo, use ambiente isolado e exponha o Gradio somente atrás de TLS e controles de acesso adequados quando houver dados não públicos. O servidor não implementa login, controle de acesso, quotas por usuário ou antivírus. Por padrão, não faça upload de dados sensíveis a uma instância pública.

Segredos pertencem ao armazenamento seguro de CI/Hugging Face, nunca a código, issues, logs ou histórico Git. O repositório inclui GitHub Actions com dependências sem credenciais. Revise proveniência e licença antes de incluir dados. Para relatar vulnerabilidades, contate os mantenedores por um canal privado da organização; nenhum endereço de segurança foi especificado neste pacote.

## English

The core limits file extensions, bytes and pixel count and delegates decoding to Pillow/Rasterio. Treat uploads as untrusted; keep dependencies current, constrain process resources, use an isolated environment, and expose Gradio only behind TLS and suitable access controls when non-public data is involved. The server does not implement login, access controls, per-user quotas or antivirus. Do not upload sensitive data to a public instance by default.

Secrets belong in secure CI/Hugging Face secret storage, never in code, issues, logs or Git history. The repository includes GitHub Actions without credentials. Review provenance and license before adding data. Report vulnerabilities privately to organization maintainers; no security contact address was specified in this package.

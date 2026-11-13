# Data governance / Governança de dados

## Português

O MVP processa a imagem no processo local da aplicação e não envia dados a uma API de inferência externa. Quando implantado publicamente no Hugging Face Spaces, os arquivos submetidos passam a ser recebidos pela infraestrutura do provedor; leia as políticas e controles atuais do provedor antes de carregar dados sensíveis. Não use dados pessoais, restritos, licenciados de forma incompatível ou sujeitos a sigilo.

Para cada cenário de pesquisa, mantenha fora do repositório a fonte bruta salvo quando a licença permitir redistribuição. Registre proprietário, URL/fonte, licença, permissão, sensor, data, resolução, bandas, CRS e transformações. Remova metadados pessoais e coordenadas sensíveis quando não forem necessárias. Os relatórios exportados contêm o nome do arquivo e metadados geográficos disponíveis; revise-os antes de compartilhar.

A distribuição inicial não inclui arquivos de imagens de satélite reais, dados STAR.VISION, tokens, senhas, credenciais ou dados de usuários. As imagens conceituais originais e a amostra sintética são identificadas como tais.

## English

The MVP processes an image in the application process and does not send data to an external inference API. When deployed publicly on Hugging Face Spaces, uploads are received by the provider's infrastructure; review the provider's current policies and controls before uploading sensitive data. Do not use personal, restricted, incompatibly licensed or confidential data.

Keep raw research data outside the repository unless its license permits redistribution. Record owner, URL/source, license, permission, sensor, acquisition date, resolution, bands, CRS and transformations. Remove personal metadata and sensitive coordinates when unnecessary. Exported reports contain the file name and available geographic metadata; review them before sharing.

The initial distribution includes no real satellite imagery, STAR.VISION data, tokens, passwords, credentials or user data. Original concept art and the synthetic sample are identified as such.

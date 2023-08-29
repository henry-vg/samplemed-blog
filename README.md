## Começando
Siga os passos abaixo para executar o projeto em sua máquina local:

1. Clone o repositório para o seu ambiente local:

```bash
git clone git@github.com:henry-vg/samplemed-blog.git
```

2. Navegue até o diretório do projeto:

```bash
cd samplemed-blog
```

3. Execute o Docker Compose para iniciar o servidor:

```bash
docker compose up
```
4. Acesse a coleção do Postman:
Na pasta **docs/** do diretório raiz, você encontrará três arquivos:

- **schema.dbml**: Este arquivo contém o esquema das relações do banco de dados, conforme solicitado.
- **schema.png**: Este arquivo é uma representação gráfica do esquema das relações do banco de dados.
- **postman.json**: Importe este arquivo no Postman para visualizar a coleção de rotas.

## Utilização

Após iniciar o servidor com o Docker Compose, siga estas etapas para começar a utilizar o sistema:

1. Crie uma conta de usuário:

- Faça uma requisição POST para o endpoint **`/user/`** com os detalhes do usuário (no mínimo **username**, **email** e **password**).
- Use as credenciais para obter um token de autenticação no endpoint **`/api/token/`**.

2. Autenticação:

- Adicione o token **access** obtido na resposta no **Authorization** da Collection, como tipo **Bearer Token**.

3. Acesse as rotas da coleção do Postman para interagir com o sistema.

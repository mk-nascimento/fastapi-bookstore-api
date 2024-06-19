
# FastAPI Bookstore API

Esta é uma aplicação RESTful API construída com FastAPI, SQLAlchemy, PostgreSQL e gerenciada pelo Poetry.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em sua máquina:

- [![PostgreSQL 16+](https://img.shields.io/badge/PostgreSQL-16+-blue.svg?logo=postgresql)](https://www.postgresql.org/download/)
- [![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python)](https://www.python.org/downloads/release/python-3110/)
- [![Poetry 1.8+](https://img.shields.io/badge/Poetry-1.8+-blue.svg?logo=poetry)](https://python-poetry.org/docs/#installation)

## Configuração do Ambiente

1. Clone o repositório:

    ```bash
    git clone https://github.com/mk-nascimento/fastapi-bookstore-api.git
    cd fastapi-bookstore-api
    ```

2. Instale as dependências:

    - Poetry
        > Antes de prosseguir com a instalação, é recomendado verificar a versão do Python e Poetry recomendada no topo deste arquivo. Certifique-se de ter a versão correta instalada em seu sistema antes de continuar.
        ```bash
        poetry install
        ```

    - Ou, se você preferir usar pip:
        > Antes de prosseguir com a instalação, é recomendado verificar a versão do Python recomendada no topo deste arquivo. Certifique-se de ter a versão correta instalada em seu sistema antes de continuar.
        ```bash
        pip install -r requirements.txt
        ```

3. Crie e configure o banco de dados PostgreSQL. Em seguida, crie um arquivo `.env` na raiz do projeto baseado no arquivo [.env.example](.env.example):

    - Copie o conteúdo de [.env.example](.env.example) para um novo arquivo `.env` e atualize as credenciais conforme necessário:

        ```bash
        cp .env.example .env
        ```

4. Ative o ambiente virtual:

    - Poetry:

        ```bash
        poetry shell
        ```

    - Ou, caso utilize um ambiente virtual criado com `venv`:

        ```bash
        # Crie um ambiente virtual com o nome desejado, substituindo "<sua_venv>" por um nome escolhido:
        python -m venv <sua_venv>
        ```

        - Sistemas Unix-like "Linux/Mac":
        ```bash
        source <sua_venv>/bin/activate  # Linux/Mac
        ```

        - Sistemas Windows:
        ```bash
        <sua_venv>\Scripts\activate     # Windows
        ```

5. Execute as migrações do banco de dados:

    ```bash
    alembic upgrade head
    ```

## Rodando a Aplicação

Execute a aplicação com o comando:

```bash
uvicorn bookstore.main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

## Licença

Este projeto está licenciado sob a licença Apache 2.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

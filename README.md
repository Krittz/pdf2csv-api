# PDF to CSV Converter API

![GitHub last commit](https://img.shields.io/github/last-commit/seu_usuario/pdf2csv-api)
![GitHub issues](https://img.shields.io/github/issues/seu_usuario/pdf2csv-api)
![GitHub stars](https://img.shields.io/github/stars/seu_usuario/pdf2csv-api?style=social)

## Descrição

O **PDF to CSV Converter API** é um serviço web desenvolvido em FastAPI que permite converter tabelas de arquivos PDF em arquivos CSV. Este serviço é ideal para automatizar o processo de extração de dados de documentos PDF estruturados.

## Funcionalidades

- **Conversão de Tabelas**: Extraia tabelas de arquivos PDF e converta-as em formato CSV.
- **Seleção de Colunas**: Especifique quais colunas deseja extrair das tabelas do PDF.
- **Resposta Amigável**: Retorne respostas estruturadas em JSON em caso de erros, facilitando o debugging e a integração com outros sistemas.

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e eficiente para desenvolvimento de APIs web.
- **Uvicorn**: Servidor ASGI para rodar aplicações FastAPI.
- **Pdfplumber**: Biblioteca para extração de texto e tabelas de arquivos PDF.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Docker**: Plataforma para desenvolvimento, envio e execução de aplicativos em contêineres.
- **Docker Compose**: Ferramenta para definir e executar aplicações multi-container.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estrutura do Projeto

```bash
pdf2csv-api/
├── Dockerfile # Definição do ambiente Docker
├── docker-compose.yml # Configuração do Docker Compose
├── main.py # Código-fonte da API FastAPI
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto
```

## Instruções de Uso

### 1. Clonar o Repositório

Clone o repositório para o seu diretório local:

```bash
git clone https://github.com/seu_usuario/pdf2csv-api.git
cd pdf2csv-api
```

### 2. Construir a Imagem Docker
Construa a imagem Docker utilizando o Docker Compose:

```bash
docker-compose build
```

### 3. Executar o Container
Execute o container para iniciar o serviço FastAPI:
```bash
docker-compose up
```

### 4. Acessar a Documentação da API
Após o container estar em execução, você pode acessar a documentação interativa da API em:

* **Swagger UI:**`http://localhost:8000/docs`
* **ReDoc:** `http://localhost:8000/redoc`

### 5. Testar A API
Você pode usar a interface **Swagger UI** para testar a funcionalodade de conversão de PDF para CSV. Siga os passos abaixo:

1. Acesse `http://localhost:8000/docs`;
2. Clique me `POST /convert`;
3. Cliquem em `Try it out`;
4. Faça upload de um arquivo PDF contendo tabelas;
5. Selecione oss índices das colunas desejadas (opcional);
6. Clique em `Execute`;
7. Baixe o arquivo CSV resultante.



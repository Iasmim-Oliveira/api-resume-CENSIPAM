# API de Eventos de Fogo

A **API de Eventos de Fogo** é uma API que fornece informações sobre eventos de queimadas no Brasil. Ela permite consultas com base em um intervalo de datas específico, utilizando dados geoespaciais do banco de dados SIG-SIPAM para analisar e contar os eventos de queimadas em várias regiões biogeográficas.

## Funcionalidades

- **Consulta de eventos por bioma:** A API retorna a quantidade de eventos de queimadas para diferentes biomas do Brasil, como Amazônia, Caatinga, Cerrado, Mata Atlântica, Pampa e Pantanal.
- **Filtro de biomas:** A API permite que você filtre os resultados por bioma, proporcionando flexibilidade na análise dos dados.
- **Conexão com o PostgreSQL e PostGIS:** A API utiliza PostgreSQL com a extensão PostGIS para realizar consultas geoespaciais e trabalhar com dados de localização dos eventos de queimadas.

## Endpoints

### `GET /biomas`

Retorna a quantidade de eventos de queimadas por bioma, considerando um intervalo de datas.

#### Parâmetros

- `startDate` (obrigatório): Data de início no formato `YYYY-MM-DD`.
- `endDate` (obrigatório): Data de término no formato `YYYY-MM-DD`.
- `bioma_id` (opcional): ID do bioma para filtrar os resultados. Se não fornecido, a consulta retorna dados de todos os biomas.

#### Exemplo de Requisição

```bash
GET http://127.0.0.1:8000/biomas?startDate=2024-01-01&endDate=2024-12-31&bioma_id=1
```

### Exemplo de resposta

```bash
[
  {
    "bioma": "AMAZÔNIA",
    "quantidade_eventos": 234
  },
  {
    "bioma": "CAATINGA",
    "quantidade_eventos": 120
  }
]
```

## Tecnologias Utilizadas
- FastAPI: Framework web para construir APIs rápidas e modernas.
- SQLAlchemy: ORM (Object Relational Mapper) para interação com o banco de dados PostgreSQL.
- PostGIS: Extensão do PostgreSQL que adiciona suporte a dados geoespaciais.
- Pydantic: Biblioteca para validação de dados e criação de modelos de dados.
- Uvicorn: Servidor ASGI para rodar a API.

## Como Rodar a API Localmente
1. Clone o repositório:
```bash
git clone https://github.com/seu_usuario/nome-do-repositorio.git
```

2. Instale as dependências: Navegue até a pasta do projeto e instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o banco de dados PostgreSQL com a extensão PostGIS.

4. Execute a API: Com o ambiente configurado, inicie a API localmente com o seguinte comando:

```bash
uvicorn app.main:app --reload
```

5. Acesse a API: Acesse a API no endereço http://127.0.0.1:8000.

## Estrutura do Projeto
- app/: Contém o código da API.
- main.py: Arquivo principal para iniciar a aplicação.
- core/: Contém arquivos de configuração e conexão com o banco de dados.
- models/: Modelos de dados e consultas ao banco de dados.
- schemas/: Definições dos modelos de entrada e saída de dados utilizando Pydantic.
- routers/: Definições dos endpoints da API.
  
## Como Contribuir
- Faça um fork deste repositório.
- Crie uma nova branch (git checkout -b feature/nome-da-funcionalidade).
- Realize as alterações e adicione os arquivos modificados (git add .).
- Faça um commit com a descrição das suas alterações (git commit -m "Descrição das alterações").
- Envie as alterações para o seu repositório forkado (git push origin feature/nome-da-funcionalidade).
- Abra um pull request para o repositório principal.
  
## Licença
Este projeto está licenciado sob a MIT License.

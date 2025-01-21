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

### Exemplo de Resposta

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

### `GET /ranking-severidade`

Retorna os 10 eventos mais severos ocorridos no dia anterior, trazendo: ID do evento, severidade calculada, duração (em dias) do evento, área do evento, estado e cidade.
Esse endpoint não requer parâmetros, pois todas as condições de consultas são imutáveis.

#### Exemplo de Resposta
```bash
[
  {
    "id_evento": 0,
    "severidade": 0,
    "duracao_evento": 0,
    "area_evento": 0,
    "uf": "string",
    "cidade": "string"
  }
]
```

### `GET /acumulado-br`
Retorna todos os evntos ocorridos no ano atual. Esse endpoint não requer parâmetros.

#### Exemplo de Resposta
```bash
[
  {
    "numero_eventos": 0,
    "data": "string"
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

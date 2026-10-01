# 🐾 API de Pessoas e Pets

API REST desenvolvida em **Python e Flask**, utilizando uma arquitetura organizada em camadas para separar responsabilidades entre rotas, controllers, views e repositories.

O projeto foi desenvolvido com foco em **boas práticas de organização de código**, tratamento de erros e integração com banco de dados utilizando **SQLAlchemy**.

---

## 🚀 Sobre o projeto

Esta aplicação permite trabalhar com informações relacionadas a **pessoas e seus pets**, disponibilizando endpoints para criação, consulta e gerenciamento dos dados.

O projeto utiliza uma estrutura baseada em **MVC (Model-View-Controller)**, juntamente com o padrão de **Repository**, buscando manter cada parte da aplicação responsável por uma função específica.

### Principais conceitos utilizados

* API REST
* Flask
* Python
* MVC
* Repository Pattern
* SQLAlchemy
* SQLite
* Blueprint
* Dependency Injection
* Tratamento de exceções
* Testes automatizados
* Flask-CORS

---

## 🛠️ Tecnologias

| Tecnologia | Utilização                       |
| ---------- | -------------------------------- |
| Python     | Linguagem principal              |
| Flask      | Framework web                    |
| SQLAlchemy | Comunicação com o banco de dados |
| SQLite     | Banco de dados                   |
| Pytest     | Testes automatizados             |
| Flask-CORS | Configuração de CORS             |
| Git        | Controle de versão               |

---


## 🏗️ Arquitetura

O projeto utiliza uma arquitetura baseada na separação de responsabilidades.

### Route

Responsável por receber a requisição HTTP e encaminhá-la para a camada responsável pelo processamento.

Exemplo:

```text
HTTP Request
     ↓
   Route
```

---

### Composer

Responsável por montar as dependências necessárias para executar uma operação.

```text
Composer
   ↓
Repository
   ↓
Controller
   ↓
View
```

Isso evita que as rotas precisem conhecer diretamente a implementação das outras camadas.

---

### Controller

Responsável pela regra de negócio da operação.

Exemplos:

```text
PersonCreatorController
PersonFinderController
PetsDeleteController
```

---

### View

Responsável por transformar o resultado do controller em uma estrutura de resposta HTTP.

```text
Controller
    ↓
View
    ↓
HttpResponse
```

---

### Repository

Responsável pela comunicação com o banco de dados.

A camada de repository concentra operações como:

* Buscar registros
* Inserir registros
* Remover registros
* Executar consultas SQL

---

## 🔄 Fluxo de uma requisição

Exemplo de uma consulta de pessoa:

```text
Cliente
  │
  │ GET /people/{person_id}
  ▼
Route
  │
  ▼
Composer
  │
  ▼
View
  │
  ▼
Controller
  │
  ▼
Repository
  │
  ▼
Database
  │
  ▼
Repository
  │
  ▼
Controller
  │
  ▼
View
  │
  ▼
HttpResponse
  │
  ▼
JSON Response
```

---

## 🔗 Endpoints

### 👤 Criar pessoa

```http
POST /people
```

Exemplo de requisição:

```json
{
    "name": "João",
    "age": 25
}
```

---

### 🔎 Buscar pessoa

```http
GET /people/<person_id>
```

Exemplo:

```http
GET /people/1
```

---

### 🐾 Listar pets

```http
GET /pets
```

---

### 🗑️ Remover pet

```http
DELETE /pets/<name>
```

---

## ⚠️ Tratamento de erros

O projeto possui uma camada específica para tratamento de erros HTTP.

As exceções são capturadas nas rotas e encaminhadas para:

```text
handle_errors()
```

Exemplo de resposta de erro:

```json
{
    "errors": [
        {
            "title": "Bad Request",
            "detail": "Mensagem do erro"
        }
    ]
}
```

Esse padrão permite manter as respostas de erro da API organizadas e padronizadas.

---

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para persistência dos dados e **SQLAlchemy** para realizar a comunicação com o banco.

A conexão é centralizada através do:

```text
db_connection_handler
```

Isso permite que os repositories utilizem a mesma estrutura de conexão sem precisar gerenciar individualmente a conexão com o banco.

---

## 🌐 CORS

O projeto utiliza `Flask-CORS` para permitir requisições de diferentes origens.

```python
from flask_cors import CORS

CORS(app)
```

Isso facilita a integração futura da API com aplicações frontend.

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd projeto-mvc
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o projeto

Com o ambiente virtual ativado:

```bash
flask --app src.main.server run
```

Ou utilize o comando definido no seu projeto para iniciar a aplicação.

A API estará disponível, normalmente, em:

```text
http://127.0.0.1:5000
```

---

## 🧪 Testes

Os testes são executados utilizando **Pytest**.

```bash
pytest
```

Para executar com mais detalhes:

```bash
pytest -v
```

---

## 📌 Objetivos de aprendizado

Este projeto foi desenvolvido como parte do meu processo de aprendizado em desenvolvimento **Back-end com Python**.

Durante o desenvolvimento, foram praticados conceitos como:

* Desenvolvimento de APIs REST
* Arquitetura MVC
* Repository Pattern
* Separação de responsabilidades
* Injeção de dependências
* Flask Blueprints
* SQLAlchemy
* Banco de dados
* Tratamento de exceções
* Testes automatizados
* Organização de projetos Python
* Git e GitHub

---


## 👨‍💻 Autor

**João Vitor Abreu**

Desenvolvedor Back-end com foco em **Python e Go**, interessado em desenvolvimento de APIs, bancos de dados e arquitetura de software.

### Tecnologias

```text
Python
Go
Flask
Gin
REST API
SQL
PostgreSQL
SQLite
MongoDB
Docker
Git
GitHub
```

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório.

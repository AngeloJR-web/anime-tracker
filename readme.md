# ⛩️ OtakuTracker Pro

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg?logo=sqlite)
![Pytest](https://img.shields.io/badge/pytest-passing-success.svg?logo=pytest)
![Architecture](https://img.shields.io/badge/Architecture-DDD-purple.svg)

OtakuTracker Pro é uma aplicação Full-Stack de gerenciamento de animes construída com foco em **Clean Architecture** e **Domain-Driven Design (DDD)** simplificado. 

O projeto demonstra a aplicação prática de padrões de engenharia de software, separando regras de negócio da camada de infraestrutura, além de utilizar chamadas assíncronas de alta performance e persistência de dados relacional.

---

## 🚀 Funcionalidades Principais

* **Busca Assíncrona:** Integração não-bloqueante com a Jikan API (MyAnimeList oficial) usando `aiohttp`.
* **Persistência Confiável:** Banco de dados SQLite gerenciado via ORM (SQLAlchemy).
* **Gestão de Estado:** Regras de negócio estritas garantem que o status do anime (ex: `WATCHING`, `COMPLETED`) mude automaticamente baseado no progresso.
* **Interface Cinemática:** Frontend responsivo com tema Dark Mode moderno, consumindo a própria API via Vanilla JavaScript (Fetch API).
* **Test-Driven:** Cobertura de testes unitários para o Core Domain garantindo estabilidade das regras de negócio.

---

## 🛠️ Stack Tecnológica

**Backend:**
* Python 3.10+
* FastAPI & Uvicorn (Web API e Servidor ASGI)
* SQLAlchemy (ORM para Banco de Dados)
* Aiohttp (Client HTTP Assíncrono)

**Frontend:**
* HTML5, CSS3 (Custom Properties, Flexbox/Grid)
* JavaScript (ES6+, Async/Await)
* Jinja2 (Templating)

**Qualidade de Código:**
* Pytest (Testes Unitários)
* Flake8 (Linting)

---

## 🏗️ Arquitetura do Projeto

O código está estruturado para maximizar a coesão e minimizar o acoplamento:

```text
anime-tracker/
├── src/
│   ├── domain/             # Regras de negócio puras (Entities, Value Objects)
│   │   └── media.py
│   └── infrastructure/     # Implementações externas (DB, APIs externas)
│       ├── database.py     # Setup do SQLAlchemy
│       └── jikan_api.py    # Client da API do MyAnimeList
├── tests/                  # Suíte de testes automatizados
│   └── test_media.py
├── templates/              # Camada de apresentação (UI)
│   └── index.html
├── web_app.py              # Entrypoint do FastAPI (Controllers/Rotas)
└── requirements.txt        # Dependências

Como Executar Localmente
Siga as instruções abaixo para rodar o projeto na sua máquina.
1. Clonar o repositório
git clone [https://github.com/seu-usuario/anime-tracker.git](https://github.com/seu-usuario/anime-tracker.git)
cd anime-tracker
2. Criar e ativar o ambiente virtual (Recomendado)
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
4. Iniciar o Servidor
python web_app.py
O servidor estará rodando em http://127.0.0.1:8000. O banco de dados otakutracker.db será gerado automaticamente no primeiro acesso.
Rodando os Testes
Para garantir que a lógica de domínio está funcionando corretamente, execute a suíte do Pytest: pytest tests/

Próximos Passos (Roadmap)
[ ] Implementar suporte completo a Mangás.

[ ] Orquestração com Docker (Docker Compose para App + PostgreSQL).

[ ] Autenticação de usuários com JWT.

Desenvolvido por Angelo De Oliveira Junior.

# wsBackend-Fabrica26.1

🎬 Catálogo de Filmes com Django

Projeto desenvolvido para O desafio  Fábrica de Software, utilizando Django com CRUD completo, entidades relacionadas e consumo da API OMDb.

🚀 Funcionalidades

CRUD de filmes
CRUD de categorias
Relacionamento entre entidades
Consumo da API OMDb
Autenticação por token

🧰 Tecnologias

Python
Django
Django REST Framework
MySQL
Docker

▶️ Como executar
git clone <wsBackend-Fabrica26.1>
cd wsBackend-Fabrica26.1-MAIN
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

Acesse: http://localhost:8000

🔐 Autenticação

Gerar token:

POST /api/token/

Usar no header:

Authorization: Token: kennedy
🔄 Endpoints
Filmes
GET /api/filmes/
POST /api/filmes/
PUT /api/filmes/{id}/
DELETE /api/filmes/{id}/
Categorias
GET /api/categorias/
POST /api/categorias/
PUT /api/categorias/{id}/
DELETE /api/categorias/{id}/

senha: "23a260d9"  OMDb

🎬 Sugestões de pesquisas para testar a API

Inception
Interstellar
The Godfather
Titanic
Avatar
Gladiator
The Dark Knight
Parasite
Joker
Forrest Gump

👨‍💻 Autor

Kennedy Oliveira        

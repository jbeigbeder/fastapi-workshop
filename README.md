# Workshop Python: FastAPI

## TLDR;

A very simple REST API build with [FastAPI](https://fastapi.tiangolo.com) and [SQLAlchemy](https://www.sqlalchemy.org).

## Architecture

* python 3.9+
* [FastAPI](https://fastapi.tiangolo.com): framework web destiné à construire des API Rest
* [SQLAlchemy](https://www.sqlalchemy.org): framework SQL et ORM
* SQLite: base de données locale pour simplifier les développements

L'architecture logicielle est simplifiée. Pas de couche métier, les endpoints Rest appellent la base de données par
l'intermédiaire de repositories.

Les endpoints ont connaissance des _schemas_ (objet de type DTO définissant les payloads des requêtes http). 
Ils les transforment (mapping) en _models_  (objets définissant le mapping objet/relationel).

Les repositories ont connaissance des _models_.

## Outillage

* [Poetry](https://python-poetry.org): gestion des dépendances et build
* [Yapf](https://pypi.org/project/yapf/): formatage code
* [flake8](https://flake8.pycqa.org/en/latest/): linter, style

## Commencer les développements

* Python est installé sur le poste de dév
* [Poetry](https://python-poetry.org) est installé comme outil de gestion de dépendances et de build.
* Lancer la commande`poetry install` pour récupérer les dépendances et créer l'environnement virtuel
* Activer l'environnement virtuel
    * soit Configurer correctement l'IDE
    * soit lancer la commande `poetry shell` dans un terminal
    * soit lancer la commande `python -venv .venv` dans un terminal
* Démarrer l'application: `uvicorn fastapi_workshop.main:app --reload`
* Tester l'API: `http://127.0.0.1:8000/docs`
* Editer le code, sauver, tester, ...
* Formatage du code:
  * utiliser l'IDE après l'avoir configurer correctement
  * ou lancer la commande `yapf.exe --in-place --recursive .\fastapi_workshop\`

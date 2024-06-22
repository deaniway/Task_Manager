### Hexlet tests and linter status:

[![Actions Status](https://github.com/deaniway/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/deaniway/python-project-52/actions)

### CodeClimate :

[![Maintainability](https://api.codeclimate.com/v1/badges/bb4dbe222e082f04cd20/maintainability)](https://codeclimate.com/github/deaniway/python-project-52/maintainability)

### Test coverage:

[![Test Coverage](https://api.codeclimate.com/v1/badges/bb4dbe222e082f04cd20/test_coverage)](https://codeclimate.com/github/deaniway/python-project-52/test_coverage)

# Task Manager

This advanced TASK MANAGER system is designed to optimize your workflow as much as possible.
It offers a comprehensive solution for organizing, distributing and monitoring tasks.
Whether you work independently or manage a team, our dispatcher tasks will be your go-to for efficiency and
productivity.

## [YOU CAN READ MORE HERE !](https://python-project-52-fh7q.onrender.com)

#### Minimum Requirements:

- [x] Python
- [x] Poetry
- [x] Django
- [x] PostgreSQL
- [x] Docker

### This is  use next tools:

|       Tools       | Version |
|:-----------------:|:-------:|
|      python       |  3.11   |
|      poetry       |  1.6.1  |
|     gunicorn      | 22.0.0  |
|      flake8       |  6.1.0  |
|   python-dotenv   |  1.0.1  |
|  psycopg2-binary  |  2.9.9  |
|        bs4        |  0.0.2  |
|      Docker       | 23.0.3  |
|    PostgreSQL     |  16.3   |
|      Django       |  5.0.6  |
| django-bootstrap5 |  24.2   |
|   django-filte    |  24.2   |
|      rollbar      | 0.16.3  |
|     coverage      |  7.5.3  |

### To get started, you need to perform the following operations:

| Step |                                   Instruction                                   |
|:----:|:-------------------------------------------------------------------------------:|
|  1   | Clone he repository to your PC:<br/>`github.com/deaniway/python-project-52.git` |
|  2   |                   Go to repository<br/>`cd python-project-52`                   |
|  3   |         Installing the application on your computer<br/>`make install`          | 
|  4   |  Run the command to create tables<br/>`make makemigrations` /  `make migrate`   | 
|  5   |               To start the Django server, use the<br/>`make dev`                |

### *You must have:*

- [Poetry](https://python-poetry.org)

- [Django](https://www.djangoproject.com/)

- [PostgreSQL](https://www.postgresql.org/)

- [Docker](https://www.docker.com/)

## How to deploy a database?

#### Create .env file in sources root and fill it (example)

```dotenv

DATABASE_URL=postgresql://pguser:pgpass@localhost:5434/pgdb

```

#### Up postgres DB (Docker for example):

```sh
make dev-db
```

#### Run local server:

```shell
make dev
```

### Contributing

How can I help develop a project? Submit a pull request :)

## Project team

- Denis Davydov (https://t.me/deway0) — Python developer
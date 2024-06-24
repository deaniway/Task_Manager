PORT ?= 8000

install:
	poetry install

dev:
	 poetry run ./manage.py runserver $(PORT)

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

lint:
	poetry run flake8 _project_

test:
	poetry run ./manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml

makemigrations:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate

dev-db:
	docker-compose up -d
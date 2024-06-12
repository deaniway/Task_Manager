PORT ?= 8000

install:
	poetry install

dev:
	 poetry run ./manage.py runserver $(PORT)

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

lint:
	poetry run flake8 task_manager

test:
	poetry run ./manage.py test

makemigrations:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate
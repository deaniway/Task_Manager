PORT ?= 8000

install:
	poetry install

dev:
	 poetry run ./manage.py runserver $(PORT)

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application
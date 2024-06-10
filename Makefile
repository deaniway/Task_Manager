PORT ?= 8000

install:
	poetry install

dev:
	 poetry run ./manage.py runserver $(PORT)


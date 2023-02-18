# инструкция по работе с файлом "Makefile" – https://bytes.usc.edu/cs104/wiki/makefile/
.DEFAULT_GOAL := all
# обновление сборки Docker-контейнера
build:
	docker compose build

# генерация документации
docs-html:
	docker compose run --workdir /docs app /bin/bash -c "make html"

# запуск форматирования кода
format:
	docker compose run --workdir / app /bin/bash -c "black src docs/source/*.py; isort --profile black src/*.py docs/source/*.py"

# запуск статического анализа кода (выявление ошибок типов и форматирования кода)
lint:
	docker compose run --workdir / app /bin/bash -c "pylint --load-plugins pylint_django --load-plugins pylint_django.checkers.migrations --django-settings-module=portfolio.settings src; flake8 src; mypy src; black --check src"

db:
	docker compose up -d db

migrate:
	docker compose run app python manage.py migrate

makemigrations:
	docker compose run app python manage.py makemigrations

create_super_user:
	docker compose run app python manage.py createsuperuser

up:
	docker compose up --build
# запуск автоматических тестов
test:
	docker compose run app ./manage.py test

# запуск всех функций поддержки качества кода
all: format lint test

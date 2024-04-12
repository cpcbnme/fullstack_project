# Makefile

RUN_SERVER=python manage.py runserver
MAKE_MIGRATIONS=python manage.py makemigrations
MIGRATE=python manage.py migrate
FILLSTOCK=python manage.py beerseed

.PHONY: runserver makemigrations migrate createsuperuser

default: runserver

runserver:
	$(RUN_SERVER)

makemigrations:
	$(MAKE_MIGRATIONS)

migrate:
	$(MIGRATE)

fillstock:
	python manage.py beerseed

# Makefile

RUN_SERVER=python3 manage.py runserver
MAKE_MIGRATIONS=python3 manage.py makemigrations
MIGRATE=python3 manage.py migrate
FILLSTOCK=python3 manage.py beerseed

.PHONY: runserver makemigrations migrate createsuperuser

default: runserver

runserver:
	$(RUN_SERVER)

makemigrations:
	$(MAKE_MIGRATIONS)

migrate:
	$(MIGRATE)

fillstock:
	$(FILLSTOCK)

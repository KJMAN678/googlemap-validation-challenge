#!/bin/sh
uv run manage.py migrate
uv run manage.py collectstatic --noinput
uv run manage.py createsuperuser --noinput || true
uv run python manage.py sample_command 3
# uv run manage.py runserver 0.0.0.0:8000
uv run gunicorn config.wsgi:application --bind 0.0.0.0:8000

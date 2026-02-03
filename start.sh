#!/usr/bin/env bash
set -e

# Collect static (safe to run on start as well)
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

# Start app
exec gunicorn task10_project.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers ${WEB_CONCURRENCY:-2} --timeout 120

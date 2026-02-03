#!/usr/bin/env bash
set -e

echo "Collecting static..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Seeding demo data..."
python manage.py seed_demo

echo "Starting app..."
exec gunicorn task10_project.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers ${WEB_CONCURRENCY:-2} --timeout 120

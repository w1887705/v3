#!/usr/bin/env bash
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Optional: seed the demo user (safe to run multiple times if the command handles duplicates)
python manage.py seed_demo

echo "Running Seed Script..."
python manage.py seed_demo --traceback
echo "Seed Script Finished."
#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
ls -la
python manage.py collectstatic --no-input
python manage.py makemigrations common errors api product
python manage.py migrate
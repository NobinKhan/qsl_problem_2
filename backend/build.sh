#!/usr/bin/env bash
# exit on error
set -o errexit


ls -la settings/django/


poetry install
python manage.py collectstatic --no-input
# python manage.py makemigrations common errors api product
# python manage.py migrate


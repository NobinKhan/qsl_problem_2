#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

env = environ.Env()
DOT_ENV_DIR = environ.Path(__file__) - 2
print(DOT_ENV_DIR)
if 'RENDER' not in os.environ:
    env.read_env(os.path.join(DOT_ENV_DIR, ".env"))
print(DOT_ENV_DIR)


def main():
    if env('ENVIRONMENT') == 'PRODUCTION':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.production')
    elif env('ENVIRONMENT') == 'local':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.local')
    elif 'RENDER' in os.environ:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.render')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

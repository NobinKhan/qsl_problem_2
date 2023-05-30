#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


if 'RENDER' in os.environ:
    load_dotenv(".env")
else:
    load_dotenv("../.env")




def main():
    if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.production')
    elif os.environ.get('ENVIRONMENT') == 'local':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.local')
    elif os.environ.get('ENVIRONMENT') == 'render':
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

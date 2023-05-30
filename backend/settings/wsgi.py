import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv


if 'RENDER' in os.environ:
    load_dotenv("../.env")
else:
    load_dotenv("../../.env")


if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.production')
elif os.environ.get('ENVIRONMENT') == 'local':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.local')
elif os.environ.get('ENVIRONMENT') == 'render':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.render')

application = get_wsgi_application()

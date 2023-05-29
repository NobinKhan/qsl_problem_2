import os

from django.core.asgi import get_asgi_application
import environ

env = environ.Env()
BASE_DIR = environ.Path(__file__) - 3

if env('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.production')
elif env('ENVIRONMENT') == 'local':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.local')

application = get_asgi_application()

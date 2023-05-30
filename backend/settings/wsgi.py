import os

from django.core.wsgi import get_wsgi_application

import environ

env = environ.Env()
DOT_ENV_DIR = environ.Path(__file__) - 3
if 'RENDER' not in os.environ:
    env.read_env(os.path.join(DOT_ENV_DIR, ".env"))

if env('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.production')
elif env('ENVIRONMENT') == 'local':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.local')
elif 'RENDER' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.render')

application = get_wsgi_application()

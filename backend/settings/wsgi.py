import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv


if 'RENDER' in os.environ:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    upper_parent_dir = os.path.dirname(current_dir)
    dotenv_path = os.path.join(upper_parent_dir, '.env')
    load_dotenv(dotenv_path)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    upper_parent_dir = os.path.dirname(os.path.dirname(current_dir))
    dotenv_path = os.path.join(upper_parent_dir, '.env')
    load_dotenv(dotenv_path)


if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.production')
elif os.environ.get('ENVIRONMENT') == 'local':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.local')
elif os.environ.get('ENVIRONMENT') == 'render':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings.django.render')

application = get_wsgi_application()

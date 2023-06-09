import os
from settings.env import BASE_DIR


# Security key, debug and host config
SECRET_KEY = os.environ.get('SECRET_KEY', default="django-insecure-!5")
DEBUG = os.environ.get("DEBUG", default=True)
ALLOWED_HOSTS = ["*"]


# Application definition
FIRST_PRIORITY_APPS = [

]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
]

LOCAL_APPS = [
    "apps.common.apps.CommonConfig",
    'apps.integrations.apps.IntegrationsConfig',
    "apps.api.apps.ApiConfig",
    "apps.errors.apps.ErrorsConfig",
    "apps.product.apps.ProductConfig",
]

INSTALLED_APPS = [
    *FIRST_PRIORITY_APPS,
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]


# Middleware config
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware", # Cors headers middleware
    "whitenoise.middleware.WhiteNoiseMiddleware", #whitenoise middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Template Configs
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database Configs
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    },
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True


# redis cache
CACHE_TTL = 60 * 1500
CACHES = {
    "default": {
        "BACKEND": os.environ.get('REDIS_BACKEND'),
        "LOCATION": os.environ.get('REDIS_LOCATION'),
    }
}
SESSION_ENGINE = os.environ.get('SESSION_ENGINE')
SESSION_CACHE_ALIAS = os.environ.get('SESSION_CACHE_ALIAS')

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Project wide configs
ROOT_URLCONF = "settings.urls"
WSGI_APPLICATION = "settings.wsgi.application"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APP_DOMAIN = os.environ.get("APP_DOMAIN", default="http://localhost:8000")
APPEND_SLASH=True

# Custom Auth Config
# AUTH_USER_MODEL = 'users.User'


# Internationalization
USE_TZ = True
USE_I18N = True
USE_L10N = True
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"


# media files config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Email setup
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025



# Import Other Settings
from settings.others.drf import *
from settings.others.cors import *  # noqa
from settings.others.sessions import *  # noqa
from settings.others.sentry import *  # noqa
from settings.others.files_and_storages import *  # noqa


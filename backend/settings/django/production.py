from .base import *  # noqa

DEBUG = os.environ.get("DJANGO_DEBUG", default=False)

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS =os.environ.get("ALLOWED_HOSTS", default=[])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST =os.environ.get("CORS_ORIGIN_WHITELIST", default=[])

SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", default=True)

# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", default=True)
# https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = os.environ.get("SECURE_CONTENT_TYPE_NOSNIFF", default=True)

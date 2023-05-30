import os

"""
Do read:

    1. https://docs.djangoproject.com/en/3.1/ref/settings/#sessions
    2. https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
"""
SESSION_COOKIE_AGE = int(os.environ.get("SESSION_COOKIE_AGE", default=1209600))  # Default - 2 weeks in seconds
SESSION_COOKIE_HTTPONLY = bool(os.environ.get("SESSION_COOKIE_HTTPONLY", default=True))
SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME", default="sessionid")
SESSION_COOKIE_SAMESITE = os.environ.get("SESSION_COOKIE_SAMESITE", default="Lax")
SESSION_COOKIE_SECURE = bool(os.environ.get("SESSION_COOKIE_SECURE", default=False))

CSRF_USE_SESSIONS = bool(os.environ.get("CSRF_USE_SESSIONS", default=True))

from .settings import *
from .settings import BASE_DIR

SECRET_KEY = 'test'
ENV = 'test'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}



from .settings import *

DEBUG = False
ENV = 'production'
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

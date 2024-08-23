from .settings import *

DEBUG = False
ENV = 'production'
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['www.uz']

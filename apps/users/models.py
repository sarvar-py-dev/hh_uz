from django.contrib.auth.models import AbstractUser
from django.db.models import Model

from shared.django.models import CreatedBaseModel, SlugBaseModel


class User(AbstractUser):
    pass


class Spams(Model):
    pass


class Favourites(Model):
    pass

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, FloatField, ImageField, BooleanField, TextField, CASCADE
from django_ckeditor_5.fields import CKEditor5Field
from mptt.fields import TreeForeignKey

from shared.django.models import CreatedBaseModel, SlugBaseModel


class Category(SlugBaseModel):
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class Company(CreatedBaseModel):
    title = CharField(max_length=255)
    info = CKEditor5Field()
    area_of_activity = CharField(max_length=255)
    website = TextField()
    longitude = FloatField()
    latitude = FloatField()
    is_verified = BooleanField(default=False)
    image = ImageField(upload_to='company/image')


class Vacancy(CreatedBaseModel):
    pass


class Subscription(Model):
    pass


class Key(Model):
    pass

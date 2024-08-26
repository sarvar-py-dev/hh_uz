from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DateTimeField, SlugField
from django.utils.text import slugify


class CreatedBaseModel(Model):
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'

        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True

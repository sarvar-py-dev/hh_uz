import factory
from django.contrib.auth.hashers import make_password

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_superuser = factory.Faker('boolean')
    email = factory.Faker('email')

    # password = factory.LazyAttribute(lambda self: make_password(self.password_))

    class Meta:
        model = User

    class Params:
        password_ = factory.Faker('password')

    @factory.lazy_attribute
    def password(self):
        return make_password(self.password_)

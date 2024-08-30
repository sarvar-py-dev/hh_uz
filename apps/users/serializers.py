import re
from random import randint
from django.core.cache import cache

from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import validate_email
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, PasswordField, TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.tasks import send_verification_to_email


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'email', 'username'


class SendCodeSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["password"] = PasswordField(required=False)
        self.fields["username"] = CharField(max_length=25, default='Phone or Email', help_text='Phone or Email')

    def validate_username(self, value):
        # value - email   phone
        code = randint(100_000, 999_999)
        if '@' in value:
            try:
                validate_email(value)
            except DjangoValidationError as e:
                raise ValidationError('Email xato!')
            else:
                send_verification_to_email.delay(value, code)
                print('pochtaga yuborildi')
        else:
            value = re.sub(r'[^\d]', '', value)

            if not (len(value) == 12 and value.startswith('998')):
                raise ValidationError('Phone number togri emas!')
            print(f'Phone: {value}, {code=}')

        cache.set(value, code, timeout=120)
        return value

    def validate(self, attrs):
        if attrs.get('password') is not None:
            self.user = authenticate(self.context['request'], **attrs)
            if not self.user:
                raise ValidationError('Username or password incorrect!')

            refresh = self.get_token(self.user)

            attrs = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'data': UserModelSerializer(self.user).data
            }

        return attrs


class VerifyCodeSerializer(Serializer):
    username = CharField(max_length=255)
    code = IntegerField()

    def validate(self, attrs):
        username = attrs.get('username')
        code = attrs.get('code')

        if '@' not in username:
            username = re.sub(r'[^\d]', '', username)
        cache_code = cache.get(username)

        if not cache_code:
            raise ValidationError('Code not found or timed out')

        if code != cache_code:
            raise ValidationError('Code is invalid')
        user, created = User.objects.get_or_create(username=username)
        login(self.context['request'], user)
        refresh = RefreshToken.for_user(user)

        attrs = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'data': UserModelSerializer(user).data
        }
        return attrs

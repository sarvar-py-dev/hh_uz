import re
from random import randint

from django.contrib.auth.models import update_last_login
from django.core.cache import cache
from django.core.exceptions import ValidationError as DjangoValidationError

from django.contrib.auth import authenticate, get_user_model
from django.core.validators import EmailValidator, validate_email
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField, EmailField
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'email', 'username'


class SendCodeSerializer(TokenObtainPairSerializer):
    username = CharField(max_length=25, default='', help_text='Nomer yoki Email')
    password = CharField(max_length=255, required=False)

    def validate_username(self, value):
        # value - email   phone
        if '@' in value:
            try:
                validate_email(value)
            except DjangoValidationError as e:
                raise ValidationError('Email xato!')
        else:
            phone = re.sub(r'[^\d]', '', value)

            if not (len(phone) == 12 and phone.startswith('998')):
                raise ValidationError('Phone number togri emas!')

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
    code = IntegerField()

    def validate_code(self, value):
        return
from random import randint

from django.core.cache import cache
from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers import SendCodeSerializer, VerifyCodeSerializer
from users.tasks import send_verification_to_email


class SendCodeAPIView(GenericAPIView):
    serializer_class = SendCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if hasattr(serializer, 'user') and serializer.user:
            return Response(serializer.validated_data)

        username = serializer.data['username']
        code = randint(100_000, 999_999)
        cache.set(username, code, timeout=120)
        if '@' in username:
            send_verification_to_email.delay(username, code)
            print('pochtaga yuborildi')
        else:
            print(f'Phone: {username}, {code=}')
        return Response({'msg': f"{username} ga kod yuborildi"})


class VerifyCodeAPIView(GenericAPIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return Response({'ok': 'ok'})

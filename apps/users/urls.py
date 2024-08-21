from django.urls import path
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users import views

urlpatterns = [
    path('auth/send-code', views.SendCodeAPIView.as_view()),
    path('auth/verify-code', views.VerifyCodeAPIView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]

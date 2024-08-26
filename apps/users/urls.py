from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users import views

urlpatterns = [
    path('auth/send-code', views.SendCodeAPIView.as_view(), name='send_code'),
    path('auth/verify-code', views.VerifyCodeAPIView.as_view(), name='verify_code'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('users', views.UserListAPIView.as_view(), name='user-list'),
]

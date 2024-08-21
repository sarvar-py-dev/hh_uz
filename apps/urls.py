from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('resume/', include('resume.urls')),
    path('vacancy/', include('vacancy.urls')),
]

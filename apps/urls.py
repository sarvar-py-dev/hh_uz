from django.urls import path, include

urlpatterns = [
    path('users/', include(('users.urls', 'users'), 'users')),
    path('resume/', include(('resume.urls', 'resume'), 'resume')),
    path('vacancy/', include(('vacancy.urls', 'vacancy'), 'vacancy')),
]

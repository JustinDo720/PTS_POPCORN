from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # This will take care of logging in and out
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # This will take care of logging in and out
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('user_profile/<int:profile_id>/', views.user_profile, name='user_profile'),
    path('edit_user_profile/<int:profile_id>', views.edit_user_profile, name='edit_user_profile'),
]
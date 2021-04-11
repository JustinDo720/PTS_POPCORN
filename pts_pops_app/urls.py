from . import views
from django.urls import path

app_name = 'pts_pops_app'

urlpatterns = [
    path('', views.index, name='index')
]
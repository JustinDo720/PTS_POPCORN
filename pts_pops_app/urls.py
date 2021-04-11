from . import views
from django.urls import path

app_name = 'pts_pops_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('community', views.community_page, name='community'),
]
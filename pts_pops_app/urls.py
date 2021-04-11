from . import views
from django.urls import path

app_name = 'pts_pops_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('community', views.community_page, name='community_page'),
    path('community_post', views.community_post, name='community_post')
]
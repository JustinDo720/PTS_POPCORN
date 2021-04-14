from . import views
from django.urls import path

app_name = 'pts_pops_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('community/', views.community_page, name='community_page'),
    path('community_post', views.community_post, name='community_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('remove_post/<int:post_id>/', views.remove_post, name='remove_post'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
]
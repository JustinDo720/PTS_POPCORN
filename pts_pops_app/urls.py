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
    path('view_full_post/<int:post_id>', views.view_full_post, name='view_full_post'),
    path('admin_add_question/', views.admin_add_question, name='admin_add_question'),
    path('admin_add_choice/', views.admin_add_choice, name='admin_add_choice'),
    path('admin_view_choice/<int:question_id>', views.admin_view_choice, name='admin_view_choice'),
    path('vote_homepage/', views.vote_homepage, name='vote_homepage'),
    path('show_question/<int:question_id>', views.show_question, name='show_question'),
    path('voteMechanism/<int:question_id>', views.voteMechanism, name='voteMechanism'),
    path('results/<int:question_id>', views.results, name='results'),
    path('results_homepage/', views.results_homepage, name='results_homepage')
]
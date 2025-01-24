from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='base'),  # Home page
    path('players', views.player_list, name='player-list'),
    path('player/<int:id>', views.player_detail, name='player-detail'),
    path('player/add', views.player_create, name='player-create'),
    path('player/<int:id>/change', views.player_update, name='player-update'),
    path('player/<int:id>/delete', views.player_delete, name='player-delete'),
    path('coach', views.coach_list, name='coach-list'),
    path('coach/<int:id>', views.coach_detail, name='coach-detail'),
    path('coach/add', views.coach_create, name='coach-create'),
    path('coach/<int:id>/change', views.coach_update, name='coach-update'),
    path('coach/<int:id>/delete', views.coach_delete, name='coach-delete'),
    path('assistant', views.assistant_list, name='assistant-list'),  # Corrected views
    path('assistant/<int:id>', views.assistant_detail, name='assistant-detail'),
    path('assistant/add', views.assistant_create, name='assistant-create'),
    path('assistant/<int:id>/change', views.assistant_update, name='assistant-update'),
    path('assistant/<int:id>/delete', views.assistant_delete, name='assistant-delete'),
    path('team', views.team_list, name='team-list'),  # Corrected views
    path('team/<int:id>', views.team_detail, name='team-detail'),
    path('team/add', views.team_create, name='team-create'),
    path('team/<int:id>/change', views.team_update, name='team-update'),
    path('team/<int:id>/delete', views.team_delete, name='team-delete'),
]


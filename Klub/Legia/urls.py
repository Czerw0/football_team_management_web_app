from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("", views.welcome_view),
    path("players", views.player_list, name='player-list'),
    path("player/<int:id>", views.player_detail, name='player-detail'),
    path("player/add", views.player_create, name='player-create'),
    path("player/<int:id>/change", views.player_update, name='player-update'),
    path("player/<int:id>/delete", views.player_delete, name='player-delete'),
]
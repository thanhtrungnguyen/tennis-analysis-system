from django.urls import path
from . import views

urlpatterns = [
    path('player/list', views.player_list, name='player-list'),
    path('player/register', views.player_register, name='player-register'),
    path('player/update', views.player_update, name='player-update'),
    path('player/delete', views.player_delete, name='player-delete'),
    path('player/get', views.get_player_by_id, name='get-player-by-id'),
]

from django.urls import path
from .views import match_register, match_list, match_update, match_delete, get_match_by_id

urlpatterns = [
    path('match/register', match_register, name='match-register'),
    path('match/list', match_list, name='match-list'),
    path('match/update', match_update, name='match-update'),
    path('match/delete', match_delete, name='match-delete'),
    path('match/get', get_match_by_id, name='get-match-by-id'),
]

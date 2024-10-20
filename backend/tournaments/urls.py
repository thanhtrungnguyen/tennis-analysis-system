from django.urls import path
from .views import (
    tournament_register, tournament_list, tournament_update, tournament_delete, get_tournament_by_id,
    video_segment_register, video_segment_list, video_segment_update, video_segment_delete, get_video_segment_by_id
)

urlpatterns = [
    # Tournament endpoints
    path('tournament/register', tournament_register, name='tournament-register'),
    path('tournament/list', tournament_list, name='tournament-list'),
    path('tournament/update', tournament_update, name='tournament-update'),
    path('tournament/delete', tournament_delete, name='tournament-delete'),
    path('tournament/get', get_tournament_by_id, name='get-tournament-by-id'),

    # VideoSegment endpoints
    path('video_segment/register', video_segment_register, name='video-segment-register'),
    path('video_segment/list', video_segment_list, name='video-segment-list'),
    path('video_segment/update', video_segment_update, name='video-segment-update'),
    path('video_segment/delete', video_segment_delete, name='video-segment-delete'),
    path('video_segment/get', get_video_segment_by_id, name='get-video-segment-by-id'),
]

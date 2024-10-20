from django.urls import path
from .views import video_register, video_list, video_update, video_delete, get_video_by_id

urlpatterns = [
    path('video/register', video_register, name='video-register'),
    path('video/list', video_list, name='video-list'),
    path('video/update', video_update, name='video-update'),
    path('video/delete', video_delete, name='video-delete'),
    path('video/get', get_video_by_id, name='get-video-by-id'),
]

from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# from .modules.player.player_views import PlayerViewSet
# from .modules.match.match_views import MatchViewSet, MatchPlayerViewSet
# from .modules.video.video_views import VideoViewSet
# from .modules.event.event_views import EventViewSet, VideoSegmentViewSet
#
# router = DefaultRouter()
# router.register(r'players', PlayerViewSet)
# router.register(r'matches', MatchViewSet)
# router.register(r'match-players', MatchPlayerViewSet)
# router.register(r'videos', VideoViewSet)
# router.register(r'events', EventViewSet)
# router.register(r'video-segments', VideoSegmentViewSet)

urlpatterns = [
    path('matches/', include('apps.matches.urls')),
]

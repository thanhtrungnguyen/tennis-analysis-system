from django.urls import path, include

urlpatterns = [
    path('player/', include('apps.matches.urls.player_urls')),
    path('matche/', include('apps.matches.urls.match_urls')),
    path('video/', include('apps.matches.urls.video_urls')),
    path('event/', include('apps.matches.urls.event_urls')),
]

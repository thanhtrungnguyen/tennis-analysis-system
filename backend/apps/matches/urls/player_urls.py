from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.matches.modules.player.player_views import PlayerViewSet

router = DefaultRouter()
router.register(r'', PlayerViewSet)

urlpatterns = router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.matches.modules.match.match_views import MatchViewSet, MatchPlayerViewSet

router = DefaultRouter()
router.register(r'', MatchViewSet)
router.register(r'players', MatchPlayerViewSet)

urlpatterns = router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.matches.modules.event.event_views import EventViewSet, VideoSegmentViewSet

router = DefaultRouter()
router.register(r'', EventViewSet)
router.register(r'segments', VideoSegmentViewSet)

urlpatterns = router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.matches.modules.video.video_views import VideoViewSet

router = DefaultRouter()
router.register(r'', VideoViewSet)

urlpatterns = router.urls

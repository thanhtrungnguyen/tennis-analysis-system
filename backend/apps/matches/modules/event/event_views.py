from rest_framework import viewsets
from apps.matches.models.event import Event, VideoSegment
from apps.matches.modules.event.event_serializers import EventSerializer, VideoSegmentSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class VideoSegmentViewSet(viewsets.ModelViewSet):
    queryset = VideoSegment.objects.all()
    serializer_class = VideoSegmentSerializer

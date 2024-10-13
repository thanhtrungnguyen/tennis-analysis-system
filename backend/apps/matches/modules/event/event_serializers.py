from rest_framework import serializers
from apps.matches.models.event import Event, VideoSegment

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class VideoSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSegment
        fields = '__all__'

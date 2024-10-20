from rest_framework import serializers

from events.models import Event


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

from rest_framework import serializers

from events.models import Tournament


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

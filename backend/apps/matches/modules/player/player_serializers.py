from rest_framework import serializers
from apps.matches.models.player import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

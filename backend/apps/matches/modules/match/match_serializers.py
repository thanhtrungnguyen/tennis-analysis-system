from rest_framework import serializers
from apps.matches.models.match import Match, MatchPlayer

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class MatchPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPlayer
        fields = '__all__'

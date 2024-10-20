from rest_framework import serializers
from .models import Match, MatchPlayer
from players.models import Player
from players.serializers import PlayerSerializer  # Assuming you have this serializer for the Player model


class MatchPlayerSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    player_id = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), source='player', write_only=True)

    class Meta:
        model = MatchPlayer
        fields = ['player', 'player_id', 'role']


class MatchSerializer(serializers.ModelSerializer):
    players = MatchPlayerSerializer(source='matchplayer_set', many=True, required=False)

    class Meta:
        model = Match
        fields = ['id', 'tournament_name', 'match_date', 'match_type', 'result', 'players']

    def create(self, validated_data):
        players_data = validated_data.pop('matchplayer_set', [])
        match = Match.objects.create(**validated_data)

        # Create MatchPlayer relationships
        for player_data in players_data:
            player = player_data['player']
            role = player_data['role']
            MatchPlayer.objects.create(match=match, player=player, role=role)

        return match

    def update(self, instance, validated_data):
        players_data = validated_data.pop('matchplayer_set', [])

        # Update match fields
        instance.tournament_name = validated_data.get('tournament_name', instance.tournament_name)
        instance.match_date = validated_data.get('match_date', instance.match_date)
        instance.match_type = validated_data.get('match_type', instance.match_type)
        instance.result = validated_data.get('result', instance.result)
        instance.save()

        # Update players and their roles
        instance.matchplayer_set.all().delete()  # Clear previous players
        for player_data in players_data:
            player = player_data['player']
            role = player_data['role']
            MatchPlayer.objects.create(match=instance, player=player, role=role)

        return instance

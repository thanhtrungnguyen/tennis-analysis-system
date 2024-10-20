from rest_framework import serializers
from tournaments.models import Tournament, VideoSegment
from players.models import Player
from matches.models import Match
from videos.models import Video
from players.serializers import PlayerSerializer
from matches.serializers import MatchSerializer
from videos.serializers import VideoSerializer

class TournamentSerializer(serializers.ModelSerializer):
    match = MatchSerializer(read_only=True)
    match_id = serializers.PrimaryKeyRelatedField(queryset=Match.objects.all(), source='match', write_only=True)
    player = PlayerSerializer(read_only=True, allow_null=True)
    player_id = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), source='player', write_only=True, allow_null=True)

    class Meta:
        model = Tournament
        fields = ['id', 'match', 'match_id', 'event_type', 'player', 'player_id', 'event_time']

    def create(self, validated_data):
        return Tournament.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.match = validated_data.get('match', instance.match)
        instance.event_type = validated_data.get('event_type', instance.event_type)
        instance.player = validated_data.get('player', instance.player)
        instance.event_time = validated_data.get('event_time', instance.event_time)
        instance.save()
        return instance


class VideoSegmentSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)
    video_id = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all(), source='video', write_only=True)
    tournament = TournamentSerializer(read_only=True)
    tournament_id = serializers.PrimaryKeyRelatedField(queryset=Tournament.objects.all(), source='tournament', write_only=True)

    class Meta:
        model = VideoSegment
        fields = ['id', 'video', 'video_id', 'tournament', 'tournament_id', 'start_time', 'end_time']

    def create(self, validated_data):
        return VideoSegment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.video = validated_data.get('video', instance.video)
        instance.tournament = validated_data.get('tournament', instance.tournament)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance

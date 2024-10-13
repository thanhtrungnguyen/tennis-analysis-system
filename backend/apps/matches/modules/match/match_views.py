from rest_framework import viewsets
from apps.matches.models.match import Match, MatchPlayer
from apps.matches.modules.match.match_serializers import MatchSerializer, MatchPlayerSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchPlayerViewSet(viewsets.ModelViewSet):
    queryset = MatchPlayer.objects.all()
    serializer_class = MatchPlayerSerializer

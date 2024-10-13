from rest_framework import viewsets
from apps.matches.models.player import Player
from apps.matches.modules.player.player_serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

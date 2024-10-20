from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from players.models import Player
from players.serializers import PlayerSerializer
from rest_framework.request import Request
from typing import Dict


@api_view(['POST'])
def player_register(request: Request) -> Response:
    """
    Register a new player.
    """
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def player_list(request: Request) -> Response:
    """
    List all players.
    """
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def player_update(request: Request) -> Response:
    """
    Update player information.
    """
    player_id: int = request.data.get('id')

    if not player_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=404)

    serializer = PlayerSerializer(player, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def player_delete(request: Request) -> Response:
    """
    Delete a player by ID.
    """
    player_id: int = request.data.get('id')

    if not player_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=404)

    player.delete()
    return Response({'message': 'Player deleted successfully'}, status=204)


@api_view(['POST'])
def get_player_by_id(request: Request) -> Response:
    """
    Retrieve a player by their ID using POST method.
    """
    player_id: int = request.data.get('id')

    if not player_id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PlayerSerializer(player)
    return Response(serializer.data, status=status.HTTP_200_OK)

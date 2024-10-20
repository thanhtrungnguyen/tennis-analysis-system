from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from matches.models import Match, MatchPlayer
from players.models import Player
from matches.serializers import MatchSerializer
from rest_framework.request import Request
from typing import Dict


@api_view(['POST'])
def match_register(request: Request) -> Response:
    """
    Register a new match with associated players.
    """
    match_data = request.data.get('match')
    players_data = request.data.get('players')

    # Validate and save the match
    match_serializer = MatchSerializer(data=match_data)
    if match_serializer.is_valid():
        match = match_serializer.save()

        # Validate and save match players
        if players_data:
            for player_data in players_data:
                player_id = player_data.get('player_id')
                role = player_data.get('role')
                try:
                    player = Player.objects.get(pk=player_id)
                except Player.DoesNotExist:
                    return Response({'error': f'Player with id {player_id} not found'}, status=404)

                MatchPlayer.objects.create(match=match, player=player, role=role)

        return Response(match_serializer.data, status=201)
    return Response(match_serializer.errors, status=400)


@api_view(['POST'])
def match_list(request: Request) -> Response:
    """
    List all matches with associated players.
    """
    matches = Match.objects.all()
    serializer = MatchSerializer(matches, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def match_update(request: Request) -> Response:
    """
    Update match information and associated players.
    """
    match_id: int = request.data.get('id')
    match_data = request.data.get('match')
    players_data = request.data.get('players')

    if not match_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        match = Match.objects.get(pk=match_id)
    except Match.DoesNotExist:
        return Response({'error': 'Match not found'}, status=404)

    # Update match details
    match_serializer = MatchSerializer(match, data=match_data, partial=True)
    if match_serializer.is_valid():
        match = match_serializer.save()

        # Update match players if provided
        if players_data:
            MatchPlayer.objects.filter(match=match).delete()  # Clear previous players
            for player_data in players_data:
                player_id = player_data.get('player_id')
                role = player_data.get('role')
                try:
                    player = Player.objects.get(pk=player_id)
                except Player.DoesNotExist:
                    return Response({'error': f'Player with id {player_id} not found'}, status=404)

                MatchPlayer.objects.create(match=match, player=player, role=role)

        return Response(match_serializer.data, status=200)
    return Response(match_serializer.errors, status=400)


@api_view(['POST'])
def match_delete(request: Request) -> Response:
    """
    Delete a match by ID along with its associated players.
    """
    match_id: int = request.data.get('id')

    if not match_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        match = Match.objects.get(pk=match_id)
    except Match.DoesNotExist:
        return Response({'error': 'Match not found'}, status=404)

    match.delete()
    return Response({'message': 'Match deleted successfully'}, status=204)


@api_view(['POST'])
def get_match_by_id(request: Request) -> Response:
    """
    Retrieve a match by its ID with associated players using POST method.
    """
    match_id: int = request.data.get('id')

    if not match_id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        match = Match.objects.get(pk=match_id)
    except Match.DoesNotExist:
        return Response({'error': 'Match not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MatchSerializer(match)
    return Response(serializer.data, status=status.HTTP_200_OK)

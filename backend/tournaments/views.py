from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tournaments.models import Tournament, VideoSegment
from tournaments.serializers import TournamentSerializer, VideoSegmentSerializer
from rest_framework.request import Request
from typing import Dict


@api_view(['POST'])
def tournament_register(request: Request) -> Response:
    """
    Register a new tournament.
    """
    serializer = TournamentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def tournament_list(request: Request) -> Response:
    """
    List all tournaments.
    """
    tournaments = Tournament.objects.all()
    serializer = TournamentSerializer(tournaments, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def tournament_update(request: Request) -> Response:
    """
    Update a tournament.
    """
    tournament_id = request.data.get('id')

    if not tournament_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except Tournament.DoesNotExist:
        return Response({'error': 'Tournament not found'}, status=404)

    serializer = TournamentSerializer(tournament, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def tournament_delete(request: Request) -> Response:
    """
    Delete a tournament.
    """
    tournament_id = request.data.get('id')

    if not tournament_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except Tournament.DoesNotExist:
        return Response({'error': 'Tournament not found'}, status=404)

    tournament.delete()
    return Response({'message': 'Tournament deleted successfully'}, status=204)


@api_view(['POST'])
def get_tournament_by_id(request: Request) -> Response:
    """
    Retrieve a tournament by its ID.
    """
    tournament_id = request.data.get('id')

    if not tournament_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except Tournament.DoesNotExist:
        return Response({'error': 'Tournament not found'}, status=404)

    serializer = TournamentSerializer(tournament)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def video_segment_register(request: Request) -> Response:
    """
    Register a new video segment.
    """
    serializer = VideoSegmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def video_segment_list(request: Request) -> Response:
    """
    List all video segments.
    """
    video_segments = VideoSegment.objects.all()
    serializer = VideoSegmentSerializer(video_segments, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def video_segment_update(request: Request) -> Response:
    """
    Update a video segment.
    """
    video_segment_id = request.data.get('id')

    if not video_segment_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        video_segment = VideoSegment.objects.get(pk=video_segment_id)
    except VideoSegment.DoesNotExist:
        return Response({'error': 'Video Segment not found'}, status=404)

    serializer = VideoSegmentSerializer(video_segment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def video_segment_delete(request: Request) -> Response:
    """
    Delete a video segment.
    """
    video_segment_id = request.data.get('id')

    if not video_segment_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        video_segment = VideoSegment.objects.get(pk=video_segment_id)
    except VideoSegment.DoesNotExist:
        return Response({'error': 'Video Segment not found'}, status=404)

    video_segment.delete()
    return Response({'message': 'Video Segment deleted successfully'}, status=204)


@api_view(['POST'])
def get_video_segment_by_id(request: Request) -> Response:
    """
    Retrieve a video segment by its ID.
    """
    video_segment_id = request.data.get('id')

    if not video_segment_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        video_segment = VideoSegment.objects.get(pk=video_segment_id)
    except VideoSegment.DoesNotExist:
        return Response({'error': 'Video Segment not found'}, status=404)

    serializer = VideoSegmentSerializer(video_segment)
    return Response(serializer.data, status=200)

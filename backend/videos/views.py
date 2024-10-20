from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from videos.models import Video
from videos.serializers import VideoSerializer
from rest_framework.request import Request
from typing import Dict

@api_view(['POST'])
def video_register(request: Request) -> Response:
    """
    Register a new video.
    """
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def video_list(request: Request) -> Response:
    """
    List all videos.
    """
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def video_update(request: Request) -> Response:
    """
    Update video information.
    """
    video_id: int = request.data.get('id')

    if not video_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        return Response({'error': 'Video not found'}, status=404)

    serializer = VideoSerializer(video, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def video_delete(request: Request) -> Response:
    """
    Delete a video by ID.
    """
    video_id: int = request.data.get('id')

    if not video_id:
        return Response({'error': 'ID is required'}, status=400)

    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        return Response({'error': 'Video not found'}, status=404)

    video.delete()
    return Response({'message': 'Video deleted successfully'}, status=204)


@api_view(['POST'])
def get_video_by_id(request: Request) -> Response:
    """
    Retrieve a video by its ID using POST method.
    """
    video_id: int = request.data.get('id')

    if not video_id:
        return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = VideoSerializer(video)
    return Response(serializer.data, status=status.HTTP_200_OK)

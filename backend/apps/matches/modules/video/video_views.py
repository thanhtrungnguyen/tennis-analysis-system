from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import viewsets, status
from apps.matches.models.video import Video
from apps.matches.modules.video.video_serializers import VideoSerializer
from core.services.s3_service import upload_file_to_s3

class VideoViewSet(viewsets.ModelViewSet):
    """CRUD operations for Video."""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        """Upload video to S3 and save metadata."""
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        # Upload to S3 and get the file URL
        file_url = upload_file_to_s3(file, folder='videos/')
        if not file_url:
            return Response({"error": "Failed to upload video."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save video metadata in the database
        serializer = self.get_serializer(data={"file": file_url})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

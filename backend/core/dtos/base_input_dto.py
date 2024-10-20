from rest_framework import serializers

class PaginationDTO(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, default=1)
    page_size = serializers.IntegerField(min_value=1, default=10)


class BaseInputDTO(serializers.Serializer):
    pagination = PaginationDTO(required=False)  # Pagination object is optional
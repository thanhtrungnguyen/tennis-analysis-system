from rest_framework import serializers
from enum import Enum
from typing import Optional, Dict, Any

class ResultCode(Enum):
    SUCCESS = 0
    VALIDATION_ERROR = 1
    NOT_FOUND = 2
    SERVER_ERROR = 9

class BaseOutputDTO(serializers.Serializer):
    message: serializers.CharField = serializers.CharField(max_length=255, allow_blank=True, default="")
    result_code: serializers.ChoiceField = serializers.ChoiceField(choices=[(tag, tag.value) for tag in ResultCode])
    data: Optional[serializers.JSONField] = serializers.JSONField(required=False)
    validation_errors: Optional[Dict[str, Any]] = serializers.DictField(
        child=serializers.CharField(), required=False, allow_null=True
    )

    def create(self, validated_data: Dict[str, Any]) -> Dict[str, Any]:
        return validated_data

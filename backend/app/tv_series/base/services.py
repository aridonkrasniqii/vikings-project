from abc import ABC, abstractmethod
from rest_framework import status
from rest_framework.response import Response

from tv_series.base.models.entity_response import EntityResponse
from tv_series.base.models.paginated_response import PaginatedResponse
from tv_series.base.validators import BaseValidator

class BaseService(ABC):

    def __init__(self, serializer, paginated_serializer):
        self.serializer = serializer
        self.paginated_serializer = paginated_serializer

    @abstractmethod
    def get_all(self, request, view):
        pass

    @abstractmethod
    def get_by_id(self, obj_id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    def _validate_id(self, obj_id):
        is_valid_id, error_message = BaseValidator.validate_id(obj_id)
        if not is_valid_id:
            return self.response(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

    def response(self, data, status_code=status.HTTP_200_OK,  message=None):
        return EntityResponse(self.serializer, data, status_code, message)

    def paginated_response(self, data, status_code=status.HTTP_200_OK, message=None):
        return PaginatedResponse(self.paginated_serializer, data, status_code, message)
from rest_framework import status

from tv_series.base.models.entity_response import EntityResponse
from tv_series.base.serializers import VikingSerializer, PaginatedVikingSerializer
from tv_series.base.services import BaseService
from tv_series.base.validators import BaseValidator
from tv_series.vikings.vikings_model import Viking
from tv_series.vikings.vikings_validator import VikingValidator


class VikingsService(BaseService):

    VIKING_CREATED = 'Vikings created'
    VIKING_UPDATED = 'Vikings updated'
    VIKING_DELETED = 'Vikings deleted'
    VIKING_NOT_FOUND = 'Vikings not found'

    def __init__(self):
        super().__init__(VikingSerializer, PaginatedVikingSerializer)

    def get_all(self, request):
        return self.paginated_response(Viking.objects.get_paginated_vikings(request, view=self))

    def get_by_id(self, viking_id):
        self._validate_id(viking_id)

        viking = Viking.objects.get_viking_by_id(viking_id)

        if viking:
            return self.response(viking, status.HTTP_200_OK)
        return self.response(None, status.HTTP_404_NOT_FOUND, self.VIKING_CREATED)

    def create(self, data):
        self._validate_data(data)
        created_viking = Viking.objects.create_viking(data)
        return self.response(created_viking, status.HTTP_201_CREATED)

    def update(self, viking_id, data):
        self._validate_id(viking_id)

        viking = Viking.objects.get_viking_by_id(viking_id)
        if not viking:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.VIKING_NOT_FOUND)

        self._validate_data(data)
        updated_viking = Viking.objects.update_viking(data)
        return self.response(updated_viking, status.HTTP_200_OK, self.VIKING_UPDATED)

    def delete(self, viking_id):
        validation_response = self._validate_id(viking_id)
        if validation_response:
            return validation_response

        viking = Viking.objects.get_viking_by_id(viking_id)
        if not viking:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.VIKING_NOT_FOUND)

        Viking.objects.delete_viking(viking)
        return self.response(viking, status.HTTP_200_OK, self.VIKING_DELETED)

    def _validate_id(self, viking_id):
        is_valid_id, error_message = BaseValidator.validate_id(viking_id)
        if not is_valid_id:
            return EntityResponse(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

    def _validate_data(self, data):
        name = data.get('name')
        description = data.get('description')
        photo = data.get('photo')
        actor_name = data.get('actor_name')

        validator = VikingValidator(name, description, photo, actor_name)
        is_valid, error_message = validator.validate()

        if not is_valid:
            return self.response(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

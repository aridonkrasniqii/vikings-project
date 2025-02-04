from rest_framework import status
from tv_series.base.models.entity_response import EntityResponse
from tv_series.base.serializers import NorsemanSerializer, PaginatedNorsemanSerializer
from tv_series.base.services import BaseService
from tv_series.base.validators import BaseValidator
from tv_series.norsemans.norsemen_models import Norseman
from tv_series.norsemans.norsemen_validators import NorsemanValidator


class NorsemenService(BaseService):

    NORSEMAN_CREATED = 'Norseman created'
    NORSEMAN_UPDATED = 'Norseman updated'
    NORSEMAN_DELETED = 'Norseman deleted'
    NORSEMAN_NOT_FOUND = 'Norseman not found'

    def __init__(self):
        super().__init__(NorsemanSerializer, PaginatedNorsemanSerializer)

    def get_all(self, request, view):
        return self.paginated_response(Norseman.objects.get_paginated_norsemen(request, view))

    def get_by_id(self, norseman_id):
        self._validate_id(norseman_id)

        norseman = Norseman.objects.get_norseman_by_id(norseman_id)

        if norseman:
            return self.response(norseman, status.HTTP_200_OK)
        return self.response(None, status.HTTP_404_NOT_FOUND, self.NORSEMAN_NOT_FOUND)

    def create(self, data):
        self._validate_data(data)
        created_norseman = Norseman.objects.create_norseman(data)
        return self.response(created_norseman, status.HTTP_201_CREATED)

    def update(self, norseman_id, data):
        self._validate_id(norseman_id)

        norseman = Norseman.objects.get_norseman_by_id(norseman_id)
        if not norseman:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.NORSEMAN_NOT_FOUND)

        self._validate_data(data)
        updated_norseman = Norseman.objects.update_norseman(norseman_id, data)
        return self.response(updated_norseman, status.HTTP_200_OK, self.NORSEMAN_UPDATED)

    def delete(self, norseman_id):
        validation_response = self._validate_id(norseman_id)
        if validation_response:
            return validation_response

        norseman = Norseman.objects.get_norseman_by_id(norseman_id)
        if not norseman:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.NORSEMAN_NOT_FOUND)

        Norseman.objects.delete_norseman(norseman)
        return self.response(norseman, status.HTTP_200_OK, self.NORSEMAN_DELETED)

    def _validate_id(self, norseman_id):
        is_valid_id, error_message = BaseValidator.validate_id(norseman_id)
        if not is_valid_id:
            return EntityResponse(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

    def _validate_data(self, data):
        name = data.get('name')
        description = data.get('description')
        photo = data.get('photo')
        actor_name = data.get('actor_name')

        validator = NorsemanValidator(name, description, photo, actor_name)
        is_valid, error_message = validator.validate()

        if not is_valid:
            return self.response(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

from asgiref.sync import sync_to_async
from django.db import transaction
from rest_framework import status

from api.base.serializers import VikingSerializer, PaginatedVikingSerializer
from api.base.services import BaseService
from api.vikings.vikings_model import Viking
from api.vikings.vikings_validator import VikingValidator


class VikingsService(BaseService):

    VIKING_CREATED = 'Vikings created'
    VIKING_UPDATED = 'Vikings updated'
    VIKING_DELETED = 'Vikings deleted'
    VIKING_NOT_FOUND = 'Vikings not found'

    def __init__(self):
        super().__init__(VikingSerializer, PaginatedVikingSerializer)

    def get_all(self, request, view):
        return self.paginated_response(Viking.objects.get_paginated_vikings(request, view))

    def get_by_id(self, viking_id):
        self._validate_id(viking_id)

        viking = Viking.objects.get_viking_by_id(viking_id)

        if viking:
            return self.response(viking, status.HTTP_200_OK)
        return self.response([], status.HTTP_404_NOT_FOUND, self.VIKING_NOT_FOUND)

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
        updated_viking = Viking.objects.update_viking(viking_id, data)
        return self.response(updated_viking, status.HTTP_200_OK, self.VIKING_UPDATED)

    @sync_to_async
    def update_or_create(self, data):
        validation_response = self._validate_data(data)
        if validation_response:
            raise ValueError(f"Invalid data: {validation_response}")

        with transaction.atomic():
            viking, created = Viking.objects.update_or_create(
                name=data.get('name'),
                defaults={
                    'actor_name': data.get('actor_name'),
                    'description': data.get('description'),
                    'photo': data.get('photo'),
                }
            )
        # No need to return response objects here, just ensure the record is created or updated
        return viking

    def delete(self, viking_id):
        self._validate_id(viking_id)

        viking = Viking.objects.get_viking_by_id(viking_id)
        if not viking:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.VIKING_NOT_FOUND)

        Viking.objects.delete_viking(viking)
        return self.response(viking, status.HTTP_200_OK, self.VIKING_DELETED)

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

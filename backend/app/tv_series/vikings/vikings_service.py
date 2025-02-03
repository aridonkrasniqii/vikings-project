from rest_framework import status

from tv_series.base.models.custom_response import CustomResponse
from tv_series.base.validators import BaseValidator
from tv_series.vikings.vikings_model import Viking
from tv_series.vikings.vikings_validator import VikingValidator


class VikingsService:
    def __init__(self):
        pass

    def get_all(self):
        vikings = Viking.objects.all()
        return CustomResponse(vikings, status.HTTP_200_OK)

    def get_by_id(self, viking_id):
        validation_response = self._validate_id(viking_id)
        if validation_response:
            return validation_response

        viking = Viking.objects.get_viking_by_id(viking_id)
        if viking:
            return CustomResponse(viking, status.HTTP_200_OK)
        return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Viking not found")

    def create(self, data):
        validation_response = self._validate_data(data)
        if validation_response:
            return validation_response

        created_viking = Viking.objects.create_viking(
            data['name'], data['description'], data['photo'], data['actor_name']
        )
        return CustomResponse(created_viking, status.HTTP_201_CREATED)

    def update(self, viking_id, data):
        # Generalized ID validation and response
        validation_response = self._validate_id(viking_id)
        if validation_response:
            return validation_response

        viking = Viking.objects.get_viking_by_id(viking_id)
        if not viking:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Viking not found")

        validation_response = self._validate_data(data)
        if validation_response:
            return validation_response

        updated_viking = Viking.objects.update_viking(
            viking, data['name'], data['description'], data['photo'], data['actor_name']
        )
        return CustomResponse(updated_viking, status.HTTP_200_OK)

    def delete(self, viking_id):
        validation_response = self._validate_id(viking_id)
        if validation_response:
            return validation_response

        viking = Viking.objects.get_viking_by_id(viking_id)
        if not viking:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Viking not found")

        Viking.objects.delete_viking(viking)
        return CustomResponse(None, status.HTTP_204_NO_CONTENT)

    def _validate_id(self, viking_id):
        is_valid_id, error_message = BaseValidator.validate_id(viking_id)
        if not is_valid_id:
            return CustomResponse(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

    def _validate_data(self, data):
        name = data.get('name')
        description = data.get('description')
        photo = data.get('photo')
        actor_name = data.get('actor_name')

        validator = VikingValidator(name, description, photo, actor_name)
        is_valid, error_message = validator.validate()

        if not is_valid:
            return CustomResponse(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

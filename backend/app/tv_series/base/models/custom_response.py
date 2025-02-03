from rest_framework.response import Response
from rest_framework import status

import importlib

class CustomResponse(Response):
    def __init__(self, data=None, status_code=status.HTTP_200_OK, message=None, **kwargs):
        if data is None:
            data = {}

        if hasattr(data, 'model') or isinstance(data, list):
            serializer = self.get_serializer(data)
            data = serializer.data

        response_data = {
            "status_code": status_code,
            "data": data,
            "message": message or ''
        }

        super().__init__(data=response_data, status=status_code, **kwargs)

    def get_serializer(self, data):
        if hasattr(data, 'model'):
            model = data.model
            serializer_class = self.get_model_serializer(model)
            return serializer_class(data, many=True)
        return data  # If it's a simple list, return as is

    def get_model_serializer(self, model):
        model_name = model.__name__
        try:
            # Dynamically load the serializer module
            module = importlib.import_module(f'.serializers', package=model.__module__.split('.')[0])
            # Dynamically get the serializer class
            serializer_class = getattr(module, f'{model_name}Serializer')
            return serializer_class
        except (ImportError, AttributeError) as e:
            raise ValueError(f"Serializer for {model_name} not found: {str(e)}")

from collections.abc import Iterable

from rest_framework import status
from rest_framework.response import Response


class PaginatedResponse(Response):
    def __init__(self, serializer, data=None, status_code=status.HTTP_200_OK, message=None, **kwargs):
        if data is None:
            data = {}

        if isinstance(data, list) or isinstance(data, Iterable):
            data = serializer(data, many=True).data
        else:
            data = serializer(data).data

        response_data = data

        super().__init__(data=response_data, status=status_code, **kwargs)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BaseListView(APIView):
    service_class = None

    def __init__(self, **kwargs):
        self.service = self.service_class()
        super().__init__(**kwargs)

    def get(self, request):
        return Response(self.service.get_all())

    def post(self, request):
        return Response(self.service.create(request.data))


class BaseDetailView(APIView):
    service_class = None

    def __init__(self, **kwargs):
        self.service = self.service_class()
        super().__init__(**kwargs)

    def get(self, request, pk=None):
        return Response(self.service.get_by_id(pk))

    def put(self, request, pk=None):
        return Response(self.service.update(pk, request.data))

    def delete(self, request, pk=None):
        return Response(self.service.delete(pk))

from rest_framework.response import Response
from rest_framework.views import APIView

class BaseListView(APIView):

    service = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return self.service.get_all()

    def post(self, request):
        return self.service.create(request.data)


class BaseDetailView(APIView):
    service = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, pk=None):
        return self.service.get_by_id(pk)

    def put(self, request, pk=None):
        return self.service.update(pk, request.data)

    def delete(self, request, pk=None):
        return self.service.delete(pk)

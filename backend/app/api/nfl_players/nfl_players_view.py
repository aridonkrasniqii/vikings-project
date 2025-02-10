from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.base.views import BaseListView, BaseDetailView
from api.nfl_players.nfl_players_service import NFLPlayerService

class NFLPlayerListView(BaseListView):
    def __init__(self, **kwargs):
        self.service = NFLPlayerService()
        super().__init__(**kwargs)

    def get(self, request):
        return self.service.get_all(request, view=self)

    def post(self, request):
        return self.service.create(request.data)

class NFLPlayerDetailView(BaseDetailView):
    def __init__(self, **kwargs):
        self.service = NFLPlayerService()
        super().__init__(**kwargs)

    def get(self, request, pk=None):
        return self.service.get_by_id(pk)

    def put(self, request, pk=None):
        return self.service.update(pk, request.data)

    def delete(self, request, pk=None):
        return self.service.delete(pk)


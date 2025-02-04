from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tv_series.base.views import BaseListView, BaseDetailView
from tv_series.vikings.vikings_service import VikingsService
from vikings_scraper.vikings_scraper.tasks import scrape_vikings


class VikingsListView(BaseListView):
    def __init__(self, **kwargs):
        self.service = VikingsService()
        super().__init__(**kwargs)

    def get(self, request):
        return self.service.get_all(request)

    def post(self, request):
        return self.service.create(request.data)

class VikingsDetailView(BaseListView):
    def __init__(self, **kwargs):
        self.service = VikingsService()
        super().__init__(**kwargs)

    def get(self, request, pk=None):
        return self.service.get_by_id(pk)

    def put(self, request, pk=None):
        return self.service.update(pk, request.data)

    def delete(self, request, pk=None):
        return self.service.delete(pk)
class VikingsScrapeView(APIView):

    def post(self, request):
        scrape_vikings().delay()
        return Response({"message": "Scraping Vikings started"}, status=status.HTTP_202_ACCEPTED)



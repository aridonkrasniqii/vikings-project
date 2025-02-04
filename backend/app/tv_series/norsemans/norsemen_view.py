from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tv_series.norsemans.norsemen_service import NorsemenService
from tv_series.base.views import BaseListView, BaseDetailView
from vikings_scraper.vikings_scraper.tasks import scrape_norsemen


class NorsemanListView(BaseListView):
    def __init__(self, **kwargs):
        self.service = NorsemenService()
        super().__init__(**kwargs)

    def get(self, request):
        return self.service.get_all(request, view=self)

    def post(self, request):
        return self.service.create(request.data)

class NorsemanDetailView(BaseDetailView):
    def __init__(self, **kwargs):
        self.service = NorsemenService()
        super().__init__(**kwargs)

    def get(self, request, pk=None):
        return self.service.get_by_id(pk)

    def put(self, request, pk=None):
        return self.service.update(pk, request.data)

    def delete(self, request, pk=None):
        return self.service.delete(pk)

class NorsemanScrapeView(APIView):
    def post(self, request):
        scrape_norsemen().delay()
        return Response({"message": "Scraping norseman started"}, status=status.HTTP_202_ACCEPTED)

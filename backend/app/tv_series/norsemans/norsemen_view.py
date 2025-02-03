from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tv_series.base.views import BaseListView, BaseDetailView
from tv_series.norsemans.norsemen_service import NorsemenService
from vikings_scraper.vikings_scraper.tasks import scrape_norsemen


class NorsemanListView(BaseListView):
    service_class = NorsemenService


class NorsemanDetailView(BaseDetailView):
    service_class = NorsemenService

class NorsemanScrapeView(APIView):

    def post(self, request):
        scrape_norsemen().delay()
        return Response({"message": "Scraping Norsemen started"}, status=status.HTTP_202_ACCEPTED)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tv_series.base.views import BaseListView, BaseDetailView
from tv_series.vikings.vikings_service import VikingsService
from vikings_scraper.vikings_scraper.tasks import scrape_vikings


class VikingsListView(BaseListView):
    service = VikingsService


class VikingsDetailView(BaseDetailView):
    service = VikingsService

class VikingsScrapeView(APIView):

    def post(self, request):
        scrape_vikings().delay()
        return Response({"message": "Scraping Vikings started"}, status=status.HTTP_202_ACCEPTED)



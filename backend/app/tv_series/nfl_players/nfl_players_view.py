from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tv_series.base.views import BaseListView, BaseDetailView
from tv_series.nfl_players.nfl_players_service import NFLPlayerService
from vikings_scraper.vikings_scraper.tasks import scrape_nfl_players

class NFLPlayerListView(BaseListView):
    service = NFLPlayerService

class NFLPlayerDetailView(BaseDetailView):
    service = NFLPlayerService

class NFLPlayerScrapeView(APIView):

    def post(self, request):
        scrape_nfl_players().delay()
        return Response({"message": "Scraping NFL Players started"}, status=status.HTTP_202_ACCEPTED)
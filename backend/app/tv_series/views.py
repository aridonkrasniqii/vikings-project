from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import VikingService, NorsemanService, NFLPlayerService, NflPlayerStatsService
from vikings_scraper.vikings_scraper.tasks import scrape_vikings, scrape_nfl, scrape_norsemen


import logging 

class VikingView(APIView):

    def __init__(self, **kwargs):
        self.viking_service = VikingService()
        super().__init__(**kwargs)

    @action(detail=False, methods=['get']) 
    def get(self, request):
        return self.viking_service.get_all()

    @action(detail=True, methods=['get']) 
    def get_by_id(self, request, pk=None):
        return self.viking_service.get_by_id(pk)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return self.viking_service.create(request.data)
        
    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return self.viking_service.update(pk, request.data)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        return self.viking_service.delete(pk)
    
    @action(detail=False, methods=['post'])
    def scrape(self, request):
        scrape_vikings.delay()
        return Response({"message": "Scraping started"}, status=status.HTTP_202_ACCEPTED)

class NorsemanView(APIView):

    def __init__(self, **kwargs):
        self.norsemen_service = NorsemanService()
        super().__init__(**kwargs)

    @action(detail=False, methods=['get']) 
    def get(self, request):
        return self.norsemen_service.get_all()

    @action(detail=True, methods=['get']) 
    def get_by_id(self, request, pk=None):
        return self.norsemen_service.get_by_id(pk)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return self.norsemen_service.create(request.data)
        
    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return self.norsemen_service.update(pk, request.data)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        return self.norsemen_service.delete(pk)
    
    @action(detail=False, methods=['post'])
    def scrape(self, request):
        scrape_norsemen.delay() # Trigger scraping via Celery task 
        return Response({"message": "Scraping started"}, status=status.HTTP_202_ACCEPTED)

class NFLPlayerView(APIView):

    def __init__(self, **kwargs):
        self.nfl_player_service = NFLPlayerService()
        super().__init__(**kwargs)

    @action(detail=False, methods=['get']) 
    def get(self, request):
        return self.nfl_player_service.get_all()

    @action(detail=True, methods=['get']) 
    def get_by_id(self, request, pk=None):
        return self.nfl_player_service.get_by_id(pk)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return self.nfl_player_service.create(request.data)
        
    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return self.nfl_player_service.update(pk, request.data)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        return self.nfl_player_service.delete(pk)
    
    @action(detail=False, methods=['post'])
    def scrape(self, request):
        scrape_nfl.delay() # Trigger scraping via Celery task
        return Response({"message": "Scraping started"}, status=status.HTTP_202_ACCEPTED)

class NflPlayerStats(APIView):

    def __init__(self, **kwargs):
        self.stats_service = NflPlayerStatsService()
        super().__init__(**kwargs)

    @action(detail=False, methods=['get']) 
    def get(self, request):
        return self.stats_service.get_all()

    @action(detail=True, methods=['get']) 
    def get_by_id(self, request, pk=None):
        return self.stats_service.get_by_id(pk)

    @action(detail=False, methods=['post'])
    def post(self, request):
        return self.stats_service.create(request.data)
        
    @action(detail=True, methods=['put'])
    def put(self, request, pk=None):
        return self.stats_service.update(pk, request.data)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        return self.stats_service.delete(pk)

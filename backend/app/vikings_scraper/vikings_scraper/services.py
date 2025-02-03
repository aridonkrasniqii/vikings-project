from tv_series.nfl_players.nfl_players_service import NFLPlayerService
from tv_series.norsemans.norsemen_service import NorsemenService
from tv_series.vikings.vikings_service import VikingsService


class VikingsScraperService:
    def __init__(self):
        self.viking_service = VikingsService()
        self.norsemen_service = NorsemenService()
        self.nfl_player_service = NFLPlayerService()
    
    @staticmethod
    def create_vikings(self, vikings_data):
        for viking_data in vikings_data:
            self.viking_service.create(viking_data)
    
    @staticmethod 
    def create_norsemen(self, norsemen_data):
        for norseman_data in norsemen_data:
            self.norsemen_service.create(norseman_data)
    
    @staticmethod 
    def create_nfl_players(self, nfl_players_data):
        for nfl_player_data in nfl_players_data:
            self.nfl_player_service.create(nfl_player_data)
    
        
    

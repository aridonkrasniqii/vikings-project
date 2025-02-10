from itemadapter import ItemAdapter

from api.nfl_players.nfl_players_service import NFLPlayerService
from api.norsemans.norsemen_service import NorsemenService
from api.vikings.vikings_service import VikingsService

class VikingsScraperService:
    def __init__(self):
        self.viking_service = VikingsService()
        self.norsemen_service = NorsemenService()
        self.nfl_player_service = NFLPlayerService()

    async def process_viking(self, item):
        adapter = ItemAdapter(item)
        viking_data = {
            'name': adapter.get('name'),
            'photo': adapter.get('photo'),
            'description': adapter.get('description'),
            'actor_name': adapter.get('actor_name'),
        }
        return await self.viking_service.update_or_create(viking_data)

    async def process_norseman(self, item):
        adapter = ItemAdapter(item)
        norseman_data = {
            'name': adapter.get('name'),
            'actor_name': adapter.get('actor_name'),
            'description': adapter.get('description'),
            'photo': adapter.get('photo'),
        }
        return await self.norsemen_service.update_or_create(norseman_data)

    async def process_nfl_player(self, item):
        adapter = ItemAdapter(item)
        nfl_player_data = {
            'name': adapter.get('name'),
            'number': adapter.get('number'),
            'position': adapter.get('position'),
            'age': adapter.get('age'),
            'experience': adapter.get('experience'),
            'college': adapter.get('college'),
            'photo': adapter.get('photo'),
            'stats': adapter.get('stats'),
        }
        return await self.nfl_player_service.update_or_create(nfl_player_data)

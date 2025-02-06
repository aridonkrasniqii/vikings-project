from itemadapter import ItemAdapter
from api.norsemans.norsemen_service import NorsemenService
from api.nfl_players.nfl_players_service import NFLPlayerService
from api.vikings.vikings_service import VikingsService
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

class VikingsScraperPipeline:
    def __init__(self):
        self.viking_service = VikingsService()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        viking = self.viking_service.update_or_create({
            'name': adapter.get('name'),
            'photo': adapter.get('photo'),
            'description': adapter.get('description'),
            'actor_name': adapter.get('actor_name'),
        })
        logger.info(f'Viking: {viking.name} added/updated')
        return item

class NorsemenScraperPipeline:
    def __init__(self):
        self.norseman_service = NorsemenService()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        norseman = self.norseman_service.update_or_create({
            'name': adapter.get('name'),
            'actor_name': adapter.get('actor_name'),
            'description': adapter.get('description'),
            'photo': adapter.get('photo'),
        })
        if norseman:
            logger.info(f'Norseman {norseman.name} added/updated')
        return item

class NFLPlayerScraperPipeline:
    def __init__(self):
        self.nfl_player_service = NFLPlayerService()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        player = self.nfl_player_service.update_or_create({
            'name': adapter.get('name'),
            'number': adapter.get('number'),
            'position': adapter.get('position'),
            'age': adapter.get('age'),
            'experience': adapter.get('experience'),
            'college': adapter.get('college'),
            'photo': adapter.get('photo'),
            'player_link': adapter.get('player_link'),
            'stats': adapter.get('stats'),
        })
        logger.info(f'NFL Player: {player.name} added/updated')
        return item

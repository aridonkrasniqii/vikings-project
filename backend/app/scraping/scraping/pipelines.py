from itemadapter import ItemAdapter
from scrapy import signals

from api.norsemans.norsemen_service import NorsemenService
from api.nfl_players.nfl_players_service import NFLPlayerService
from api.vikings.vikings_service import VikingsService
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class CombinedScraperPipeline:
    def __init__(self):
        self.viking_service = VikingsService()
        self.norseman_service = NorsemenService()
        self.nfl_player_service = NFLPlayerService()

    async def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        logger.info(f"Processing item for spider '{spider.name}'")

        if spider.name == "vikings":
            logger.info(f"creating viking")
            await self.viking_service.update_or_create({
                'name': adapter.get('name'),
                'photo': adapter.get('photo'),
                'description': adapter.get('description'),
                'actor_name': adapter.get('actor_name'),
            })
        elif spider.name == "norsemen":
            await self.norseman_service.update_or_create({
                'name': adapter.get('name'),
                'actor_name': adapter.get('actor_name'),
                'description': adapter.get('description'),
                'photo': adapter.get('photo'),
            })
        elif spider.name == "nflplayers":
            await self.nfl_player_service.update_or_create({
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
        return item

    def open_spider(self, spider):
        logger.info(f"Opening spider '{spider.name}'")

    def close_spider(self, spider):
        logger.info(f"Spider '{spider.name}' closed.")

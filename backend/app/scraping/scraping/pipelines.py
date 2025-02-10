from itemadapter import ItemAdapter
import logging
from scraping.scraping.services import VikingsScraperService

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

class CombinedScraperPipeline:
    def __init__(self):
        self.vikings_scraper_service = VikingsScraperService()

    async def process_item(self, item, spider):
        if spider.name == "vikings":
            await self.process_viking_item(item)
        elif spider.name == "norsemen":
            await self.process_norseman_item(item)
        elif spider.name == "nflplayers":
            await self.process_nfl_player_item(item)

        return item

    async def process_viking_item(self, item):
        adapter = ItemAdapter(item)
        logger.info(f"Processing Viking item: {adapter.get('name')}")
        await self.vikings_scraper_service.process_viking(item)

    async def process_norseman_item(self, item):
        adapter = ItemAdapter(item)
        logger.info(f"Processing Norseman item: {adapter.get('name')}")
        await self.vikings_scraper_service.process_norseman(item)

    async def process_nfl_player_item(self, item):
        adapter = ItemAdapter(item)
        logger.info(f"Processing NFL Player item: {adapter.get('name')}")
        await self.vikings_scraper_service.process_nfl_player(item)

    def open_spider(self, spider):
        logger.info(f"Opening spider '{spider.name}'")

    def close_spider(self, spider):
        logger.info(f"Spider '{spider.name}' closed.")

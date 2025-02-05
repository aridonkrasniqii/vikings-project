
from tv_series.nfl_players.nfl_players_service import NFLPlayerService
from tv_series.norsemans.norsemen_service import NorsemenService
from tv_series.vikings.vikings_service import VikingsService
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
        # self.viking_service.update_or_create(item)
        pass

class NorsemenScraperPipeline:
    def __init__(self):
        self.norseman_service = NorsemenService()

    def process_item(self, item, spider):
        norseman = self.norseman_service.update_or_create(item)
        if norseman:
            logger.info(f"Norsemen {norseman.name} added/updated")

class NFLPlayerScraperPipeline:
    def __init__(self):
        self.nfl_player_service = NFLPlayerService()

    def process_item(self, item, spider):
        # self.nflplayer_service.update_or_create(item)
        pass


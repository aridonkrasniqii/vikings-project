from .spiders.nfl_players_spider import NflPlayersSpider
from .spiders.vikings_spider import VikingsSpider
from .spiders.norsemen_spider import NorsemenSpider

from celery import shared_task
from scrapy.crawler import CrawlerProcess

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)



@shared_task
def scrape_vikings():
    process = CrawlerProcess(settings={
        'ITEM_PIPELINES': {'vikings_scraper.pipelines.VikingsScraperPipeline': 300}
    })
    process.crawl(VikingsSpider)
    process.start()

@shared_task
def scrape_norsemen():
    logger.info('Starting the NorsemenSpider')
    process = CrawlerProcess(settings={
        'ITEM_PIPELINES': {'vikings_scraper.pipelines.NorsemenScraperPipeline': 300}
    })
    process.crawl(NorsemenSpider)
    process.start()

@shared_task
def scrape_nfl_players():
    process = CrawlerProcess(settings={
        'ITEM_PIPELINES': {'vikings_scraper.pipelines.NFLPlayerScraperPipeline': 300}
    })
    process.crawl(NflPlayersSpider)
    process.start()

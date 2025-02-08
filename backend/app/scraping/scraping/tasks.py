

from scraping.scraping.spiders.nfl_players_spider import NflPlayersSpider
from scraping.scraping.spiders.vikings_spider import VikingsSpider
from scraping.scraping.spiders.norsemen_spider import NorsemenSpider

from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

@shared_task
def scrape_vikings():
    logger.info('Scraping Vikings')
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(VikingsSpider)
    process.start()
    

@shared_task
def scrape_norsemen():
    logger.info('Scraping NorsemenSpider')
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(NorsemenSpider)
    process.start()


@shared_task
def scrape_nfl_players():
    logger.info('Scraping NflPlayersSpider')
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(NflPlayersSpider)
    process.start()

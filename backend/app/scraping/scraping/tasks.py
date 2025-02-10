import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraping.scraping.spiders.nfl_players_spider import NflPlayersSpider
from scraping.scraping.spiders.vikings_spider import VikingsSpider
from scraping.scraping.spiders.norsemen_spider import NorsemenSpider

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

from scraping.scraping.celery import app 

def run_spider(spider_class):
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(spider_class)
    process.start(stop_after_crawl=False)

@app.task
def scrape_vikings(*args, **kwargs):
    logger.info('Scraping Vikings')
    run_spider(VikingsSpider)

@app.task
def scrape_norsemen(*args, **kwargs):
    logger.info('Scraping Norsemen')
    run_spider(NorsemenSpider)

@app.task
def scrape_nfl_players(*args, **kwargs):
    logger.info('Scraping NFL Players')
    run_spider(NflPlayersSpider)

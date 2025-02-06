from scrapy import signals
from scrapy.settings import Settings

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

from scraping.scraping import settings as my_settings

@shared_task
def scrape_vikings():
    logger.info('Starting the VikingsSpider')
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    crawler_settings.update({'ITEM_PIPELINES': {
            'scraping.pipelines.VikingsScraperPipeline': 300
    }})

    process = CrawlerProcess(settings=crawler_settings)

    # def _on_spider_opened(spider):
    #     logger.info(f"Spider opened: {spider.name}")
    #
    # def _on_item_scraped(item, response, spider):
    #     logger.info(f"Item scraped: {item}")
    #
    # def _on_spider_closed(spider, reason):
    #     logger.info(f"Spider closed: {spider.name}, reason: {reason}")
    #
    # process.signals.connect(_on_spider_opened, signal=signals.spider_opened)
    # process.signals.connect(_on_item_scraped, signal=signals.item_scraped)
    # process.signals.connect(_on_spider_closed, signal=signals.spider_closed)
    process.crawl(VikingsSpider)


@shared_task
def scrape_norsemen():
    logger.info('Starting the NorsemenSpider')
    process = CrawlerProcess(settings=get_project_settings())

    def _on_spider_opened(spider):
        logger.info(f"Spider opened: {spider.name}")

    def _on_item_scraped(item, response, spider):
        logger.info(f"Item scraped: {item}")

    def _on_spider_closed(spider, reason):
        logger.info(f"Spider closed: {spider.name}, reason: {reason}")

    process.crawl(
        NorsemenSpider,
        pipeline='scraping.pipelines.NorsemenScraperPipeline',
        signals={
            'spider_opened': _on_spider_opened,
            'item_scraped': _on_item_scraped,
            'spider_closed': _on_spider_closed
        }
    )
    process.start()


@shared_task
def scrape_nfl_players():
    logger.info('Starting the NflPlayersSpider')
    process = CrawlerProcess(settings=get_project_settings())

    def _on_spider_opened(spider):
        logger.info(f"Spider opened: {spider.name}")

    def _on_item_scraped(item, response, spider):
        logger.info(f"Item scraped: {item}")

    def _on_spider_closed(spider, reason):
        logger.info(f"Spider closed: {spider.name}, reason: {reason}")

    process.crawl(
        NflPlayersSpider,
        pipeline='scraping.pipelines.NFLPlayerScraperPipeline',
        signals={
            'spider_opened': _on_spider_opened,
            'item_scraped': _on_item_scraped,
            'spider_closed': _on_spider_closed
        }
    )
    process.start()

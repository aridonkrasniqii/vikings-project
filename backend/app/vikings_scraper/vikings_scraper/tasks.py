from celery import shared_task
from scrapy.crawler import CrawlerProcess

from vikings_scraper.vikings_scraper.services import VikingsScraperService
from vikings_scraper.vikings_scraper.spiders.spiders import VikingsSpider, NorsemenSpider, NflPlayersSpider


@shared_task
def scrape_vikings():
    # Get project settings for Scrapy
    # settings = get_project_settings()
    process = CrawlerProcess(settings={})
    service = VikingsScraperService()
    vikings_data = process.crawl(VikingsSpider)  # Returns data from the spider
    service.create_vikings(vikings_data)
    process.start()

@shared_task
def scrape_norsemen():
    process = CrawlerProcess(settings={})
    service = VikingsScraperService()
    norsemen_data = process.crawl(NorsemenSpider)
    service.create_norsemen(norsemen_data)
    process.start()

@shared_task
def scrape_nfl():
    process = CrawlerProcess(settings={})
    service = VikingsScraperService()
    nfl_data = process.crawl(NflPlayersSpider)
    service.create_nfl_players(nfl_data)
    process.start()


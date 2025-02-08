import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging

from scraping.scraping.items import VikingItem

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class VikingsSpider(scrapy.Spider):
    name = 'vikings'
    start_urls = ['https://www.history.com/shows/vikings/cast']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=lambda driver: WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/shows/vikings/cast/"]'))
                ),
            )

    def parse(self, response):
        for character in response.css('a[href^="/shows/vikings/cast/"]'):
            actor_page = character.css('::attr(href)').get()
            character_name = character.css('.details strong::text').get()
            actor_name = character.css('.details small::text').get()
            photo = character.css('.img-container img::attr(src)').get()
            photo_url = response.urljoin(photo) if photo else None

            item = VikingItem(
                name=character_name,
                actor_name=actor_name,
                photo=photo_url,
                description='Fetching biography...'
            )

            logger.info(f'Processing vikings page :{character_name}')

            if actor_page:
                actor_url = response.urljoin(actor_page)
                yield SeleniumRequest(url=actor_url, callback=self.parse_actor, meta={'item': item})
            else:
                yield item

    def parse_actor(self, response):
        item = response.meta['item']
        description = response.css('article.main-article p::text').get()
        item['description'] = description.strip() if description else 'No description available.'
        yield item

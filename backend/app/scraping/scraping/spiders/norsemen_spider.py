import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from scraping.scraping.items import NorsemanItem

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

class NorsemenSpider(scrapy.Spider):
    name = 'norsemen'
    start_urls = ['https://www.themoviedb.org/tv/68126-vikingane/cast']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=20,
                wait_until=lambda driver: WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//li[contains(@data-order, "0")]'))
                ),
            )

    def parse(self, response):
        for character in response.xpath('//li[contains(@data-order, "0")]'):
            actor_page = character.xpath('.//a/@href').get()
            actor_name = character.xpath('.//div[@class="info"]//p/a/text()').get()
            character_name = character.xpath('.//p[@class="character"]/a/text()').get()
            photo = character.xpath('.//img[contains(@class, "profile")]/@src').get()
            photo_url = response.urljoin(photo) if photo else None

            item = NorsemanItem(
                name=character_name,
                actor_name=actor_name,
                photo=photo_url,
                description='Fetching biography...'
            )

            if actor_page:
                actor_url = response.urljoin(actor_page)
                yield SeleniumRequest(url=actor_url, callback=self.parse_actor, meta={'item': item})
            else:
                yield item

    def parse_actor(self, response):
        item = response.meta['item']
        biography = response.xpath('//div[contains(@class, "text") and contains(@class, "line-clamp-6")]//p/text()').get()
        item['description'] = biography.split('. ')[0] + '.' if biography else 'No description available.'
        yield item




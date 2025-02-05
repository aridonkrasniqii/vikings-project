import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

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

            logger.info(f'Processing norsemen page: {character_name}')
            if actor_page:
                actor_url = response.urljoin(actor_page)
                yield SeleniumRequest(url=actor_url, callback=self.parse_actor, meta={
                    'actor_name': actor_name,
                    'character_name': character_name,
                    'photo': photo_url
                })

    def parse_actor(self, response):
        biography = response.xpath(
            '//div[contains(@class, "text") and contains(@class, "line-clamp-6")]//p/text()').get()
        description = biography.split('. ')[0] + '.' if biography else 'No description available.'

        yield {
            'name': response.meta['character_name'],
            'actor': response.meta['actor_name'],
            'description': description,
            'photo': response.meta['photo']
        }



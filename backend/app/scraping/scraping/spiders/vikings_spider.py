import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum

from scraping.scraping.utils.xpaths import VikingsXPath
from scraping.scraping.items import VikingItem

class VikingsSpider(scrapy.Spider):
    name = 'vikings'
    start_urls = ['https://www.history.com/shows/vikings/cast']

    def start_requests(self):
        print("Request is starting")
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=lambda driver: WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, VikingsXPath.CAST_MEMBER))
                ),
            )

    def parse(self, response):
        for character in response.xpath(VikingsXPath.CAST_MEMBER.value):
            item = self.extract_viking_info(character, response)
            actor_page = character.xpath(VikingsXPath.ACTOR_PAGE.value).get()
            if actor_page:
                actor_url = response.urljoin(actor_page)
                yield SeleniumRequest(url=actor_url, callback=self.parse_actor, meta={'item': item})
            else:
                yield item

    def extract_viking_info(self, character, response) -> VikingItem:
        actor_raw = character.xpath(VikingsXPath.ACTOR_NAME.value).get(default='Unknown Actor')
        actor_name = actor_raw.replace("Played by ", "").strip()  # Fix: Remove extra text

        return VikingItem(
            name=character.xpath(VikingsXPath.CHARACTER_NAME.value).get(default='Unknown Character'),
            actor_name=actor_name,
            photo=response.urljoin(character.xpath(VikingsXPath.PHOTO.value).get(default='N/A')),
            description='Fetching biography...'
        )

    def parse_actor(self, response):
        item = response.meta['item']
        biography = response.xpath(VikingsXPath.DESCRIPTION.value).get(default='No description available.')
        item['description'] = biography.strip() if biography else 'No description available.'
        yield item

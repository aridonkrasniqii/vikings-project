import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from scraping.scraping.items import NorsemanItem
from scraping.scraping.utils.xpaths import NorsemanXPath

class NorsemenSpider(scrapy.Spider):
    name = 'norsemen'
    start_urls = ['https://www.themoviedb.org/tv/68126-vikingane/cast']
    collected_items = []

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=20,
                wait_until=lambda driver: WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, NorsemanXPath.CAST_MEMBER.value))
                ),
            )

    def parse(self, response):
        for character in response.xpath(NorsemanXPath.CAST_MEMBER.value):
            item = self.extract_norseman_info(character, response)

            actor_page = character.xpath(NorsemanXPath.ACTOR_PAGE.value).get(default='')
            if actor_page:
                actor_url = response.urljoin(actor_page)
                yield SeleniumRequest(url=actor_url, callback=self.parse_actor, meta={'item': item})
            else:
                yield item

    def extract_norseman_info(self, character, response) -> NorsemanItem:
        return NorsemanItem(
            name=character.xpath(NorsemanXPath.CHARACTER_NAME.value).get(default='Unknown Character'),
            actor_name=character.xpath(NorsemanXPath.ACTOR_NAME.value).get(default='Unknown Actor'),
            photo=response.urljoin(character.xpath(NorsemanXPath.PHOTO.value).get(default='N/A')) if character.xpath(
                NorsemanXPath.PHOTO.value).get() != 'N/A' else None,
            description='Fetching biography...'  # Default description, will be updated later
        )

    def parse_actor(self, response):
        item = response.meta['item']
        biography = response.xpath(NorsemanXPath.DESCRIPTION.value).get(default='No description available.')
        item['description'] = biography.split('. ')[0] + '.' if biography else 'No description available.'
        yield item

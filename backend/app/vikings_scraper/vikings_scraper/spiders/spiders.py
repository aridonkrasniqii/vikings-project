import scrapy
from celery import Celery
from scrapy_selenium import SeleniumRequest
from scrapy_splash import SplashRequest

class VikingsSpider(scrapy.Spider):
    name = 'vikings'
    start_urls = ['https://www.history.com/shows/vikings/cast']

    def parse(self, response):
        # Loop through each character link in the cast list
        for character in response.css('a[href^="/shows/vikings/cast/"]'):  # Ensure correct selection of links
            actor_page = character.css('::attr(href)').get()  # Get the href of the character's page
            character_name = character.css('.details strong::text').get()  # Get the character's name
            actor_name = character.css('.details small::text').get()  # Get the actor's name
            photo = character.css('.img-container img::attr(src)').get()  # Get the character's photo URL

            # Ensure the photo URL is absolute
            if photo:
                photo_url = response.urljoin(photo)
            else:
                photo_url = None

            # Ensure the actor's page link is valid
            if actor_page:
                actor_url = response.urljoin(actor_page)
                yield scrapy.Request(actor_url, callback=self.parse_actor, meta={
                    'actor_name': actor_name,
                    'character_name': character_name,
                    'photo': photo_url
                })

    def parse_actor(self, response):
        # Get the actor's description from the page
        description = response.css('article.main-article p::text').get()  # Extract the first paragraph description
        description = description.strip() if description else 'No description available.'

        # Yield the data with the full URL for the photo
        yield {
            'actor': response.meta['actor_name'],
            'character': response.meta['character_name'],
            'description': description,
            'photo': response.meta['photo'],  # This will now have the full URL
        }


class NorsemenSpider(scrapy.Spider):
    name = 'norsemen'
    start_urls = ['https://www.themoviedb.org/tv/68126-vikingane/cast']

    def parse(self, response):
        # Iterate through each character's card using XPath for better precision
        for character in response.xpath('//li[contains(@data-order, "0")]'):
            actor_page = character.xpath('.//a/@href').get()
            actor_name = character.xpath('.//div[@class="info"]//p/a/text()').get()
            character_name = character.xpath('.//p[@class="character"]/a/text()').get()
            photo = character.xpath('.//img[contains(@class, "profile")]/@src').get()

            if actor_page:
                actor_url = response.urljoin(actor_page)
                yield scrapy.Request(actor_url, callback=self.parse_actor, meta={
                    'actor_name': actor_name,
                    'character_name': character_name,
                    'photo': photo
                })

    def parse_actor(self, response):
        # Extract the biography using XPath
        biography = response.xpath('//div[contains(@class, "text") and contains(@class, "line-clamp-6")]//p/text()').get()

        # Get the first sentence from the biography, if available
        description = biography.split('. ')[0] + '.' if biography else 'No description available.'

        # Yield the data, including the character's name, actor's name, description, and photo URL
        yield {
            'name': response.meta['character_name'],
            'actor': response.meta['actor_name'],
            'description': description,
            'photo': response.meta['photo']
        }

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NflPlayersSpider(scrapy.Spider):
    name = 'nflplayers'
    start_urls = ['https://www.vikings.com/team/players-roster/']

    def start_requests(self):
        self.logger.info("Starting NFL players spider")
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=20,
                wait_until=lambda driver: WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'table.d3-o-table'))
                ),
                # headers={
                #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) `Chrome`/58.0.3029.110 Safari/537.36'
                # }
            )

    def parse(self, response):
        roster_table = response.css('table.d3-o-table')

        if not roster_table:
            self.logger.warning("Roster table not found!")
            return

        for player_row in roster_table.css('tbody tr'):
            player_name = player_row.css('.nfl-o-roster__player-name a::text').get()
            photo_url = player_row.css('figure a picture img::attr(src)').get()
            position = player_row.css('td:nth-child(3)::text').get()
            height = player_row.css('td:nth-child(4)::text').get()
            weight = player_row.css('td:nth-child(5)::text').get()
            age = player_row.css('td:nth-child(6)::text').get()
            experience = player_row.css('td:nth-child(7)::text').get()
            college = player_row.css('td:nth-child(8)::text').get()

            yield {
                'name': player_name.strip() if player_name else None,
                'photo_url': response.urljoin(photo_url) if photo_url else None,
                'position': position.strip() if position else None,
                'height': height.strip() if height else None,
                'weight': weight.strip() if weight else None,
                'age': int(age.strip()) if age else None,
                'experience': int(experience.strip()) if experience else None,
                'college': college.strip() if college else None,
            }

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


class NflPlayersSpider(scrapy.Spider):
    name = 'nflplayers'
    start_urls = ['https://www.vikings.com/team/players-roster/']

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=90,  # Extend wait time to ensure the page is fully loaded
                wait_until=lambda driver: WebDriverWait(driver, 90).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//section[@class="d3-l-grid--outer d3-l-section-row"]//div[@class="d3-o-table--horizontal-scroll"]/table'))
                )
            )

    def parse(self, response):
        table = response.xpath(
            '//section[@class="d3-l-grid--outer d3-l-section-row"]//div[@class="d3-o-table--horizontal-scroll"]/table')

        if table:
            for player_row in table.xpath('.//tbody/tr'):
                player_name = player_row.xpath(
                    './/td[@class="sorter-lastname"]//span[@class="nfl-o-roster__player-name"]/a/text()').get()
                player_link = player_row.xpath(
                    './/td[@class="sorter-lastname"]//figure[@class="d3-o-media-object__figure"]/a/@href').get()

                picture_sources = player_row.xpath(
                    './/td[@class="sorter-lastname"]//figure[@class="d3-o-media-object__figure"]/a/picture/source[@media]')
                if picture_sources:
                    photo_url = picture_sources[0].xpath('@srcset').get().split(', ')[0].split(' ')[0]
                else:
                    photo_url = player_row.xpath(
                        './/td[@class="sorter-lastname"]//figure[@class="d3-o-media-object__figure"]/a/picture/img/@src').get()

                position = player_row.xpath('.//td[3]/text()').get()
                age = player_row.xpath('.//td[6]/text()').get()
                experience = player_row.xpath('.//td[7]/span/text()').get()
                college = player_row.xpath('.//td[8]/text()').get()

                player_info = {
                    'name': player_name.strip() if player_name else 'N/A',
                    'photo_url': response.urljoin(photo_url) if photo_url else 'N/A',
                    'position': position.strip() if position else 'N/A',
                    'age': int(age.strip()) if age and age.strip().isdigit() else 'N/A',
                    'experience': int(experience.strip()) if experience and experience.strip().isdigit() else 'N/A',
                    'college': college.strip() if college else 'N/A',
                    'player_link': response.urljoin(player_link) if player_link else 'N/A',
                }
                logger.info(f'Processing nfl player: {player_name}')
                # Follow the player's link to get stats
                if player_link:
                    yield SeleniumRequest(
                        url=response.urljoin(player_link),
                        callback=self.parse_player_stats,
                        meta={'player_info': player_info}
                    )
                else:
                    yield player_info

        else:
            self.logger.warning("Roster table not found!")

    def parse_player_stats(self, response):
        player_info = response.meta['player_info']

        # Extract stats from the player's individual page
        player_info['stats'] = self.parse_stats(response)

        yield player_info

    def parse_stats(self, response):
        # Extract stats from the player's individual page
        stats_table = response.xpath('//div[@class="d3-l-col__col-12 nfl-t-stats--table flex-wrap"]//table/tbody/tr')

        stats = []
        for row in stats_table[:3]:  # Get only the first 3 rows
            season = row.xpath('./td[1]/text()').get()
            team = row.xpath('./td[2]/text()').get()
            games_played = row.xpath('./td[3]/text()').get()
            receptions = row.xpath('./td[4]/text()').get()
            receiving_yards = row.xpath('./td[5]/text()').get()
            receiving_touchdowns = row.xpath('./td[6]/text()').get()
            longest_reception = row.xpath('./td[7]/text()').get()

            stat = {
                'season': int(season.strip()) if season and season.strip().isdigit() else 0,
                'team': team.strip() if team else 'N/A',
                'games_played': int(games_played.strip()) if games_played and games_played.strip().isdigit() else 0,
                'receptions': int(receptions.strip()) if receptions and receptions.strip().isdigit() else 0,
                'receiving_yards': int(receiving_yards.strip()) if receiving_yards and receiving_yards.strip().isdigit() else 0,
                'receiving_touchdowns': int(receiving_touchdowns.strip()) if receiving_touchdowns and receiving_touchdowns.strip().isdigit() else 0,
                'longest_reception': int(longest_reception.strip()) if longest_reception and longest_reception.strip().isdigit() else 0,
            }
            stats.append(stat)

        return stats

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from scraping.scraping.items import NflPlayerStatsItem, NFLPlayerItem

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
                wait_time=10,
                wait_until=lambda driver: WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//section[@class="d3-l-grid--outer d3-l-section-row"]//div[@class="d3-o-table--horizontal-scroll"]/table'))
                )
            )

    def parse(self, response):
        table = response.xpath(
            '//section[@class="d3-l-grid--outer d3-l-section-row"]//div[@class="d3-o-table--horizontal-scroll"]/table')

        if table:
            for player_row in table.xpath('.//tbody/tr'):
                player_item = NFLPlayerItem(
                    name=player_row.xpath(
                        './/td[@class="sorter-lastname"]//span[@class="nfl-o-roster__player-name"]/a/text()').get(
                        default='N/A').strip(),
                    player_link=response.urljoin(player_row.xpath(
                        './/td[@class="sorter-lastname"]//figure[@class="d3-o-media-object__figure"]/a/@href').get(
                        default='')),
                    photo=response.urljoin(player_row.xpath(
                        './/td[@class="sorter-lastname"]//figure[@class="d3-o-media-object__figure"]/a/picture/img/@src').get(
                        default='N/A')),
                    position=player_row.xpath('.//td[3]/text()').get(default='N/A').strip(),
                    age=int(player_row.xpath('.//td[6]/text()').get(default='0')),
                    experience=int(player_row.xpath('.//td[7]/span/text()').get(default='0')),
                    college=player_row.xpath('.//td[8]/text()').get(default='N/A').strip()
                )

                logger.info(f'Processing nfl player: {player_item["name"]}')
                if player_item['player_link']:
                    yield SeleniumRequest(
                        url=player_item['player_link'],
                        callback=self.parse_player_stats,
                        meta={'player_item': player_item}
                    )
                else:
                    yield player_item

        else:
            self.logger.warning("Roster table not found!")

    def parse_player_stats(self, response):
        player_item = response.meta['player_item']
        player_item['stats'] = self.parse_stats(response)
        yield player_item

    def parse_stats(self, response):
        stats_table = response.xpath('//div[@class="d3-l-col__col-12 nfl-t-stats--table flex-wrap"]//table/tbody/tr')

        stats = []
        for row in stats_table[:3]:
            stats.append(NflPlayerStatsItem(
                player_name=response.meta['player_item']['name'],
                season=int(row.xpath('./td[1]/text()').get(default='0')),
                team=row.xpath('./td[2]/text()').get(default='N/A').strip(),
                games_played=int(row.xpath('./td[3]/text()').get(default='0')),
                receptions=int(row.xpath('./td[4]/text()').get(default='0')),
                receiving_yards=int(row.xpath('./td[5]/text()').get(default='0')),
                receiving_touchdowns=int(row.xpath('./td[6]/text()').get(default='0')),
                longest_reception=int(row.xpath('./td[7]/text()').get(default='0'))
            ))
        return stats

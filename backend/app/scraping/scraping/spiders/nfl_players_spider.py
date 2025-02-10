import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraping.scraping.items import NflPlayerStatsItem, NFLPlayerItem
from scraping.scraping.utils.xpaths import NflXPath

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
                    EC.presence_of_element_located((By.XPATH, NflXPath.PLAYER_TABLE.value)) and
                    EC.attribute_to_be((By.CSS_SELECTOR, 'picture'), 'is-loaded', 'true')
                )
            )

    def parse(self, response):
        table = response.xpath(NflXPath.PLAYER_TABLE.value)

        if not table:
            self.logger.warning("Roster table not found!")
            return

        for player_row in table.xpath(NflXPath.PLAYER_ROW.value):
            player_item = self.extract_player_info(player_row, response)

            player_link = player_item.get('player_link')
            if player_link:
                yield SeleniumRequest(
                    url=player_link,
                    callback=self.parse_player_stats,
                    meta={'player_item': player_item},
                    wait_until=lambda driver: WebDriverWait(driver, 10).until(
                        EC.attribute_to_be((By.CSS_SELECTOR, 'picture'), 'is-loaded', 'true')
                    )
                )
            else:
                yield player_item

    def extract_player_info(self, player_row, response) -> NFLPlayerItem:
        player_item = NFLPlayerItem(
            name=player_row.xpath(NflXPath.PLAYER_NAME.value).get(default='N/A').strip(),
            photo=response.urljoin(player_row.xpath(NflXPath.PLAYER_PHOTO.value).get(default='https://www.generationsforpeace.org/en/how-we-work/publications/empty/')),
            position=player_row.xpath(NflXPath.PLAYER_POSITION.value).get(default='N/A').strip(),
            age=int(player_row.xpath(NflXPath.PLAYER_AGE.value).get(default='0')),
            experience=int(player_row.xpath(NflXPath.PLAYER_EXPERIENCE.value).get(default='0')),
            college=player_row.xpath(NflXPath.PLAYER_COLLEGE.value).get(default='N/A').strip(),
            number=int(player_row.xpath(NflXPath.PLAYER_NUMBER.value).get(default='0')),
            stats=[],
            player_link=response.urljoin(player_row.xpath(NflXPath.PLAYER_LINK.value).get(default=''))
        )
        return player_item

    def parse_player_stats(self, response):
        player_item = response.meta['player_item']
        player_item['stats'] = self.extract_stats(response)
        yield player_item

    def extract_stats(self, response) -> list:
        stats_table = response.xpath(f"({NflXPath.STATS_TABLE.value})")

        stats = []
        for row in stats_table[:3]:
            stats.append(NflPlayerStatsItem(
                season=self.to_float(row.xpath(NflXPath.STATS_SEASON.value).get(default='0')),
                team=row.xpath(NflXPath.STATS_TEAM.value).get(default='N/A').strip(),
                games_played=self.to_float(row.xpath(NflXPath.STATS_GAMES_PLAYED.value).get(default='0')),
                receptions=self.to_float(row.xpath(NflXPath.STATS_RECEPTIONS.value).get(default='0')),
                receiving_yards=self.to_float(row.xpath(NflXPath.STATS_RECEIVING_YARDS.value).get(default='0')),
                receiving_touchdowns=self.to_float(row.xpath(NflXPath.STATS_RECEIVING_TOUCHDOWNS.value).get(default='0')),
                longest_reception=self.to_float(row.xpath(NflXPath.STATS_LONGEST_RECEPTION.value).get(default='0'))
            ))
        return stats

    def to_float(self, value: str) -> float:
        try:
            return float(value)
        except ValueError:
            return 0.0

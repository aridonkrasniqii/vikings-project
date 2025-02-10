from enum import Enum

class NflXPath(Enum):
    PLAYER_TABLE = '//section[@class="d3-l-grid--outer d3-l-section-row"]//div[@class="d3-o-table--horizontal-scroll"]/table'
    PLAYER_ROW = './/tbody/tr'

    PLAYER_NAME = './/td[@class="sorter-lastname"]//span[@class="nfl-o-roster__player-name"]/a/text()'
    PLAYER_LINK = './/td[@class="sorter-lastname"]//figure[@class="d3-o-media-object__figure"]/a/@href'
    PLAYER_PHOTO = './/td[@class="sorter-lastname"]//figure[@class="d3-o-media-object__figure"]/a/picture/img/@src'
    PLAYER_NUMBER = './/td[2]/text()'
    PLAYER_POSITION = './/td[3]/text()'
    PLAYER_AGE = './/td[6]/text()'
    PLAYER_EXPERIENCE = './/td[7]/span/text()'
    PLAYER_COLLEGE = './/td[8]/text()'

    STATS_TABLE = '(//div[@class="d3-l-col__col-12 nfl-t-stats--table flex-wrap"]//table/tbody/tr)[2]'
    STATS_SEASON = './td[1]/text()'
    STATS_TEAM = './td[2]/text()'
    STATS_GAMES_PLAYED = './td[3]/text()'
    STATS_RECEPTIONS = './td[4]/text()'
    STATS_RECEIVING_YARDS = './td[5]/text()'
    STATS_RECEIVING_TOUCHDOWNS = './td[6]/text()'
    STATS_LONGEST_RECEPTION = './td[7]/text()'

class NorsemanXPath(Enum):
    CAST_MEMBER = '//li[contains(@data-order, "0")]'
    ACTOR_PAGE = './/a/@href'
    ACTOR_NAME = './/div[@class="info"]//p/a/text()'
    CHARACTER_NAME = './/p[@class="character"]/a/text()'
    PHOTO = './/img[contains(@class, "profile")]/@src'
    DESCRIPTION = '//div[contains(@class, "text") and contains(@class, "line-clamp-6")]//p/text()'

class VikingsXPath(Enum):
    CAST_MEMBER = '//a[starts-with(@href, "/shows/vikings/cast/")]'
    ACTOR_PAGE = './/@href'
    CHARACTER_NAME = './/div[@class="details"]//strong/text()'
    ACTOR_NAME = './/div[@class="details"]//small/text()'
    PHOTO = './/div[@class="img-container"]//img/@src'
    DESCRIPTION = '//article[contains(@class, "main-article")]//p/text()'

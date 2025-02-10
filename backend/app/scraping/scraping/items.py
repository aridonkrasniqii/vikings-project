import scrapy

class VikingItem(scrapy.Item):
    name = scrapy.Field()
    actor_name = scrapy.Field()
    description = scrapy.Field()
    photo = scrapy.Field()

class NorsemanItem(scrapy.Item):
    name = scrapy.Field()
    actor_name = scrapy.Field()
    description = scrapy.Field()
    photo = scrapy.Field()

class NFLPlayerItem(scrapy.Item):
    name = scrapy.Field()
    number = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    experience = scrapy.Field()  # Years in the NFL
    college = scrapy.Field()
    photo = scrapy.Field()
    stats = scrapy.Field()
    player_link = scrapy.Field()

class NflPlayerStatsItem(scrapy.Item):
    season = scrapy.Field()
    team = scrapy.Field()
    games_played = scrapy.Field()
    receptions = scrapy.Field()
    receiving_yards = scrapy.Field()
    receiving_touchdowns = scrapy.Field()
    longest_reception = scrapy.Field()

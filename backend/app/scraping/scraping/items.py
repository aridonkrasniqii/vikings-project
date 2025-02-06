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

class NflPlayerStatsItem(scrapy.Item):
    player_name = scrapy.Field()
    season = scrapy.Field()  # Season year
    team = scrapy.Field()  # Team for the season
    games_played = scrapy.Field()  # Total games played
    receptions = scrapy.Field()  # Total receptions
    receiving_yards = scrapy.Field()  # Total receiving yards
    receiving_touchdowns = scrapy.Field()  # Receiving touchdowns
    longest_reception = scrapy.Field()  # Longest reception in yards

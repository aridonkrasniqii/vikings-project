import scrapy

class VikingItem(scrapy.Item):
    name = scrapy.Field()
    actor = scrapy.Field()
    description = scrapy.Field()
    photo = scrapy.Field()

class NorsemenItem(scrapy.Item):
    name = scrapy.Field()
    actor = scrapy.Field()
    description = scrapy.Field()
    photo = scrapy.Field()

class NFLPlayerItem(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    stats = scrapy.Field()
    photo = scrapy.Field()

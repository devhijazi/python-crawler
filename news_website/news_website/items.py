import scrapy


class NewsWebsiteItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    thumbnail = scrapy.Field()
    author = scrapy.Field()

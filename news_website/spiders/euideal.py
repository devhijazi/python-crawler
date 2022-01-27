import scrapy

from news_website.items import NewsWebsiteItem


class EuidealSpider(scrapy.Spider):
    name = 'euideal'
    allowed_domains = ['https://www.euideal.com/']
    start_urls = ['https://www.euideal.com/']

    def parse(self, response):
        for article in response.css("article"):
            link = article.css("a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        link = response.url
        title = response.css("div.main-post h2 a::attr(title)").extract_first()
        text = "".join(response.css("div.main-post p span").extract())

        notice = NewsWebsiteItem(title=title, text=text, link=link)

        yield notice

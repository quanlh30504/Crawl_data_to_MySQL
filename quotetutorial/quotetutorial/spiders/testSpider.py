import scrapy
from ..items import QuotetutorialItem

class testSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self,response):
        books = response.css(".quote")
        items = QuotetutorialItem()
        for book in books:
            items["title"]= book.css(".text::text").get()
            items["author"] = book.css(".author::text").get()
            items["tags"] = book.css(".tag::text").extract()

            yield items

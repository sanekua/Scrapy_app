import scrapy


def parse(self, response):
    items = PhonesItem()
    all_items = response.css('div.s-item-container')

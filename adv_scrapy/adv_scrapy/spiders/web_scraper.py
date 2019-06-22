import scrapy


def parse(self, response):
    items = PhonesItem()
    all_items = response.css('div.s-item-container')


    for respons in all_items:
        product_name = respons.css('.s-access-title').css('::text').extract()
        product_corp = respons.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
        items['product_price'] = (re.search(r'\d+', str(product_price)).group(0)).split()
        items['product_image'] = product_image
        yield items
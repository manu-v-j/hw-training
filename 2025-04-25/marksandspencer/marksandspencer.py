import requests
from parsel import Selector

class Markandspencer:
    def __init__(self):
        self.url='https://www.marksandspencer.com/l/women/dresses'

    def parser(self):
        response=requests.get(self.url)
        selector=Selector(response.text)
        products=selector.xpath('//div[@class="product-card_rootBox__BcM9P"]')
        category=selector.xpath('//label[contains(@class, "media-0") and contains(@for, "subcategory")]/text()').getall()
        pagination_link = selector.xpath('//a[@class="pagination_trigger__YEwyN"]/@href').get()
        print(f'Total categories found: {category}')
        print(f"pagination_link:{pagination_link}")

        for product in products:
            product_url=product.xpath('.//a[@class="product-card_cardWrapper__GVSTY"]/@href').get()
            product_url='https://www.marksandspencer.com'+product_url
            content=self.properties(product_url)


    def properties(self,content):
        response=requests.get(content)
        selector=Selector(response.text)

        unique_id=selector.xpath('//div[contains(@class,"pdp-template")]/p/text()[2]').get()
        brand_name = selector.xpath('//div[contains(@class, "product-intro_left")]//p[contains(@class, "brand-title_title")]/text()').get()
        product_name=selector.xpath('//div[@class="product-intro_slot__MH6jv"]/h1/text()').get()
        selling_price=selector.xpath('//div[contains(@class,"product-intro_priceWrapper")]/p/text()').get()
        print(unique_id,brand_name,product_name,selling_price)

obj=Markandspencer()

obj.parser()    
import scrapy
from .parse import parse_products  

class LidlSpider(scrapy.Spider):
    name = "Lidl"
    allowed_domains = ["sortiment.lidl.ch"]
    start_urls = ["https://sortiment.lidl.ch/de/alle-kategorien?manufacturer=Qualit%C3%A9+Suisse#/"]

    def parse(self, response):
        products = response.xpath("//div[@class='product-item-info']")
        for product in products:
            product_url = product.xpath(".//a/@href").get()
            yield response.follow(product_url, callback=self.parse_product)

    def parse_product(self, response): 
        product_data = parse_products(response)  
        if product_data:
            yield product_data

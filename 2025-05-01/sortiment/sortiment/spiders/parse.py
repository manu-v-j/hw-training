import re

def parse_products(response):
    unique_id = response.xpath("//p[@class='sku text-gray']/text()").get()
    if unique_id:  # Ensure unique_id is found before using regex
        unique_id = re.search(r'\d+', unique_id).group()

    return {
        "unique_id": unique_id,
        "product_name": response.xpath("//span[@class='base']//text()").get(),
        "price": response.xpath("//strong[@class='pricefield__price']/@content").get(),
        "description": response.xpath("//div[@class='col-left']/p[2]/font/font/text()").get()  # Fixed typo 'xpth' -> 'xpath'
    }

import requests
from parsel import Selector
import re

def parser(url):
    response = requests.get(url)
    selector = Selector(response.text)

    unique_id = selector.xpath("//p[@class='sku text-gray']/text()").get()
    if unique_id:
        match = re.search(r'\d+', unique_id)
        unique_id = match.group() if match else None
    product_name=selector.xpath("//span[@class='base']//text()").get().strip()
    price=selector.xpath("//strong[@class='pricefield__price']/@content").get()
    image_url=selector.xpath("//img[@class='gallery-placeholder__image']/@src").getall()
    currency=selector.xpath("//span[contains(@class,'price-currency')]/text()").get()
    reviews=selector.xpath("//a[@class='action view']/span[1]//text()").get()
    breadcrumps=[b.strip() for b in selector.xpath("//div[@class='breadcrumbs']/ul/li//text()").getall() if b.strip()]
    description=" ".join(selector.xpath("//div[@class='col-left']/p[2]//text()").getall()).strip()

    return {
        "Unique_id": unique_id,
        "Product_name":product_name ,
        "Price": price,
        "Image_url" : image_url,
        "Currency":currency,
        "Reviews":reviews,
        "Breadcrumps":breadcrumps ,
        "description": description
    }

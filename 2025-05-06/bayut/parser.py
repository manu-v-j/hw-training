from parsel import Selector
import requests
from urllib.parse import urljoin


def parser(full_url,header):
    response=requests.get(full_url,headers=header)
    selector=Selector(response.text)
    price=selector.xpath("//span[@class='_2d107f6e']/text()").get()
    currency=selector.xpath("//span[@class='d241f2ab']/text()").get()
    property_id=selector.xpath("//span[@class='_2fdf7fc5' and @aria-label='Reference']/text()").get()
    type=selector.xpath("//span[@class='_2fdf7fc5' and @aria-label='Type']/text()").get()
    status=selector.xpath("//span[@class='_2fdf7fc5' and @aria-label='Completion status']/text()").get()
    furnishing=selector.xpath("//span[@class='_2fdf7fc5' and @aria-label='Furnishing']/text()").get()
    purpose=selector.xpath("//span[@class='_2fdf7bedfc5' and @aria-label='Purpose']/text()").get()
    beds=selector.xpath("//span[@class='_783ab618' and @aria-label='Beds']/span/text()").get()
    baths=selector.xpath("//span[@class='_783ab618' and @aria-label='Baths']/span/text()").get()
    square_feet=selector.xpath("//span[@class='_783ab618' and @aria-label='Area']/span/span/text()").get()
    location=selector.xpath("//div[@class='e4fd45f0']/text()").get()
    agent=selector.xpath("//a[@class='_10501224']/h2/text()").get()
    images=selector.xpath("//picture[@class='a659dd2e']/img/@src").get()

    print(furnishing)


    

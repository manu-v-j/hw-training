import requests
from parsel import Selector
import logging
logging.basicConfig(level=logging.INFO)
headers={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'none',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1'
}

###########################################CRAWLER##############################################
url='https://www.mylittlesalesman.com/trucks-for-sale-i2c0f0m0?ptid=1'

while url:
    response=requests.get(url,headers=headers)
    print(url)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//div[@class='col-12 col-xl-3 c5g pri']/a/@href").getall()
    for product in product_urls:
        full_url=f'https://www.mylittlesalesman.com{product}'
        # print(full_url)
    next_page=sel.xpath("//li[@class='page-item pagination-next']/a/@href").get()
    if next_page:
        url=f'https://www.mylittlesalesman.com{next_page}'
    else:
        break   


########################################PARSER#################################################
url='https://www.mylittlesalesman.com/2023-caterpillar-259d3-tracked-skid-steer-12171941'
response=requests.get(url,headers=headers)
if response.status_code==200:
    sel=Selector(text=response.text)
    price=sel.xpath("//span[@class='b text-darkred']/text()").get()
    description=sel.xpath("//h2[contains(text(),'Product Description')]/following-sibling::div/text()").getall()
    rows=sel.xpath("//h2[contains(text(),'Product Specifications')]/following-sibling:: table//tr")
    specifications={}
    for row in rows:
        key = row.xpath("./th/text()").get()
        value = row.xpath("./td//text()").get()
        specifications[key]=value
    images=sel.xpath("//a[@data-fancybox='gallery']/@href").getall()
    location=sel.xpath("//h2[@class='h6 pb0']/text()").get()
    contact_info=sel.xpath("//a[@id='ctl00_ctl00_mc_mc_hypPhone']/@data-mls-tel").get()
    logging.info(contact_info)

import requests
from parsel import Selector
import logging
import re
logging.basicConfig(level=logging.INFO)
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?1',
    'sec-ch-ua-platform':'Android',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
}

#################################CRAWLER#########################################################
page=1
product_url=[]
while True:
    url=f"https://www2.hm.com/en_in/women/shop-by-product/tops.html?productTypes=Top&page={page}"
    response=requests.get(url,headers=headers)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[@class='afcaaf']/@href").getall()
    if not product_urls:
        break
    for url in product_urls:
        product_url.append(url)
    page+=1
print(len(product_url))

##################################PARSER########################################################
# url="https://www2.hm.com/en_in/productpage.1293219004.html"
# response=requests.get(url,headers=headers)
# sel=Selector(text=response.text)
# product_name=sel.xpath("//h1[@class='fe9348 bdb3fa d582fb']/text()").get()
# regular_price_raw=sel.xpath("//span[@class='e70f50 d7cab8 d9ca8b']/text()").get()
# regular_price=regular_price_raw.replace('Rs.','')
# if regular_price:
#     regular_price=regular_price.strip()
# currency=re.search(r'Rs',regular_price_raw).group()
# product_description=sel.xpath("//p[@class='e95b5c f8c1e9 e2b79d']/text()").get()
# pdp_url=url
# size=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Size')]/following-sibling::dd/text()").getall()
# clothing_length=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Length: ')]/following-sibling::dd/text()").get()
# clothing_fit=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Fit: ')]/following-sibling::dd/text()").get()
# style=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Style: ')]/following-sibling::dd/text()").get()
# neck_style=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Neckline: ')]/following-sibling::dd/text()").get()
# country_of_origin=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Neckline: ')]/following-sibling::dd/text()").get()
# manufacturer_address=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Manufactured by: ')]/following-sibling::dd/text()").get()
# importer_address=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Marketed or imported by: ')]/following-sibling::dd/text()").get()
# material_composition=sel.xpath("//li[@class='d9d00c']/span/text()").get()
# material=sel.xpath("//div[@class='ecc0f3']/dt[contains(text(), 'Material: ')]/following-sibling::dd/text()").get()
# care_instructions=sel.xpath("//li[@class='e16073 fdbaf2']/text()").getall()
# image_url=sel.xpath("//div[@class='def5f0 fcc68c a33b36 f6e252']/span/img/@src").getall()

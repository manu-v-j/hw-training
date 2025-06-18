import requests
from parsel import Selector
import re
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'sec-ch-ua':'?1',
    'sec-ch-ua-platform':'Android',
    'sec-fetch-mode':'navigate',
    'sec-fetch-user':'?1',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
}
##############################CRAWLER##############################

# count=0
# url="https://www.almayaonline.com/soft-drink-and-juices"
# while True:
#     response=requests.get(url,headers=headers)
#     sel=Selector(text=response.text)
#     product_urls=sel.xpath("//h2[@class='product-title']/a/@href").getall()
#     for product in product_urls:
#         url=f"https://www.almayaonline.com{product}"
#         print(url)
#         count+=1
#         print(count)
#     next_page=sel.xpath("//li[@class='next-page']/a/@href").get()
#     if next_page:
#         url=next_page
#     else:
#         break

###############################PARSER##############################
url="https://www.almayaonline.com/7up-free-soft-drink-can-6x330ml"
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//div[contains(@class,'product-name')]/h1/text()").get()
grammage_quantity=re.search(r'\d+x\d+',product_name).group()
grammage_unit=re.search(r'(kg|g|ml|l)',product_name).group()
price_raw=sel.xpath("//div[@class='product-price']/span/text()").get()
regular_price=re.search("AED",price_raw).group()
currency=re.search(r'\d+\.\d+',price_raw).group()
product_decsription=sel.xpath("//div[@class='full-description']/text()").get()
image_url=sel.xpath("//div[@class='picture']/img/@src").get()
print(image_url)
import requests
from parsel import Selector
import re
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'referer':'https://justforpets.co.uk/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'sec-ch-ua-mobile',
    'sec-fetch-dest':'document',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
}
##############################CRAWLER##############################

# url="https://justforpets.co.uk/dogs/"
# count=0
# while True:
#     response=requests.get(url,headers=headers)
#     sel=Selector(text=response.text)
#     products_url=sel.xpath("//figure[@class='card-figure']/a/@href").getall()
#     for product in products_url:
#         print(product)
#         count+=1
#         print(count)
#     next_page=sel.xpath("//li[@class='pagination-item pagination-item--next']/a/@href").get()
#     if next_page:
#         url=next_page
#     else:
#         break

###############################PARSER##############################
url="https://justforpets.co.uk/canagan-dog-game-400g/"
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//h1[@class='productView-title']/text()").get()
grammage_quantity=re.search(r'\d+',product_name).group()
grammage_unit=re.search(r'(kg|g|ml|l)',product_name).group()
regular_price_raw=sel.xpath("//span[@class='price price--withTax']/text()").get()
regular_price=re.search(r'\d+\.\d+',regular_price_raw).group()
currency=re.search(r'£',regular_price_raw).group()
pdp_url=url
image_url=sel.xpath("//div[@class='productView-img-container']/a/img/@src").get()
breadcrumb=sel.xpath("//a[@class='breadcrumb-label']/span/text()").getall()
producthierarchy_level1=breadcrumb[0]
producthierarchy_level2=breadcrumb[1]
producthierarchy_level3=breadcrumb[2]
producthierarchy_level4=breadcrumb[3]
producthierarchy_level5=breadcrumb[4]
product_description=sel.xpath("//div[@class='tab-content has-jsContent is-active']/text()[2]").get().strip()
ingredients=sel.xpath("//div[@class='tab-content has-jsContent']/text()[2]").get().strip()
rating=sel.xpath("//span[@class='jdgm-prev-badge__stars']/@data-score").get()

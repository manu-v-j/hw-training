import requests
from parsel import Selector
import json
import re
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'connection':'keep-alive',
    'referer':'https://www.hoogvliet.com/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

################################CRAWLER############################################
page=1
count=0
while True:
    url=f'https://navigator-group1.tweakwise.com/navigation/ed681b01?tn_q=&tn_p={page}&tn_ps=16&tn_sort=Relevantie&tn_profilekey=fJLU4uH7kLxf4omMWx974frxbwC0qhWsY4FV8S0HluLIkg==&tn_cid=999999-10003&CatalogPermalink=producten&CategoryPermalink=aardappelen-groente-fruit&format=json&tn_parameters=ae-productorrecipe%3Dproduct'
    
    response=requests.post(url,headers=headers)
    data = response.json()
    item_list=data.get('items',[])
    if not item_list:
        break
    for item in item_list:
        product_url=item.get('url','')
        print(product_url)
        count+=1
        print(count)
    page+=1


######################################PARSER##################################
# with open('/home/user/Hashwave/2025-07-16/product_link.json','r') as f:
#         product_list = json.load(f)
#         for url in product_list:
#             response=requests.get(url,headers=headers)
#             if response.status_code==200:
#                 sel=Selector(text=response.text)
#                 product_name=sel.xpath("//div[@class='product-info']//h1/text()").get()
#                 grammage_quantity_raw=sel.xpath("//div[@class='ratio-base-packing-unit']/span//text()").get()
#                 if grammage_quantity_raw:
#                     grammage_quantity=re.sub(r'\s\w+','',grammage_quantity_raw)
#                     grammage_unit=re.sub(r'\d+','',grammage_quantity_raw).strip()
#                 ingredients=sel.xpath("//h3[contains(text(), 'Ingredi')]/ancestor::div[@class='accordion-item open']//div[@class='accordion-content']/p/text()").get()
#                 storage_instructions = sel.xpath("//h3[contains(text(), 'Bewaar en/of gebruiksadvies')]/ancestor::div[@class='accordion-item']//div[@class='accordion-content']/p/text()").get()
#                 country_of_origin=sel.xpath("//h3[contains(text(), 'Land van herkomst:')]/ancestor::div[@class='accordion-item']//div[@class='accordion-content']/p/text()").get()
#                 distributor_address=sel.xpath("//h3[contains(text(), 'Leverancier:')]/ancestor::div[@class='accordion-item']//div[@class='accordion-content']/p/text()").get()
#                 nutritions={}
#                 rows=sel.xpath("//div[@class='accordion-content nutritional-info']//tr")
#                 for row in rows:
#                     label = row.xpath(".//td[1]/text()").get().strip()
#                     value = row.xpath(".//td[2]/text()").get().strip()
#                     nutritions[label]=value
#                 image_url=sel.xpath("//div[@class='product-image-container']/img/@src").get()
#                 breadcrumbs_raw=sel.xpath("//li[contains(@class,'breadcrumbs-list')]//text()").getall()
#                 breadcrumbs = [item.strip() for item in breadcrumbs_raw if item.strip() and item.strip() != '/']



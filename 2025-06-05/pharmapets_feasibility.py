import requests
from parsel import Selector
import re

headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'priority':'u=0,i',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-user':'?1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

##############################CRAWLER##############################

# count=0
# category_list= ["Dog Dry","Dog Wet","Dog Snack","Cat Dry"]
# for category in category_list:
#     page=1
#     while True:
#         url = f"https://www.pharmapets.nl/catalogsearch/result/?p={page}&q={category.replace(' ', '+')}"

#         response=requests.get(url,headers=headers)
#         sel=Selector(text=response.text)
#         product_urls=sel.xpath("//a[@class='product-item-link']/@href").getall()
#         if not product_urls:
#             break
#         for url in product_urls:
#             print(url)
#             count+=1
#             print(count)
    
#         page+=1

###############################PARSER##############################

response=requests.get('https://www.pharmapets.nl/60g-barouf-kat-cat-love-mix.html',headers=headers)
sel=Selector(text=response.text)
unique_id=sel.xpath("//td[@data-th='Tom & Co sku']/text()").get()
product_name=sel.xpath("//span[@class='base']//text()").get()
brand=sel.xpath("//td[@data-th='Merk']/text()").get()
grammage_quantity=(re.search('(\d+)',product_name)).group(1)
grammage_unit=(re.search(r'(kg|g|ml|l)',product_name)).group(1)
selling_price=sel.xpath("//meta[@itemprop='price']/@content").get()
price_was=sel.xpath("//span[@data-price-type='oldPrice']/@data-price-amount").get()
percentage_discount=re.search(r'(\d+%)',sel.xpath("//span[@class='promo-percentage']//text()").get()).group(1)
currency=sel.xpath("//meta[@itemprop='priceCurrency']/@content").get()
breadcrumb=sel.xpath("//div[@class='breadcrumbs breadcrumbs-mobile--compact']/ul/li//text()").getall()
breadcrumb = [b.strip() for b in breadcrumb if b.strip()]
product_description=sel.xpath("//div[@class='value reset-pagebuilder']/p//text()").getall()
ingredients=sel.xpath("//div[@class='pagebuilder-accordion__content']//p[1]/text()").get()
nutritional_information=sel.xpath("//div[@class='pagebuilder-accordion__content']//p[2]/text()").get()
product_unique_key=sel.xpath("//td[@data-th='SKU']/text()").get()
image_url=sel.xpath("//img[@class='gallery-placeholder__image']/@src").get()
features=sel.xpath("//div[@class='block-content is-paws-list']/ul/li/text()").getall()
print(grammage_unit)
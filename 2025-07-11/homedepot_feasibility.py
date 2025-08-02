from curl_cffi import requests
from parsel import Selector
import logging
logging.basicConfig(level=logging.INFO)
import json

headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'referer':'https://www.homedepot.com/',
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

###################CATEGORY###############################################

final_category_urls = []
visited = set()

def explore_category(url):
    if url in visited:
        return
    visited.add(url)

    try:
        print(f"[DEBUG] Exploring: {url}")
        response = requests.get(url, headers=headers)
        sel = Selector(text=response.text)

        product_links = sel.xpath("//a[@class='sui-top-0 sui-left-0 sui-absolute sui-size-full sui-z-10']/@href").getall()
        if product_links:
            final_category_urls.append(url)
            return 

        subcategories = sel.xpath("//li[contains(@class, 'side-navigation__li')]//a/@href").getall()
        subcategories = [f"https://www.homedepot.com{sub}" if sub.startswith('/') else sub for sub in subcategories]

        for sub_url in subcategories:
            explore_category(sub_url)

    except Exception as e:
        print(f"Error on {url}: {e}")

start_url = 'https://www.homedepot.com/b/Appliances/N-5yc1vZbv1w'
explore_category(start_url)

for url in final_category_urls:
    print(url)

#############################CRAWLER#######################################
# page=0
# count=0
# product_url=[]
# while True:
#     url = f'https://www.homedepot.com/b/Appliances-Dishwashers/N-5yc1vZc3po?catStyle=ShowProducts&Nao={page}'
#     response = requests.get(url, headers=headers)
  
#     sel = Selector(text=response.text)
#     product_urls = sel.xpath("//a[@class='sui-top-0 sui-left-0 sui-absolute sui-size-full sui-z-10']/@href").getall()
#     if not product_urls:
#         print("No more products found.")
#         break

#     for product in product_urls:
#         full_url = f"https://www.homedepot.com{product}"
#         product_url.append(full_url)
#         # count += 1
#         # print(count, full_url)
#         print(len(product_url))

#     page += 24


###########################PARSER########################################

# for url in product_url:
#
#     product_name=sel.xpath("//h1[contains(@class,'sui-h4-bold')]/text()").get()
#     selling_price=sel.xpath("//span[@class='sui-font-display sui-leading-none sui-px-[2px] sui-text-9xl sui--translate-y-[0.5rem]']/text()").get()
#     price_was_raw=sel.xpath("//span[@class='sui-line-through']//text()").get()
#     price_was=price_was_raw.replace('$','')
#     currency=sel.xpath("//span[@class='sui-font-display sui-leading-none sui-text-3xl']/text()").get()
#     percentage_discount=sel.xpath("//span[@class='sui-text-success']/div/span/text()[2]").get()
#     script=sel.xpath("//script[@id='thd-helmet__script--productStructureData']/text()").get()
#     data=json.loads(script)
#     product_description=data.get('description','')
#     unique_id=data.get('productID','')
#     product_sku=data.get('sku','')
#     brand=data.get('brand',{}).get('name','')
#     rating=data.get('aggregateRating',{}).get('ratingValue','')
#     review=data.get('aggregateRating',{}).get('reviewCount','')
#     color=data.get('color','')
#     model_number=data.get('model','')
#     depth=data.get('depth','')
#     height=data.get('height','')
#     width=data.get('width','')
#     weight=data.get('weight','')
#     image_url=data.get('image',[])
#     print(product_name)

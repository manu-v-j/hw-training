import requests
from parsel import Selector
import re
import json
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'referer':'https://noragardner.com/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

##############################CRAWLER##############################
url = "https://noragardner.com/collections/dresses"

while url:
    response = requests.get(url, headers=headers)
    sel = Selector(text=response.text)

    product_urls = sel.xpath("//a[contains(@class, 'grid-product__link')]/@href").getall()
    for product_url in product_urls:
        full_url = f"https://noragardner.com{product_url}"
        print(full_url)

    next_page = sel.xpath("//link[@rel='next']/@href").get()
    next_page=f"https://noragardner.com{next_page}"
    if next_page:
        url = next_page
    else:
        break


###############################PARSER##############################
url="https://noragardner.com/collections/dresses/products/donna-dress-teal"
review_url="https://fast.a.klaviyo.com/reviews/api/client_reviews/6577894293598/"

payload = {
    "product_id": "6577894293598",
    "company_id": "HWxMF4",
    "limit": 5,
    "offset": 0,
    "sort": 3,
    "filter": "",
    "type": "reviews",
    "media": "false",
    "kl_review_uuid": "",
    "preferred_country": "US",
    "tz": "Asia/Calcutta"
}
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)

url=url
product_name=sel.xpath("//h1[@class='h2 product-single__title']/text()").get()
sales_price_raw=sel.xpath("//span[@class='product__price']/text()").get()
sales_price=re.search(r'\d+',sales_price_raw).group()
script=sel.xpath("//script[@ type='application/ld+json'][2]/text()").get()
data=json.loads(script)
product_sku=data.get('sku','')
brand=data.get("brand",{}).get('name','')

response=requests.get(review_url,params=payload,headers=headers)

data=response.json()
reviews_list=data.get("reviews",[])
total_number_of_reviews=reviews_list[0].get('product',{}).get('review_count','')
star_rating=reviews_list[0].get('product',{}).get('star_rating','')
for item in reviews_list:
    review_title=item.get('title','')
    review_text=item.get('content','')
print(star_rating)

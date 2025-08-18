import requests
from parsel import Selector
import json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'downlink': '10',
    'dpr': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.walmart.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}

###################################CRAWLER#################################
# response=requests.get("https://www.walmart.com/shop/savings?povid=GlobalNav_rWeb_Savings_ShopAll",headers=headers)
# sel=Selector(text=response.text)
# product_urls=sel.xpath("//a[contains(@class,'hide-sibling-opacity')]/@href").getall()
# for url in product_urls:
#     full_url=f'https://www.walmart.com{url}'
#     print(full_url)

####################################PARSER##################################
base_url="https://www.walmart.com/ip/Astercook-6-Piece-Flower-Kitchen-Knife-Set-German-High-Carbon-Stainless-Steel-Knives-Sets-6-Blade-Guards-Dishwasher-Safe-Perfect-Gifts-Kitchen/9697054720?classType=VARIANT&athbdg=L1600"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//h1[@class='lh-copy dark-gray mv1 f4 mh0 b']/text()").get()
selling_price=sel.xpath("//span[@class='inline-flex flex-column']/span/text()").get()
regular_price=sel.xpath("//span[contains(@class,'nearer-mid-gray')]/text()").get()
color=sel.xpath("//span[@class='ml1']/text()").get()
brand=sel.xpath("//a[contains(@data-seo-id,'brand-name')]/text()").get()
script_text=sel.xpath("//script[@data-seo-id='schema-org-product']//text()").get()
# data=json.loads(script_text)
# product_description=data.get('description','')
script=sel.xpath("//script[@id='__NEXT_DATA__']/text()").get()
item=json.loads(script)
specification={}
keys=item.get('props',{}).get('pageProps',{}).get('initialData',{}).get('data',{}).get('idml',{}).get('specifications',[])
for item in keys:
    key=item.get('name','')
    value=item.get('value','')
    specification[key]=value
print(brand)
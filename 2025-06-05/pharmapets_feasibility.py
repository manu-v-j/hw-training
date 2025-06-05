import requests
from parsel import Selector

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
selling_price=sel.xpath("//meta[@itemprop='price']/@content").get()
price_was=sel.xpath("//span[@data-price-type='oldPrice']/@data-price-amount").get()
print(price_was)
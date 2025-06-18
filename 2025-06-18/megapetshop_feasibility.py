import requests
from parsel import Selector
import re
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
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
}

##############################CRAWLER##############################
count=0
url='https://www.megapetshop.dk/shop/hund-3s1.html'
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)
category=sel.xpath("//div[@class='SubCategoriesContainerImage']/a/@href").getall()
for item in category:
    url=f"https://www.megapetshop.dk{item}"
    response=requests.get(url,headers=headers)
    subcategory=sel.xpath("//div[@class='SubCategoriesContainerImage']/a/@href").getall()
    for item in subcategory:
        url=f"https://www.megapetshop.dk{item}"
        response=requests.get(url,headers=headers)
        sel=Selector(text=response.text)
        subcategory_one=sel.xpath("//div[@class='SubCategoriesContainerImage']/a/@href").getall()
        for item in subcategory_one:
            url=f"https://www.megapetshop.dk{item}"
            print(url)        
            while True:
                response=requests.get(url,headers=headers)
                sel=Selector(text=response.text)
                product_url=sel.xpath("//a[@class='lazy productLink']/@href").getall()
                for product in product_url:
                    print(product)
                    count+=1
                    print(count)
                next_page=sel.xpath("//a[@rel='next']/@href").get()
                if next_page:
                    next_page=f"https://www.megapetshop.dk{next_page}"
                    url=next_page
                else:
                    break


###############################PARSER##############################
url='https://www.megapetshop.dk/shop/3-kg-eukanuba-26395p.html'
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//span[@class='Description_Productinfo' and @itemprop='name']//text()").get()
grammage_quantity=re.search(r'\b\d+\b',product_name).group()
grammage_unit=re.search(r'\b(kg|g|ml|l)\b',product_name).group()
pdp_url=url
regular_price=sel.xpath("//div[@class='priceLine']/span[@itemprop='price']/text()").get()
currency=sel.xpath("//div[@class='priceLine']/text()").get().strip()
product_description=sel.xpath("//div[@class='Description_Productinfo' and @itemprop='description']/text()").getall()
product_description=[item.strip() for item in product_description if item.strip()]
breadcrumb=sel.xpath("//td[contains(@class, 'BreadCrumb_ProductInfo')]//text()").getall()
breadcrumb=[item.strip() for item in breadcrumb if '/' not in item]
image_url=sel.xpath("//div[@id='product-image-container']//img/@src").get()

import requests
from parsel import Selector
import re
url="https://www.walgreens.com/shop"
response=requests.get(url)
sel=Selector(text=response.text)
category_links=sel.xpath("//li[@class='labelledIconContainer']/a/@href").getall()

for idx, link in enumerate(category_links):
    match = re.search(r'ID=(\d+)', link)
    if match:
        id_value = match.group(1)
        if idx == 0:
            payload = {
                "id": ["20003545", id_value]
            }
        else:
            payload = {
                "id": [id_value]
            }


        response=requests.post('https://www.walgreens.com/productsearch/v1/categories',json=payload)
        data=response.json()
        category=data.get("categories",[])
        for item in category:
            category_url=item.get("url","")
            full_url=f"https://www.walgreens.com{category_url}"
            response=requests.get(full_url)
            sel=Selector(text=response.text)
            product_list=sel.xpath("//div[@class='product__details']").getall()
            for product in product_list:
                product_link=product.xpath("//a[@class='color__text-black']/@href").get()
                print(product_link)
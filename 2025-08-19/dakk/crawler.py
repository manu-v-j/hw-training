import requests
from parsel import Selector
import json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.dakkofferstore.com/zoeken?q=Roofboxes',
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
# url='https://www.dakkofferstore.com/dakkoffers'
# response=requests.get(url,headers=headers)
# sel=Selector(text=response.text)
# products = sel.xpath("//vue-thumbnail")

# links = []
# for product in products:
#     attrs = product.attrib   # dict of all attributes
#     link = attrs.get(":link")
#     if link:
#         links.append(link)

# print("Total products:", len(links))
# for l in links:
#     print(l)

url='https://www.dakkofferstore.com/dakkoffer-thule-vector-alpine-black-metallic'
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//h1[@class='heading-h2']/text()").get()
selling_price=sel.xpath("//span[contains(@class,'product-detail__special-price')]/text()").get()
regular_price=sel.xpath("//span[contains(@class,'product-detail__old-price')]/text()").get()
brand=sel.xpath("//dt[contains(text(),'Merk')]/following-sibling::dd/text()").get()
color=sel.xpath("//dt[contains(text(),'Kleur')]/following-sibling::dd/text()").get()
material=sel.xpath("//dt[contains(text(),'Materiaal')]/following-sibling::dd/text()").get()
volume=sel.xpath("//dt[contains(text(),'Inhoud')]/following-sibling::dd/text()").get()
product_description=sel.xpath("//h2[contains(text(),'Productbeschrijving')]/following-sibling::p/text()").get()
breadcrumb=sel.xpath("//ol[@class='breadcrumb']//span/text()").getall()
breadcrumb = " > ".join([i for i in breadcrumb if i != '>'])
image_url=sel.xpath("//div[@class='gallery__mobile']/img/@src").get()
print(image_url)
import requests
from parsel import Selector
import json
import re
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'referer':'https://www.diebo.nl/',
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

# ean_list=[76344107521,76344107491,76344108115,76344107538,76344118572,76344107262,76344108320,76344106661,64992523206,64992525200,64992523602,64992525118,64992714376,64992719814,
# 64992719807,5425039485010,5425039485034,5425039485317,5407009640353,5407009640391,5407009640636,5407009641022,3182551055672,3182551055788,3182551055719,3182551055825,
# 9003579008362,3182550704625,3182550706933,9003579013793]

# for ean in ean_list:
#     url=f"https://www.diebo.nl/assortiment?q={ean}&action=getAjaxSearchArtikelen"

#     response=requests.get(url,headers=headers)
#     sel=Selector(text=response.text)
#     url=sel.xpath("//div[@class='forix-product__item']/a/@href").getall()
#     print(url)

###############################PARSER##############################

response=requests.get("https://www.diebo.nl/kat/natvoer/royal-canin-kattenvoer-indoor-in-gravy-br12-x-85-gr#omschrijving",headers=headers)
sel=Selector(text=response.text)

script=sel.xpath("//script[@ type='application/ld+json']/text()").get()
data = json.loads(script)
data=data[0]
unique_id=data.get("sku","")
product_name=sel.xpath("//h1[@class='forix-product__title']/text()").get()
brand=data.get("brand", {}).get("name","")
brand_type=data.get("brand", {}).get("@type","")
grammage_quantity = re.search(r'(\d+(?:[\.,]\d+)?(?:\s*[xX×]\s*\d+)?)', product_name).group(1)
grammage_unit=re.search(r'\b(kg|g|gr|ml|l)\b',product_name).group()
selling_price=data.get("offers",{}).get("price","")
currency=data.get("offers",{}).get("priceCurrency","")
pdp_url=data.get("offers",{}).get("url","")
product_description=data.get("description")
image_url=data.get("image","")
instock=data.get("offers","").get("availability")
breadcrumb=sel.xpath("//span[@itemprop='name']/text()").getall()


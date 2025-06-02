import requests
from parsel import Selector
import json
import re
headers={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'priority':'u=0,i',
    'referer':'https://www.carrefouruae.com/mafuae/en/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1'
}


##############################CRAWLER##############################
url='https://www.carrefouruae.com/mafuae/en/c/F1600000'
response=requests.get(url,headers=headers)

sel=Selector(response.text)
script = sel.xpath("//script[contains(text(), 'adtechComponentApiResponse')]/text()").get()



to_remove = r'self.__next_f.push([1,"11:["$","$L40",null,'
match = re.search(r'\{.*\}', script, re.DOTALL)

if match:
    json_str = match.group(0)
    unescaped = json_str.encode().decode('unicode_escape')

    data = json.loads(unescaped)

    product_list=data.get("products",[])
    for product in product_list:
        product_url = product.get("links", {}).get("productUrl", {}).get("href")
        url=f"https://www.carrefouruae.com{product_url}"

 
 ##############################PARSER##############################

response=requests.get('https://www.carrefouruae.com/mafuae/en/fish/seabream-400-600g-fresh/p/165311?offer=offer_carrefour_&sid=SLOTTED',headers=headers)
sel=Selector(text=response.text)
product_name_xpath="//h1[@class='css-106scfp']/text()"
selling_price_xpath="//h2[@class='css-17ctnp']/text()[3]"
regular_price_xpath="//div[@class='css-148pv1t']/text()[3]"
currency_xpath="//h2[@class='css-17ctnp']/text()[1]"
grammage_quantity_xpath="//span[@class='css-t0sf5c']/span[2]/text()"
country_of_origin_xpath="//div[@class='css-13w9ki7']/text()"
breadcrumb_xpath="//div[@class='css-iamwo8']/a/text()"
image_xapth=""
product_name=sel.xpath(product_name_xpath).get()
selling_price=sel.xpath(selling_price_xpath).get()
regular_price=sel.xpath(regular_price_xpath).get()
currency=sel.xpath(currency_xpath).get()
grammage_quantity=sel.xpath(grammage_quantity_xpath).get()
match = re.search(r'(\d+(?:\.\d+)?)\s*(kg|g|ml|l|mg)?', grammage_quantity) 
grammage_quantity = int(match.group(1))
grammage_unit=match.group(2)
country_of_origin=sel.xpath(country_of_origin_xpath).get()
breadcrumb=sel.xpath(breadcrumb_xpath).getall()
print(breadcrumb)
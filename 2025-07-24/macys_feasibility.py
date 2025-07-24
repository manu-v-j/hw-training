from curl_cffi import requests
from parsel import Selector
import re
import logging
logging.basicConfig(level=logging.INFO)

url='https://www.macys.com/shop/womens-clothing/all-womens-clothing/dresses?id=5449&tagid=1072403_03_01&ctype=G'
headers={
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'if-none-match':'W/"1b3268-W6GO+X4lb3lh7nKVryCpg84+0KU"',
    'priority':'u=0,i',
    'referer':'https://www.macys.com/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',

}

###################################CRAWLER##########################################
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)
product_urls=sel.xpath("//div[@class='description-spacing']/a/@href").getall()
for url in product_urls:
    full_url=f"https://www.macys.com{url}"
    print(full_url)


#################################PARSER#############################################
url="https://www.macys.com/shop/product/adrianna-papell-womens-asymmetric-metallic-print-mermaid-gown?ID=17472691"
response=requests.get(url,headers=headers)
if response.status_code==200:
    sel=Selector(text=response.text)
    product_name=sel.xpath("//h1[@class='product-title']//a/text()").get()
    regular_price=sel.xpath("//span[@class='body-regular price-strike']/text()").get()
    selling_price=sel.xpath("//span[contains(@aria-label, 'Current Price')]/text()").get()
    promotion_description_raw=sel.xpath("//span[contains(@class,'body-regular price-red')]/text()").get()
    if promotion_description_raw:
        promotion_description=re.sub(r'[\(\)]', '', promotion_description_raw)
    currency="INR"
    pdp_url=url
    breadcrumb=sel.xpath("//li[@class='p-menuitem']/a/text()").getall()
    breadcrumb='>'.join(breadcrumb)
    product_description=sel.xpath("//span[@class='body']/text()").get()
    color=sel.xpath("//span[contains(@data-testid,'selected-color-name')]/text()").get()
    size=sel.xpath("//label[@class='size-tile selection-tile']//text()").getall()
    rating=sel.xpath("//span[contains(@class,'rating-average')]/text()").get()
    review=sel.xpath("//span[@class='rating-description']/a/text()").get()
    features=sel.xpath("//h4[contains(text(),'Product Features')]/following-sibling::div//span/text()").getall()
    fit_guide=sel.xpath("//h4[contains(text(),' Size & Fit ')]/following-sibling::ul//span/text()").getall()
    material=sel.xpath("//h4[contains(text(),' Materials & Care')]/following-sibling::ul//div/text()").getall()
    print(product_name)

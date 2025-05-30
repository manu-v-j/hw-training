import requests
from parsel import Selector
import json
import re

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}


##############################CRAWLER##############################

url='https://www.petsathome.com/product/listing/dog/dog-food'
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)
product_urls=sel.xpath("//a[@class='product-tile_wrapper__T0IlX']/@href").getall()
for product in product_urls:
    product_url='https://www.petsathome.com'+product


##############################PARSER##############################

response=requests.get('https://www.petsathome.com/product/pro-plan-veterinary-diets-canine-ha-hypoallergenic-dry-dog-food/7118367P?productId=7118367&purchaseType=easy-repeat&weight=11kg',
                      headers=headers)

sel=Selector(response.text)
product_name_xpath="//h1[contains(@class,'preview_title-base-product__RDtS0')]/text()"
price_xpath="//span[contains(@class,'purchase-type-selector_price__kb9w9')]/text()"
review_xpath="//span[contains(@class,'preview_reviews__IxlSC')]/text()"
netweight_xpath="//span[@class='product-selector_label__RdDMU']/text()"
breadcrumb_xpath="//a[contains(@class,'breadcrumbs_link__VbQ0m')]/text()"
about_xpath="//div[@class='accordion-items_accordion-body__ziwKz']/p/text()"
ingredients_xpath="//div[@class='accordion-items_ingredients-body__9_M0P']/p/span/text()"

product_name=sel.xpath(product_name_xpath).get()
price=sel.xpath(price_xpath).get()
review=sel.xpath(review_xpath).get()
review=re.search(r'\d+',review).group()if review else None
netweight=sel.xpath(netweight_xpath).get()
ingredients=sel.xpath(ingredients_xpath).get()
breadcrumb=sel.xpath(breadcrumb_xpath).getall()
about=sel.xpath(about_xpath).getall()
print(breadcrumb)

##############################FINDINGS##############################

#product image in pdp is dynamic
import requests
from parsel import Selector
from json import loads
from setttings import headers


base_url="https://www.lorespresso.com/fr_fr/p/splendente-50"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)

#XPATH
PRODUCT_NAME_XPATH="//h1[contains(@class,'MuiTypography-root')]/text()"
SELLING_PRICE_XPATH="//p[@data-testid='final-price']/span/text()"
REGULAR_PRICE_XPATH="//span[@data-testid='lowest-price']/span/text()"
PRODUCT_DESCRIPTION_XPATH="//div[contains(@class,'mui-style-1wb2gim')]/p/text()"
RATING_XPATH="//span[contains(@class,'mui-style-uom3d3')]/text()"
REVIEW_XPATH="//div[contains(@class,'mui-style-19u5b5r')]/text()"
PERCENTAGE_DISCOUNT_XPATH="//div[contains(@class,'mui-style-1hztcnh')]/text()"
BREADCRUMB_XPATH="//li[@class='MuiBreadcrumbs-li']/a/text()"
IMAGES_XPATH="//img[contains(@class,'mui-style-1molse9')]/@src"
SPECIFICATION_XPATH="//tr[contains(@class,'mui-style-kq3u83')]"
product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
selling_price_raw=sel.xpath(SELLING_PRICE_XPATH).get()
regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH).get()
product_decsription=sel.xpath(PRODUCT_DESCRIPTION_XPATH).getall()
rating=sel.xpath(RATING_XPATH).get()
review=sel.xpath(REVIEW_XPATH).get()
percentage_discount=sel.xpath(PERCENTAGE_DISCOUNT_XPATH).get()
breadcrumb=sel.xpath(BREADCRUMB_XPATH).getall()
images=sel.xpath(IMAGES_XPATH).get()
product_specification={}
specification_raw=sel.xpath(SPECIFICATION_XPATH)
for row in specification_raw:
    key=row.xpath(".//td/p/text()").get()
    value=row.xpath(".//td/p[contains(@class,'mui-style-z7ivlo')]/text()").get()
    product_specification[key]=value

#backend
json_text = sel.xpath("//script[@type='application/ld+json']/text()").get()

data = loads(json_text)
sku=data.get('sku','')

print(selling_price)

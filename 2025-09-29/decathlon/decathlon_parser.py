from curl_cffi import requests
from parsel import Selector
from json import loads
from settings import headers

base_url="https://www.decathlon.de/p/wanderschuhe-kinder-groesse-28-34-halbhoch-klettverschluss-nh500-blau/_/R-p-348281?mc=8852774&c=sturmblau_stahlblau_perlrosa"
response=requests.get(base_url,headers=headers,impersonate='chrome')
sel=Selector(text=response.text)

#XPATH
UNIQUE_XPATH="//div[@class='product-info__product-id']/span/text()"
SELLING_PRICE_XPATH="//span[contains(@class,'price-base__current-price')]/text()"
REGULAR_PRICE_XPATH="//span[contains(@class,'price-base__previous-price')]/text()"
BREADCRUMB_XPATH="//a[@class='breadcrumb-item']/span/text()"
WARRANTY_XPATH="//span[contains(text(),'Garantie')]/text()"
CARE_INSTRUCTIONS_XPATH="//h3[contains(@class,'care-instructions__title ')]/following-sibling::div//text()"
MATERIAL_XPATH="//p[@class='specifications__item vp-body-s']/text()"
PROMOTION_XPATH="//span[@class='price-base__commercial-message']/text()"

#EXTRACT
unique_id_raw=sel.xpath(UNIQUE_XPATH).getall()
script=sel.xpath("//script[@type='application/ld+json']/text()").get()
data=loads(script)
product_name=data.get('name','')
brand=data.get('brand',{}).get('name','')
product_description=data.get('description','')
rating=data.get('aggregateRating',{}).get('ratingValue','')
review=data.get('aggregateRating',{}).get('reviewCount','')
image_url=data.get('image','')

selling_price_raw=sel.xpath(SELLING_PRICE_XPATH).get()
regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH).get()
breadcrumb_raw=sel.xpath(BREADCRUMB_XPATH).getall()
warranty_raw=sel.xpath(WARRANTY_XPATH).get()
care_instructions_raw=sel.xpath(CARE_INSTRUCTIONS_XPATH).getall()
material_composition=sel.xpath(MATERIAL_XPATH).get()
promotion_description=sel.xpath(PROMOTION_XPATH).get()

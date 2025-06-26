import requests
from parsel import Selector
from settings import url,headers
import re
response=requests.get(url,headers=headers)
sel=Selector(text=response.text)


product_name=sel.xpath("//div[@class='product__title']/h1/text()").get()
brand=sel.xpath("//p[@class='product__text inline-richtext caption-with-letter-spacing']/text()").get()
regular_price_raw=sel.xpath("//span[@class='price-item price-item--regular']/text()").get()
if regular_price_raw:
    regular_price_raw=regular_price_raw.strip()
regular_price=regular_price_raw.replace('₹','')
currency=match = re.search(r"[^\d\s.,]+", regular_price_raw).group()
breadcrumb=sel.xpath("//li[@class='breadcrumbs__item']/a/text()").getall()
pdp_url=url
product_description=sel.xpath("//div[@class='features_discription']/p/text()").get()

country_of_origin=sel.xpath("//div[@class='features' and b[text()='Country Of Origin:']]/text()[2]").get()
if country_of_origin:
    country_of_origin=country_of_origin.strip()

instructions=sel.xpath("//div[@class='features' and b[text()='Care Instruction:']]/text()[2]").get()
if instructions:
    instructions=instructions.strip()

material=sel.xpath("//div[@class='features' and b[text()='Fabric Composition:']]/text()[2]").get()
if material:
    material=material.strip()

size=sel.xpath("//label[@class='product_clr_variant' and @id='pdp-variant']/text()").getall()
image_urls=sel.xpath("//div[@class='product__media media media--transparent']/img/@src").getall()

fit_guide=sel.xpath("//div[@class='features' and b[text()='Model Fit:']]/text()[2]").get()
if fit_guide:
    fit_guide=fit_guide.strip()

body_fit=sel.xpath("//div[@class='features' and b[text()='Fit:']]/text()[2]").get()
if body_fit:
    body_fit=body_fit.strip()


product_sku=sel.xpath("//div[@class='features' and b[text()='SKU:']]/text()[2]").get()
if product_sku:
    product_sku=product_sku.strip()

manufacturer_address=sel.xpath("//div[@class='features' and b[text()='Manufactured and Marketed By:']]/p/text()").get()

product_dimensions=sel.xpath("//div[@class='features' and b[text()='Dimensions:']]/text()[2]").get()
if product_dimensions:
    product_dimensions=product_dimensions.strip()

product_quantity=sel.xpath("//div[@class='features' and b[text()='Net Quantity:']]/text()[2]").get()
if product_quantity:
    product_quantity=product_quantity.strip()

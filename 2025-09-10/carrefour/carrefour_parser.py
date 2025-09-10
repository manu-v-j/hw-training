import requests
from settings import headers,cookies
from parsel import Selector
import json,re
base_url="https://www.carrefour.fr/p/dattes-deglet-nour-la-favorite-3068232250003?t=1908"
response=requests.get(base_url,headers=headers,cookies=cookies)
sel=Selector(text=response.text)
script=sel.xpath("//script[@type='application/ld+json'][2]/text()").get()
data=json.loads(script)
country='france'
brand=data.get('brand',{}).get('name','')
product_name=data.get('name','')
pack_size=data.get('description','')
price_per_pack=data.get('offers',{}).get('offers',[])
price_per_pack=price_per_pack[0].get('price','')

price_per_raw=sel.xpath("//p[contains(@class,'roduct-title__per-unit-label')]/text()").get()
price_per=''
if price_per_raw:
    price_per=re.search(r'\d+(\.\d+)?', price_per_raw)
    price_per = price_per.group() if price_per else ''

promotion_available=sel.xpath("//span[contains(@class,'promotion-label-refonte__label')]/text()").getall()
promotion="Yes" if promotion_available else "No"

promotion_description=sel.xpath("//span[contains(@class,'promotion-label-refonte__label')]/text()").getall()
promotion_description = ' '.join([p.strip() for p in promotion_description if p.strip()])

product_description=sel.xpath(
    "//p[contains(text(),' Description') ]/ancestor::div[@class='product-content__title']/following-sibling ::div/div//text()").get()

if product_description:
    product_description = product_description.replace('\n', ' ')
    product_description = re.sub(r'\s+', ' ', product_description).strip()

ingredients=sel.xpath(
    "//p[contains(text(),' Ingrédients') ]/ancestor::div[@class='product-content__title']/following-sibling ::div/div//text()").get()

if ingredients:
    ingredients = ingredients.replace('\n', ' ')
    ingredients = re.sub(r'\s+', ' ', ingredients).strip()

legal_name = sel.xpath(
            "//p[contains(text(),'Nom légal')]/ancestor::div[@class='product-content__title']/following-sibling::div//div/text()").get() 

#doubts
category_path=sel.xpath("//li[contains(@class,'c-breadcrumbs__breadcrumb')]//a//text()").getall()
category_path=','.join(category_path)

image_url=data.get('image',{}).get('url','')

#Backend
product_code=data.get('gtin13','')
#Backend
promotion_start=data.get('offers',{}).get('offers',[])[0].get('validFrom','')
promotion_end=data.get('offers',{}).get('offers',[])[0].get('priceValidUntil','')


nutritional_values = sel.xpath("//tr[contains(@class,'nutritional-details__value')]").getall()
nutritional={}
for item_html in nutritional_values:
    item_sel = Selector(text=item_html)
    
    name = item_sel.xpath("//th/span/text()").get()
    name = name.strip() if name else ""

    value = item_sel.xpath("//td[1]/span/text()").get()
    value = value.strip() if value else ""

    percent = item_sel.xpath("//td[2]/span/text()").get()
    percent = percent.strip() if percent else ""

    nutritional[f"{name}_Valeurs nutritionnelles"]=value
    nutritional[f"{name}_Taux d'apports journaliers"]=percent

manufacture=brand
labels=sel.xpath("//div[contains(@class,'pdp-hero__tag')]/div//text()").get()

item={}
item['Country'] = country
item['Retail Chain'] = ''
item['Brand'] = brand
item['Product Name'] = product_name
item['Pack Size'] = pack_size
item['Price per Pack'] = price_per_pack
item['Price per Kg or L'] = price_per
item['Promotion (Yes/No)'] = promotion
item['Promotion Description'] = promotion_description
item['Product Description'] = product_description
item['Ingredients'] = ingredients
item['Legal Name'] = legal_name
item['Category Path'] = category_path
item['Product Image URL'] = image_url
item['Product Code (EAN/GTIN)'] = product_code
item['Unit Count or Quantity'] = ''
item['Private Label (Yes/No)'] = ''
item['Promotion Start Date'] = promotion_start
item['Promotion End Date'] = promotion_end
item['Promotion Type'] = ''
item['Store or Region'] = ''
item['Allergen & Dietary Claims'] = ''
item['Nutritional Values'] = nutritional
item['Manufacturer or Distributor'] = brand
item['Additional Claims or Labels'] = labels

print(item['Nutritional Values'])

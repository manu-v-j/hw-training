import requests
from settings import headers,cookies,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS,COLLECTION_ERROR
from parsel import Selector
import json,re
import logging
import pandas as pd
from pymongo import MongoClient
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]
        self.collection_error=self.db[COLLECTION_ERROR]
        self.fieldnames = ['Pdp Url','Country', 'Retail Chain', 'Brand', 'Product Name', 'Pack Size',
            'Price per Pack', 'Price per Kg or L', 'Promotion (Yes/No)',
            'Promotion Description', 'Product Description', 'Ingredients',
            'Legal Name', 'Category Path', 'Product Image URL',
            'Product Code (EAN/GTIN)', 'Unit Count or Quantity',
            'Private Label (Yes/No)', 'Promotion Start Date',
            'Promotion End Date', 'Promotion Type', 'Store or Region',
            'Allergen & Dietary Claims', 'Nutritional Values',
            'Manufacturer or Distributor', 'Additional Claims or Labels'
        ]

        self.items = []

    def start(self):
        for item in self.db[COLLECTION].find().limit(200):
            base_url=item.get('link')
            response=requests.get(base_url,headers=headers,cookies=cookies)
            if response.status_code==200:
                self.parse_item(response,base_url)
            else:
                self.collection_error.insert_one({'link':base_url})

        df = pd.DataFrame(self.items, columns=self.fieldnames)
        df.to_csv('carrefour_20250911.csv', index=False, encoding='utf-8')

    def parse_item(self,response,base_url):
        sel=Selector(text=response.text)

        #XPATH
        SCRIPT_XPATH="//script[@type='application/ld+json'][2]/text()"
        PRICE_PER_RAW_XAPTH="//p[contains(@class,'roduct-title__per-unit-label')]/text()"
        PROMOTION_AVAILABLE_XPATH="//span[contains(@class,'promotion-label-refonte__label')]/text()"
        PROMOTION_DESCRIPTION_XPATH="//span[contains(@class,'promotion-label-refonte__label')]/text()"
        PRODDUCT_DESCRIPTION_XPATH="//p[contains(text(),' Description') ]/ancestor::div[@class='product-content__title']/following-sibling ::div/div//text()"
        INGREDIENTS_XPATH="//p[contains(text(),' Ingrédients') ]/ancestor::div[@class='product-content__title']/following-sibling ::div/div//text()"
        LEGAL_NAME_XPATH="//p[contains(text(),'Nom légal')]/ancestor::div[@class='product-content__title']/following-sibling::div//div/text()"
        CATEGORY_PATH_XPATH="//li[contains(@class,'c-breadcrumbs__breadcrumb')]//a//text()"
        NUTRITIONAL_VALUES_XPATH="//tr[contains(@class,'nutritional-details__value')]"
        LABELS_XPATH="//div[contains(@class,'pdp-hero__tag')]/div//text()"

        #EXTARCT
        script=sel.xpath(SCRIPT_XPATH).get()
        data=json.loads(script)
        country='france'
        brand=data.get('brand',{}).get('name','')
        product_name=data.get('name','')
        pack_size=data.get('description','')
        price_per_pack=data.get('offers',{}).get('offers',[])
        price_per_pack=price_per_pack[0].get('price','')


        price_per_raw=sel.xpath(PRICE_PER_RAW_XAPTH).get()
        promotion_available=sel.xpath(PROMOTION_AVAILABLE_XPATH).getall()
        promotion_description=sel.xpath(PROMOTION_DESCRIPTION_XPATH).getall()
        product_description=sel.xpath(PRODDUCT_DESCRIPTION_XPATH).get()
        ingredients=sel.xpath(INGREDIENTS_XPATH).get()
        legal_name = sel.xpath(LEGAL_NAME_XPATH).get() 
        nutritional_values = sel.xpath(NUTRITIONAL_VALUES_XPATH).getall()
        labels=sel.xpath(LABELS_XPATH).get()

        #doubt
        category_path=sel.xpath(CATEGORY_PATH_XPATH).getall()


        #CLEAN
        price_per=''
        if price_per_raw:
            price_per=re.search(r'\d+(\.\d+)?', price_per_raw)
            price_per = price_per.group() if price_per else ''

        promotion="Yes" if promotion_available else "No"

        promotion_description = ' '.join([p.strip() for p in promotion_description if p.strip()])

        if product_description:
            product_description = product_description.replace('\n', ' ')
            product_description = re.sub(r'\s+', ' ', product_description).strip()

        if ingredients:
            ingredients = ingredients.replace('\n', ' ')
            ingredients = re.sub(r'\s+', ' ', ingredients).strip()

        category_path=','.join(category_path)
        image_url=data.get('image',{}).get('url','')

        #Backend
        product_code=data.get('gtin13','')
        #Backend
        promotion_start=data.get('offers',{}).get('offers',[])[0].get('validFrom','')
        promotion_end=data.get('offers',{}).get('offers',[])[0].get('priceValidUntil','')


        values = sel.xpath("//th[contains(@class, 'nutritional-details__header--column-title')]/span/text()").getall()
        values = [h.strip().replace('\n', ' ') for h in values]

        value_1 = ""
        value_2 = ""

        for h in values:
            if "Valeurs nutritionnelles" in h and "Taux" not in h:
                value_1 = h
            elif "Taux d'apports journaliers" in h:
                value_2 = h

        nutritional = {}

        for item_html in nutritional_values:
            item_sel = Selector(text=item_html)
                    
            name = item_sel.xpath(".//th//text()").get()
            name = name.strip() if name else ""

            value = item_sel.xpath(".//td[1]//text()").get()
            value = value.strip() if value else ""

            percent = item_sel.xpath(".//td[2]//text()").get()
            percent = percent.strip() if percent else ""
            if name:
                if value_1:
                    key_value = f"{name}_{value_1}"
                    nutritional[key_value] = value
                
                if value_2:
                    key_percent = f"{name}_{value_2}"
                    nutritional[key_percent] = percent



        item={}
        item['Pdp Url']=base_url
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

        self.items.append(item)

        logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()
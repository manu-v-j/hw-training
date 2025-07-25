from curl_cffi import requests
from parsel import Selector
from pymongo import MongoClient
from macys_items import Product_Item
import json
from settings import headers,MONGO_DB,MONGO_URL,COLLECTION
import logging
import re
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                sel=Selector(text=response.text)

                #XPATH
                PRODUCT_NAME_XPATH="//h1[@class='product-title']//span/text()"
                BRAND_XPATH="//h1[@class='product-title']//a/text()"
                REGULAR_PRICE_XPATH="//span[@class='body-regular price-strike']/text()"
                SELLING_PRICE_XPATH="//span[contains(@aria-label, 'Current Price')]/text()"
                PROMOTION_DESCRIPTION_XPATH="//span[contains(@class,'body-regular price-red')]/text()"
                BREADCRUMB_XPATH="//li[@class='p-menuitem']/a/text()"
                PRODUCT_DESCRIPTION_XPATH="//div[@class='long-description medium']/p/text()"
                COLOR_XPATH="//img[@class='color-swatch-sprite']/@alt"
                SIZE_XPATH="//label[@class='size-tile selection-tile']//text()"
                RATING_XPATH="//span[contains(@class,'rating-average')]/text()"
                REVIEW_XPATH="//span[@class='rating-description']/a/text()"
                FEATURES_XPATH="//h4[contains(text(),'Product Features')]/following-sibling::div//span/text()"
                MATERIAL_CARE_XPATH="//h4[contains(text(),' Materials & Care')]/following-sibling::ul//div/text()"
                AVAILABILITY_XPATH="//div[@class='grid-y margin-bottom-m']/div/text()"
                SCRIPT_XPATH="//script[@type='application/ld+json' and @id='productMktData']/text()"

                #EXTRACT
                product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
                brand=sel.xpath(BRAND_XPATH).get()
                regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH).get()
                selling_price_raw=sel.xpath(SELLING_PRICE_XPATH).get()
                promotion_description_raw=sel.xpath(PROMOTION_DESCRIPTION_XPATH).get()
                breadcrumb_raw=sel.xpath(BREADCRUMB_XPATH).getall()
                product_description=sel.xpath(PRODUCT_DESCRIPTION_XPATH).get()
                color=sel.xpath(COLOR_XPATH).getall()
                size=sel.xpath(SIZE_XPATH).getall()
                rating=sel.xpath(RATING_XPATH).get()
                review=sel.xpath(REVIEW_XPATH).get()
                features=sel.xpath(FEATURES_XPATH).getall()
                material_care_instruction=sel.xpath(MATERIAL_CARE_XPATH).getall()
                availability=sel.xpath(AVAILABILITY_XPATH).get()
                script=sel.xpath(SCRIPT_XPATH).get()
        
                #CLEAN
                match = re.search(r'ID=(\d+)', url)
                if match:
                    product_id = match.group(1)
                if regular_price_raw:    
                    regular_price=regular_price_raw.replace('INR','')
                if selling_price_raw:    
                    selling_price=selling_price_raw.replace('INR','')
                if promotion_description_raw:
                    promotion_description=re.sub(r'[\(\)]', '', promotion_description_raw)
                breadcrumb='>'.join(breadcrumb_raw)
                features=','.join(features)
                material_care_instruction=','.join(material_care_instruction)
                data=json.loads(script)
                image_url=data.get('image',[])


                item={}
                item['product_id']=product_id
                item['product_name']=product_name
                item['brand']=brand
                item['regular_price']=regular_price
                item['selling_price']=selling_price
                item['promotion_description']=promotion_description
                item['currency']='INR'
                item['pdp_url']=url
                item['breadcrumb']=breadcrumb
                item['product_description']=product_description
                item['color']=color
                item['size']=size
                item['rating']=rating
                item['review']=review
                item['features']=features
                item['material_care_instruction']=material_care_instruction
                item['availability']=availability
                item['image_url']=image_url

                product_item=Product_Item(**item)
                product_item.save()

                logging.info(item)

                
if __name__=='__main__':
    parser=Parser()
    parser.start()
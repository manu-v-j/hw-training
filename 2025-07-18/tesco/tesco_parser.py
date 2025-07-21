import requests
from parsel import Selector
import re
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS,COLLECTION_ERROR
from tesco_items import ProductItem
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]
        self.collection_error=self.db[COLLECTION_ERROR]

    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response,url)
            else:
                self.collection_error.insert_one({'link':url})

    def parse_item(self,response,url):
        sel=Selector(text=response.text)

        #XPATH
        PRODUCT_NAME_XPATH="//h1[@data-auto='pdp-product-title']/text()"
        REGULAR_PRICE_XPATH="//p[contains(@class,'ddsweb-text ac8f2b_FKk1BW_priceText')]/text()"        
        PRODUCT_DESCRIPTION_XPATH="//h3[contains(text(), 'Description')]/following-sibling::div[contains(@class, 'OobGYfu9hvCUvH6')]/span/text()"
        INGREDIENTS_XPATH="//h3[contains(text(), 'Ingredients')]/following-sibling::div[contains(@class, 'OobGYfu9hvCUvH6')]/p//text()"
        ALLERGIES_XPATH="//h3[contains(text(), 'Allergy Information')]/following-sibling::div[contains(@class, 'OobGYfu9hvCUvH6')]/span/text()"
        NUTRITIONS_ROWS_XPATH = "//table[contains(@class,'product__info-table')]//tbody/tr"
        STORAGE_INSTRUCTIONS_XPATH="//div[@id='accordion-panel-storage']//div[@class='OobGYfu9hvCUvH6']/text()"
        PREPARATION_INSTRUCTIONS_XPATH="//h3[contains(text(),'Cooking Instructions')]/following-sibling::div[@class='OobGYfu9hvCUvH6']//text()"
        RECYCLING_INFORMATION_XPATH="//div[@id='accordion-panel-recycling-info']//following-sibling::div[@class='OobGYfu9hvCUvH6']/text()"
        COLOR_XPATH="//img[contains(@class,'ac8f2b_o7KQoq_dataLayerimage')]/@alt"
        SIZE_XPATH="//span[contains(@class,'ddsweb-button__inner-container b6325c_8WKJvW_container')]/text()"
        MATERIAL_XPATH="//h3[contains(text(), 'Material')]/following-sibling::div[1]/span[@class='QhtPR2LZPKOnKcE']/text()"
        GRAPE_VARIETY_XPATH="//h3[contains(text(), 'Grape Variety')]/following-sibling::div/text()"
        COUNTRY_OF_ORIGIN_XPATH="//h3[contains(text(), 'Country')]/following-sibling::div/text()"
        CARE_INSTRUCTIONS_XPATH="//h3[contains(text(), 'Care')]/following-sibling::div/span[@class='QhtPR2LZPKOnKcE']/text()"
        ADDRESS_XPATH="//h3[contains(text(),'Manufacturer Address')]/following-sibling::div[1]//span/text()"
        RETURN_ADDRESS_XPATH="//h3[contains(text(),'Return to')]/following-sibling::div[@class='OobGYfu9hvCUvH6']/span/text()"
        RATING_XPATH = "//p[contains(@class,'ddsweb-rating__hint')]/text()"
        REVIEW_XPATH="//a[@class='ddsweb-link ddsweb-link__anchor ddsweb-link__inline d7d27c_8WKJvW_inlineLink d7d27c_8WKJvW_link']/text()"
        BREADCRUMBS_XPATH="//div[contains(@class,'ddsweb-breadcrumb__item')]//text()"
        IMAGE_URL_XPATH="//img[contains(@class,'ddsweb-responsive-image__image ')]/@src"
        DATE_XPATH="//p[contains(@class,'ddsweb-value-bar__terms fcea0c_l011wq_termsText')]/text()"
      

        #EXTRACT
        product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
        regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH).get()
        currency="pound"
        pdp_url=url
        product_description=sel.xpath(PRODUCT_DESCRIPTION_XPATH).get()
        ingredients=sel.xpath(INGREDIENTS_XPATH).getall()
        allergens=sel.xpath(ALLERGIES_XPATH).get()
        nutritions_rows=sel.xpath(NUTRITIONS_ROWS_XPATH)
        storage_instructions=sel.xpath(STORAGE_INSTRUCTIONS_XPATH).get()
        preparation_instructions=sel.xpath(PREPARATION_INSTRUCTIONS_XPATH).getall()
        recycling_information=sel.xpath(RECYCLING_INFORMATION_XPATH).get()
        color=sel.xpath(COLOR_XPATH).getall()
        size=sel.xpath(SIZE_XPATH).getall()
        material=sel.xpath(MATERIAL_XPATH).get()
        grape_variety=sel.xpath(GRAPE_VARIETY_XPATH).get()
        country_of_origin=sel.xpath(COUNTRY_OF_ORIGIN_XPATH).get()
        care_instructions=sel.xpath(CARE_INSTRUCTIONS_XPATH).get()
        address=sel.xpath(ADDRESS_XPATH).getall()
        return_address=sel.xpath(RETURN_ADDRESS_XPATH).getall()
        rating=sel.xpath(RATING_XPATH).get()
        review=sel.xpath(REVIEW_XPATH).get()
        breadcrumbs=sel.xpath(BREADCRUMBS_XPATH).getall()
        image_url=sel.xpath(IMAGE_URL_XPATH).getall()
        date=sel.xpath(DATE_XPATH).get()

        #CLEAN
        regular_price=''
        if regular_price_raw:
            regular_price= regular_price_raw.replace('Â', '').replace('£', '').strip()
            regular_price = "{:.2f}".format(float(regular_price))
        product_description=''.join([description for description in product_description]) if product_description else ''
        preparation_instructions=' '.join([instruction for instruction in preparation_instructions])
        manufacturer_address = ''.join([line.strip() for line in address if line.strip()])
        return_address = ''.join([line.strip() for line in return_address if line.strip()])
        ingredients=''.join([item for item in ingredients])
        grammage_quantity=''
        grammage_unit=''
        if product_name:
            match = re.search(r'(\d+(?:\.\d+)?)[\s]*?(mg|kg|g|ml|l|cl|pcs|pack|pk|ct)', product_name, re.IGNORECASE)
            if match:
                grammage_quantity=match.group(1)
                grammage_unit=match.group(2)

        nutritions = {}
        for row in nutritions_rows:
            label = row.xpath("./th/text()").get()
            per_100g = row.xpath("./td[1]/text()").get()
            per_pack = row.xpath("./td[2]/text()").get()
            if label and per_100g and per_pack:
                nutritions[label.strip()] = {
                    "per_100g": per_100g.strip(),
                    "per_pack": per_pack.strip()
                    }
        rating=rating.replace(' stars','')
        if review:
            review=review.replace(' Reviews','')
        offer_valid_from=''  
        offer_valid_upto=''
        if date:
            dates = re.findall(r"\d{2}/\d{2}/\d{4}", date)
            if len(dates) == 2:
                offer_valid_from = dates[0]
                offer_valid_upto = dates[1]



        item={}
        item['product_name']=product_name
        item['regular_price']=regular_price
        item['currency']=currency
        item['pdp_url']=pdp_url
        item['product_description']=product_description
        item['ingredients']=ingredients
        item['allergens']=allergens
        item['grammage_quantity']=grammage_quantity
        item['grammage_unit']=grammage_unit
        item['nutritions']=nutritions
        item['storage_instructions']=storage_instructions
        item['preparation_instructions']=preparation_instructions
        item['recycling_information']=recycling_information
        item['color']=color
        item['size']=size
        item['material']=material
        item['grape_variety']=grape_variety
        item['country_of_origin']=country_of_origin
        item['care_instructions']=care_instructions
        item['manufacturer_address']=manufacturer_address
        item['return_address']=return_address
        item['rating']=rating
        item['review']=review
        item['breadcrumbs']=breadcrumbs
        item['image_url']=image_url
        item['offer_valid_from']=offer_valid_from
        item['offer_valid_upto']=offer_valid_upto
        
        product_item=ProductItem(**item)
        product_item.save()

        logging.info(item)
                     
if __name__=='__main__':
    parser=Parser()
    parser.start()
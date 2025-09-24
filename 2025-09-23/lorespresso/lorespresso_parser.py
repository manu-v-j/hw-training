import requests
import logging
from parsel import Selector
from json import loads
from pymongo import MongoClient
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS,COLLECTION_ERROR
from lorespresso_item import Product_Item
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION_DETAILS]
        self.collection_error=self.db[COLLECTION_ERROR]

    def start(self):
        for item in self.db[COLLECTION].find():
            base_url=item.get('link')
            response=requests.get(base_url,headers=headers)
            if response.status_code==200:
                self.parse_item(response,base_url)
            else:
                self.collection_error.insert_one({'link':base_url})

    def parse_item(self,response,base_url):
        sel=Selector(text=response.text)

        #XPATH
        PRODUCT_NAME_XPATH="//h1[contains(@class,'MuiTypography-root')]/text()"
        SELLING_PRICE_XPATH="//p[@data-testid='final-price']/span/text()"
        REGULAR_PRICE_XPATH="//span[@data-testid='lowest-price']/span/text()"
        PRODUCT_DESCRIPTION_XPATH="//h2[text()='Description']/parent::div/following-sibling::div/p/text()"
        RATING_XPATH="//span[contains(@class,'mui-style-uom3d3')]/text()"
        REVIEW_XPATH="//div[contains(@class,'mui-style-19u5b5r')]/text()"
        PERCENTAGE_DISCOUNT_XPATH="//div[contains(@class,'mui-style-1hztcnh')]/text()"
        BREADCRUMB_XPATH="//li[@class='MuiBreadcrumbs-li']/a/text()"
        IMAGES_XPATH="//img[contains(@class,'mui-style-1molse9')]/@src"

        #EXTRACT
        product_name=sel.xpath(PRODUCT_NAME_XPATH).get()
        selling_price_raw=sel.xpath(SELLING_PRICE_XPATH).get()
        regular_price_raw=sel.xpath(REGULAR_PRICE_XPATH).get()
        product_description_raw=sel.xpath(PRODUCT_DESCRIPTION_XPATH).getall()
        rating=sel.xpath(RATING_XPATH).get()
        review_raw=sel.xpath(REVIEW_XPATH).get()
        promotion_description=sel.xpath(PERCENTAGE_DISCOUNT_XPATH).get()
        breadcrumb_raw=sel.xpath(BREADCRUMB_XPATH).getall()
        images=sel.xpath(IMAGES_XPATH).get()

        #CLEAN
        selling_price=''
        if selling_price_raw:
            selling_price=selling_price_raw.replace('€','').replace(',','.')
            selling_price="{:.2f}".format(float(selling_price))

        regular_price=''
        if regular_price_raw:
            regular_price=regular_price_raw.replace('€','').replace(',','.')
            regular_price="{:.2f}".format(float(regular_price))
        else:
            regular_price=selling_price

        breadcrumb=' > '.join(breadcrumb_raw)

        if review_raw:
            review=review_raw.replace(' Avis','')
        else:
            review=''
        
        product_description=''
        if product_description_raw:
            product_description = ' '.join([item.strip() for item in product_description_raw])

       

        item={}
        item['product_name']=product_name
        item['selling_price']=selling_price
        item['regular_price']=regular_price
        item['currency']='EURO'
        item['pdp_url']=base_url
        item['product_description']=product_description
        item['rating']=rating
        item['review']=review
        item['promotion_description']=promotion_description
        item['breadcrumb']=breadcrumb
        item['images']=images

        product_item=Product_Item(**item)
        product_item.save()

        logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()
import requests
import json
from parsel import Selector
from pymongo import MongoClient
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_ERROR

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]

    def start(self):
        for item in self.db[COLLECTION].find():
            base_url=item.get('link','')
            response=requests.get(base_url,headers=headers)

            if response.status_code==200:
                self.parse_item(response,base_url)
            else:
                self.db[COLLECTION_ERROR].insert_one({'link':base_url})

    def start(self,response,base_url):
        sel=Selector(text=response.text)

        #XPATH
        PRODUCT_NAME_XPATH="//div[contains(@class,'product-heading')]//text()"
        SELLING_PRICE_XPATH="//span[@class='money']/text()"
        REGULAR_PRICE_XPATH="//span[@class='regular-price']/span/text()"
        PERCENTAGE_DISCOUNT="//span[@class='perc_price']/text()"
        SIZE_XPATH="//span[@class='size-title']/text()"
        COLOR_XPATH="//div[@class='color-title']/text()"
        SCRIPT_XPATH="//script[@type='application/ld+json'][3]/text()"
        BREADCRUMB_XPATH="//nav[@class='breadcrumb']//text()"
        MANUFACTURER_ADDRESS_XAPTH="//div[text()='Manufacturer Details']/following-sibling::div//text()"

        #EXTRACT
        product_name_raw=sel.xpath(PRODUCT_NAME_XPATH).getall()
        regular_price_raw=sel.xpath(SELLING_PRICE_XPATH).get()
        selling_price_raw=sel.xpath(REGULAR_PRICE_XPATH).get()
        percentage_discount=sel.xpath(PERCENTAGE_DISCOUNT).get()
        size=sel.xpath(SIZE_XPATH).getall()
        color=sel.xpath(COLOR_XPATH).get()
        script=sel.xpath(SCRIPT_XPATH).get()
        breadcrumb_raw=sel.xpath(BREADCRUMB_XPATH).getall()
        manufacturer_address_raw=sel.xpath(MANUFACTURER_ADDRESS_XAPTH).getall()

        #CLEAN
        product_name=' '.join([item.strip() for item in product_name_raw if item.strip()])
        selling_price=selling_price_raw.replace('₹ ','').replace(',','')
        regular_price=regular_price_raw.replace('₹ ','').replace(',','')
        size=','.join(size)

        data=json.loads(script)
        product_description=data.get('description','')
        images=data.get('image','')
        breadcrumb = ' > '.join([item.strip() for item in breadcrumb_raw if item.strip() and item.strip() != '/'])
        manufacturer_address=' '.join([item.strip() for item in manufacturer_address_raw if item.strip()])

        item={}
        item['product_name']=product_name
        item['selling_price']=selling_price
        item['regular_price']=regular_price
        item['currency']='INR'
        item['pdp_url']=base_url
        item['product_description']=product_description
        item['percentage_discount']=percentage_discount
        item['size']=size
        item['color']=color
        item['breadcrumb']=breadcrumb
        item['manufacturer_address']=manufacturer_address
        item['images']=images


if __name__=='__main__':
    parser=Parser()
    parser.start()
    
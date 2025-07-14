from curl_cffi import requests
from parsel import Selector
from pymongo import MongoClient
from settings import headers,MONGO_DB,MONGO_URI,COLLECTION,DETAILS_COLLECTION
import json

class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[DETAILS_COLLECTION]
        
    def start(self):
        for item in self.db[COLLECTION].find():
            url=item.get('link')
            print(url)
            response=requests.get(url,headers=headers)
            if response.status_code==200:
                self.parse_item(response)
    def parse_item(self,response):
        sel=Selector(text=response.text)

        #XPATH
        product_name_xpath="//h1[contains(@class,'sui-h4-bold')]/text()"
        selling_price_xpath="//span[@class='sui-font-display sui-leading-none sui-px-[2px] sui-text-9xl sui--translate-y-[0.5rem]']/text()"
        price_was_xpath="//span[@class='sui-line-through']//text()"
        currency_xpath="//span[@class='sui-font-display sui-leading-none sui-text-3xl']/text()"
        percentage_discount_xpath="//span[@class='sui-text-success']/div/span/text()[2]"
        script_xpath="//script[@id='thd-helmet__script--productStructureData']/text()"

        #EXTRACT
        product_name=sel.xpath(product_name_xpath).get()
        selling_price=sel.xpath(selling_price_xpath).get()
        price_was=sel.xpath(price_was_xpath).get()
        currency=sel.xpath(currency_xpath).get()
        percentage_discount=sel.xpath(percentage_discount_xpath).get()
        script=sel.xpath(script_xpath).get()
        data=json.loads(script)
        product_description=data.get('description','')
        unique_id=data.get('productID','')
        product_sku=data.get('sku','')
        brand=data.get('brand',{}).get('name','')
        rating=data.get('aggregateRating',{}).get('ratingValue','')
        review=data.get('aggregateRating',{}).get('reviewCount','')
        color=data.get('color','')
        model_number=data.get('model','')
        depth=data.get('depth','')
        height=data.get('height','')
        width=data.get('width','')
        weight=data.get('weight','')
        image_url=data.get('image',[])

        item={}
        item['product_name']=product_name
        item['selling_price']=selling_price
        item['price_was']=price_was
        item['currency']=currency
        item['percentage_discount']=percentage_discount
        item['product_description']=product_description
        item['unique_id']=unique_id
        item['product_sku']=product_sku
        item['brand']=brand
        item['rating']=rating
        item['review']=review
        item['color']=color
        item['model_number']=model_number
        item['depth']=depth
        item['height']=height
        item['width']=width
        item['weight']=weight
        item['image_url']=image_url


if __name__=='__main__':
    parser=Parser()
    parser.start()
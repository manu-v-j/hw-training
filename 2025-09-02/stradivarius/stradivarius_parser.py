import requests
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION
import json,re
from pymongo import MongoClient
from stradivarius_items import Product_Item
import logging
logging.basicConfig(level=logging.INFO)


class Parser:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]

    def start(self):
        for item in self.db[COLLECTION].find():
            id=item.get('id','')
            params = {
                'languageId': '-1',
                'appId': '1',
            }
            base_url=f'https://www.stradivarius.com/itxrest/2/catalog/store/55009581/50331096/category/0/product/{id}/detail'
            response = requests.get(
                base_url,
                params=params,
                headers=headers,
            )

            data=response.json()
            product_id=data.get('id','')
            product_summary_list=data.get('bundleProductSummaries',[])
            for item in product_summary_list:
                product_description=item.get('detail',{}).get('longDescription','')

            color_list=data.get('bundleColors',[])
            for list in color_list:
                color=list.get('name','')

            for item in product_summary_list:
                colors = item.get('detail',{}).get('colors', [])
                if colors:
                    prices = colors[0].get('sizes', [])
                    if prices:
                        price = prices[0].get('price', '')
                        price= f"{int(price)/100:.2f}"
            item={}
            item['prices']=price
            item['product_id']=product_id
            item['product_description']=product_description
            item['color']=color
            item['department']=''
            item['sub_department']=''
            item['product_type']=''

            product_item=Product_Item(**item)
            product_item.save()

            logging.info(item)

if __name__=='__main__':
    parser=Parser()
    parser.start()



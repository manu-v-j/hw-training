import requests
from parsel import Selector
import logging
from pymongo import MongoClient,errors
from settings import headers,MONGO_URL,MONGO_DB

logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]

    def start(self):
        page=1
        while True:
            params = {
                'page': str(page),
                'limit': '100',
                '0': '[object Object]',
                'product_type': 'Shirts',
            }

            response = requests.get('https://mxemjhp3rt.ap-south-1.awsapprunner.com/products/plp/v2', params=params, headers=headers)

            if response.status_code==200:
                self.parse_item(response)

            page+=1

    def parse_item(self,response):
        data=response.json()
        product_list=data.get('data',{}).get('products',[])

        if not product_list:
                return False
        
        for item in product_list:
            id=item.get('shopify_product_id','')
            handle=item.get('handle','')
            full_url=f"https://www.snitch.com/men-shirts/{handle}/{id}/buy"
            product_name=item.get('title','')
            selling_price=item.get('selling_price','')
            reglar_price=item.get('mrp','')

            if reglar_price==0.0:
                reglar_price=selling_price
            # rating=item.get('average_rating','')
            # review=item.get('total_rewiews_count','')
            size_list=item.get('variants',[])
            size=','.join([value.get('size','') for value in size_list])
            product_description=item.get('short_description','')
            fit_guide=item.get('fit','')
            images=','.join(item.get('images', []))

            print(full_url,size)
            



if __name__=='__main__':
    crawler=Parser()
    crawler.start()
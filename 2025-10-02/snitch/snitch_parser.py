import requests
from parsel import Selector
import logging
from pymongo import MongoClient,errors
from settings import headers,MONGO_URL,MONGO_DB
from snitch_item import Product_Item
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
                has_item=self.parse_item(response)
                if not has_item:
                    break

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
            regular_price=item.get('mrp','')       
            rating=item.get('average_rating','')
            size_list=item.get('variants',[])
            size=','.join([value.get('size','') for value in size_list])
            product_description=item.get('short_description','')
            style=item.get('fit','')
            collar=item.get('collar','')
            material=item.get('material','')
            images=item.get('preview_image', '')

            params = {
                'shopify_product_id': str(id),
                'page': '1',
                'limit': '10',
                'sort_by': 'is_helpful',
            }

            response = requests.get('https://mxemjhp3rt.ap-south-1.awsapprunner.com/products/reviews/v2', params=params, headers=headers)
            data=response.json()
            status_code = data.get('status', {}).get('code')
            message = data.get('status', {}).get('message', '')
            if status_code == 200 and message == "No reviews found":
                review=''
            else:
                review=data.get('data',{}).get('total_reviews_count','')
                review=str(review)
            
            #CLEAN
            if regular_price==0.0:
                regular_price=selling_price

            item={}
            item['unique_id']=id
            item['product_name']=product_name
            item['selling_price']=selling_price
            item['regular_price']=regular_price
            item['currency']='INR'
            item['rating']=str(rating)
            item['review']=review
            item['pdp_url']=full_url
            item['product_description']=product_description
            item['size']=size
            item['style']=style
            item['collar']=collar
            item['material']=material
            item['images']=images

            product_item=Product_Item(**item)
            product_item.save()
            logging.info(item)

        return True

if __name__=='__main__':
    crawler=Parser()
    crawler.start()
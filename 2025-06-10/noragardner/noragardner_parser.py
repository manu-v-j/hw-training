import requests
from parsel import Selector
from settings import *
from pymongo import MongoClient
import json
import re


class Crawler:

    def __init__(self): 
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_DETAIL]

    def start(self):
        for item in self.db[COLLECTION].find():
            url = item.get("link") 
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.parse_item(response, url)      
    
    def parse_item(self, response, url):
        sel = Selector(text=response.text)

        product_name = sel.xpath("//h1[@class='h2 product-single__title']/text()").get().strip()
        sales_price_raw= sel.xpath("//span[@class='product__price']/text()  | //span[@class='product__price product__price--compare']/text()").get().strip()
        sales_price=re.search(r'\d+',sales_price_raw).group()
        script_content = sel.xpath('//script[@id="__st"]/text()').get()
        if script_content:
            rid_match = re.search(r'"rid":(\d+)', script_content)
            product_id = rid_match.group(1) if rid_match else None
        else:
            product_id = None

        script = sel.xpath("//script[@type='application/ld+json'][2]/text()").get()
        if script:
            data = json.loads(script)
            product_sku = data.get('sku','')
            brand = data.get("brand", {}).get('name','')

   
            review_url = f"https://fast.a.klaviyo.com/reviews/api/client_reviews/{product_id}/"
            params = {
                "product_id": product_id,
                "company_id": "HWxMF4",
                "limit": 5,
                "offset": 0,
                "sort": 3,
                "filter": "",
                "type": "reviews",
                "media": "false",
                "kl_review_uuid": "",
                "preferred_country": "US",
                "tz": "Asia/Calcutta"
            }
            
            response = requests.get(review_url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                reviews_list = data.get("reviews", [])
                
                if reviews_list:
                    product_info = reviews_list[0].get('product',{})
                    total_number_of_reviews = product_info.get('review_count','')
                    if int(total_number_of_reviews)>0 :
                        star_rating = product_info.get('star_rating','')
                    
                        for item in reviews_list:
                            review_title = item.get('title','')
                            review_text = item.get('content','')
                    
        

                            item={}
                            item['url']=url
                            item['product_name']=product_name
                            item['sales_price']=sales_price
                            item['product_sku']=product_sku
                            item['brand']=brand
                            item['total_number_of_reviews']=total_number_of_reviews
                            item['star_rating']=star_rating
                            item['review_title']=review_title
                            item['review_text']=review_text

                            self.collection.insert_one(item)

if __name__ == "__main__":
    crawler = Crawler()
    crawler.start()
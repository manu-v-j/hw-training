import requests
from parsel import Selector
import logging
from pymongo import MongoClient,errors
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION_CATEGORY,COLLECTION

logging.basicConfig(level=logging.INFO)

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def start(self):
        for item in self.db[COLLECTION_CATEGORY].find():
            id=item.get('id')
            start=0
            while True:
                params = {
                    'size': '51',
                    'start': str(start),
                }

                base_url=f"https://www.3m.com/snaps2/api/pcp-show-next/https/www.3m.com/3M/en_US{id}"
                print(base_url)
                response = requests.get(
                    base_url,
                    params=params,
                    headers=headers,
                )
                if response.status_code==200:
                    has_item=self.parse_item(response)
                    if not has_item:
                        break

                start+=51

    def parse_item(self,response):
        data=response.json()
        item_list=data.get('items',[])
        if not item_list:
            return False
        
        for item in item_list:
            try:
                full_url=item.get('url','')
                id=full_url.split('en_US',1)[1]
                item={}
                item['link']=full_url
                item['id']=id
                self.collection.insert_one(item)
            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {full_url}")   

        return True

if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
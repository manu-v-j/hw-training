import requests
from settings import headers,cookies,category_urls,MONGO_URL,MONGO_DB,COLLECTION
from parsel import Selector
from pymongo import MongoClient,errors
import logging
logging.basicConfig(level=logging.INFO)


class Crawler:
    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]
        self.collection.create_index("link", unique=True)

    def start(self):
        for category_url in category_urls:
            print(f"\nScraping category: {category_url}")
            page = 1
            while True:
                url = f"{category_url}?noRedirect=0&page={page}"
                print(f"Fetching page {page}: {url}")
                response = requests.get(url, cookies=cookies, headers=headers)
                has_items = self.parse_item(response)
                if not has_items:
                    print("No more items, moving to next category.")
                    break
                page += 1

    def parse_item(self,response):            
        sel = Selector(text=response.text)
        product_urls = sel.xpath("//a[@data-testid='product-card-title']/@href").getall()
        
        if not product_urls:
            return False
        
        for relative_url in product_urls:

            try:
                full_url = f"https://www.carrefour.fr{relative_url}"
                self.collection.insert_one({'link':full_url})
                logging.info(full_url)

            except errors.DuplicateKeyError:
                logging.info(f"Duplicate: {full_url}")               


        return True
    
if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
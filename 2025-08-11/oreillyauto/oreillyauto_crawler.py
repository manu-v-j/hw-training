from settings import headers, MONGO_URL, MONGO_DB, CATAEGORY_COLLECTION, COLLECTION
import requests
from parsel import Selector
from pymongo import MongoClient,errors
import re, json, json5, logging
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def extract_child_categories(self, sel):
        script_text = sel.xpath("//script[contains(text(), 'window._ost.childCategories')]/text()").get()
        if script_text:
            match = re.search(r"window\._ost\.childCategories\s*=\s*(\[.*?\]);", script_text, re.S)
            if match:
                data_str = match.group(1)
                try:
                    return json.loads(data_str)
                except json.JSONDecodeError:
                    return json5.loads(data_str)
        return []
    
    def start(self):
       for cat in self.db[CATAEGORY_COLLECTION].find():
            url = cat.get('link')
            print(f"data_value {url}")
            response = requests.get(url, headers=headers)
            sel = Selector(text=response.text)

            categories = self.extract_child_categories(sel)
            category_list = [c.get('url', '') for c in categories]

            for sub_url in category_list:
                full_url = f'https://www.oreillyauto.com{sub_url}'
                print(f" Subcategory: {full_url}")
                self.scrape_category(full_url)

    def scrape_category(self, url):
        resp = requests.get(url, headers=headers)
        sel = Selector(text=resp.text)

        page_num = 1
        last_first_link = None  

        while True:
            product_links = sel.xpath("//a[contains(@class,'product__link')]/@href").getall()

            if product_links:
                if last_first_link == product_links[0]:
                    print("Detected repeat of first page — stopping pagination.")
                    break

                last_first_link = product_links[0]

                product_links = [f"https://www.oreillyauto.com{link}" for link in product_links]
                for prod_url in product_links:
                    try:
                        self.collection.insert_one({'link': prod_url})
                    except errors.DuplicateKeyError:
                        logging.info(f"Duplicate: {prod_url}")

            else:
                sub_categories = self.extract_child_categories(sel)
                for sub in sub_categories:
                    sub_full_url = f"https://www.oreillyauto.com{sub.get('url', '')}"
                    print(f"  Inner Subcategory: {sub_full_url}")
                    self.scrape_category(sub_full_url)
                return  

            next_page_url = f"{url}?page={page_num+1}"
            print(f"Next page: {next_page_url}")
            resp = requests.get(next_page_url, headers=headers)
            sel = Selector(text=resp.text)
            page_num += 1




if __name__ == '__main__':
    crawler = Crawler()
    crawler.start()

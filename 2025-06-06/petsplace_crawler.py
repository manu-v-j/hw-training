import requests
from settings import headers,ean_lists,MONGO_URI,DB_NAME,COLLECTION,COLLECTION_FAILED
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION]
        self.failed=self.db[COLLECTION_FAILED]

    def start(self):
        for ean in ean_lists:
            page = 0
            while True:
                payload = {
                    "requests": [
                        {
                            "indexName": "PRO_Products_NL_NL",
                            "params": f"facetFilters=[\"active:Yes\"]&facets=[\"active\",\"brand\",\"category0\",\"category1\",\"category2\",\"price\",\"promo_details_special_type\",\"sub_product_group\"]&highlightPostTag=__/ais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=12&maxValuesPerFacet=10&page={page}&query={ean}&ruleContexts=[\"magento_filters\"]&tagFilters="
                        }
                    ]
                }

                url = "https://c4jtu0l6zx-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.3)%3B%20Browser%3B%20instantsearch.js%20(4.63.0)%3B%20Magento2%20integration%20(3.13.4)%3B%20JS%20Helper%20(3.16.1)"
                response = requests.post(url, headers=headers, json=payload)

                if response.status_code == 200:
                    found = self.parse_item(response, ean)
                    if not found:
                        break
                else:
                    self.failed.insert_one({'link':url})
                    
                page += 1            


    def parse_item(self, response, ean):
        data = response.json()
        result_list = data.get("results", [])
        if not result_list or not result_list[0].get("hits"):
            return False

        for result in result_list:
            hits_list = result.get("hits", [])
            for hit in hits_list:
                url = hit.get("link", "")
                if url and str(ean) in url:
                    item={}
                    item['link']=url
                    self.collection.insert_one(item)
                    logging.info(item)
        return True


if __name__ == '__main__':
    crawler = Crawler()
    crawler.start()

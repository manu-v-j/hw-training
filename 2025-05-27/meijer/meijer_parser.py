import requests
from settings import *
from pymongo import MongoClient
import re
from meijer_items import ProductItem
import logging
logging.basicConfig(level=logging.INFO)


class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URI)
        self.db=self.client[DB_NAME]
        self.collection=self.db[COLLECTION_DETAIL]

    def start(self):
        page = 1
        while page:
            url=f"https://ac.cnstrc.com/browse/group_id/L1-918?c=ciojs-client-2.64.2&key=key_GdYuTcnduTUtsZd6&i=e14167cf-a719-4007-9eb3-eda086d4084f&s=3&us=web&page={page}&num_results_per_page=52&filters%5BavailableInStores%5D=20&sort_by=relevance&sort_order=descending&fmt_options%5Bgroups_max_depth%5D=3&fmt_options%5Bgroups_start%5D=current&_dt=1748333663952"
            payload={
                        "c": "ciojs-client-2.64.2",
                        "key": "key_GdYuTcnduTUtsZd6",
                        "i": "e14167cf-a719-4007-9eb3-eda086d4084f",
                        "s": 3,
                        "us": "web",
                        "page": 1,
                        "num_results_per_page": 52,
                        "filters": {
                            "availableInStores": 20
                        },
                        "sort_by": "relevance",
                        "sort_order": "descending",
                        "fmt_options": {
                            "groups_max_depth": 3,
                            "groups_start": "current"
                        },
                        "_dt": 1748333663952
                        }
            response=requests.get(url,headers=headers,json=payload)
            if response.status_code==200:
                has_item=self.parse_item(response)
                if not has_item:
                    break

            page += 1

    def parse_item(self,response):
        data=response.json()
        response_list=data.get("response",{}).get("results",[])
        if not response_list:
            return False

        for item in response_list:
            unique_id=item.get("data",{}).get("id","")
            product_name=item.get("value","")
            grammage_quantity=re.search(r'\d+(?:\.\d+)?(?=\D*$)',product_name)
            if grammage_quantity:
                grammage_quantity=grammage_quantity.group()
            else:
                grammage_quantity=""
            match_unit=re.search(r'\b\d+(?:\.\d+)?\s*(ml|l|g|kg|oz|cl|fl)\b',product_name,re.IGNORECASE)
            grammage_unit=match_unit.group(1) if match_unit else None
            regular_price=item.get("data",{}).get("price","")
            selling_price=item.get("data",{}).get("discountSalePriceValue","")
            product_description=item.get("data",{}).get("description","")
            promotion_date=item.get("data",{}).get("priceGoodThrough","")
            promotion_valid_upto=re.findall(r'\d{4}-\d{2}-\d{2}',promotion_date)
            image_url=item.get("data",{}).get("image_url","")
            instock=item.get("data",{}).get("stockLevelStatus","")
            netcontent=item.get("data",{}).get("packageSize","")

            item={}
           
            item["unique_id"]=unique_id
            item["product_name"]=product_name
            item["grammage_quantity"]=grammage_quantity
            item["grammage_unit"]=grammage_unit
            item["regular_price"]=regular_price
            item["selling_price"]=selling_price
            item["product_description"]=product_description
            item["promotion_valid_upto"]=promotion_valid_upto
            item["image_url"]=image_url
            item["instock"]=instock
            item["netcontent"]=netcontent
            
            product_item=ProductItem(**item)
            product_item.save()
            logging.info(item)

        return True    

if __name__ == "__main__":
    parser = Parser()
    parser.start()

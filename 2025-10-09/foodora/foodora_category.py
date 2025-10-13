import requests
from parsel import Selector
import re,json
from pymongo import MongoClient
from settings import headers,base_url,MONGO_URL,MONGO_DB,CATEGORY_ID

class Category:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[CATEGORY_ID]

    def start(self):
        response = requests.get(base_url, headers=headers)
        if response.status_code==200:
            self.parse_item(response)

    def parse_item(self,response):
        sel=Selector(text=response.text)
        script_text = sel.xpath("//script[contains(text(),'window.__PRELOADED_STATE__')]/text()").get()

        if  script_text:
            match = re.search(r"window\.__PRELOADED_STATE__\s*=\s*({.*})", script_text, re.DOTALL)
            if match:
                json_str = match.group(1)

                json_str = json_str.replace("undefined", "null")  
                json_str = json_str.replace("NaN", "null")
                json_str = json_str.replace("\\u002F", "/")  

                json_str = re.sub(r",(\s*[}\]])", r"\1", json_str)

                data = json.loads(json_str)
                category_list=data.get('categories',{}).get('categoryTree',[])
                for item in category_list:
                    if item.get('children',[])==[]:
                        cate_id=item.get('id','')
                        self.collection.insert_one({'link':cate_id,'type':'cat_id'})
                    else:
                        sub_cat_list=item.get('children',[])
                        for item in sub_cat_list:
                            sub_id=item.get('id','')
                            self.collection.insert_one({'link':sub_id,'type':'sub_id'})


if __name__=='__main__':
    category=Category()
    category.start()
       
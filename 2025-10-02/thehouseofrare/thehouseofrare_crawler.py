import requests
import logging
from pymongo import MongoClient
from settings import headers,MONGO_URL,MONGO_DB,COLLECTION

logging.basicConfig(level=logging.INFO)

class Crawler:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]
        self.collection=self.db[COLLECTION]

    def start(self):
        start=0
        while True:

            params = {
                'p': 'category_handle_uFilter:"rare-rr-men-shirts"',
                'uid': 'uid-1759297095483-81114',
                'facet.multiselect': 'true',
                'variants': 'true',
                'variants.fields': 'variantId,v_Size,v_availableForSale,v_sku',
                'variants.count': '20',
                'fields': 'title,uniqueId,price,imageUrl,productUrl,meta_my_fields_main_title,handle,images,variants,meta_my_fields_sub_title,compareAtPrice,computed_discount,grouped_products,meta_custom_variant_color_image,meta_my_fields_COLOR,swatch_image_url,meta_custom_gender,meta_custom_best_price,best_price,url,v_sku,gst_saving_amount',
                'spellcheck': 'true',
                'pagetype': 'boolean',
                'start': str(start),
                'rows': '20',
                'sort': '',
            }

            response = requests.get(
                'https://search.unbxd.io/e94cac92f0f2da84ae5ca93f42a57658/ss-unbxd-aapac-prod-shopify-houseofrare58591725608684/category',
                params=params,
                headers=headers,
            )
            data=response.json()
            product_list=data.get('response',{}).get('products',[])

            if not product_list:
                break

            for item in product_list:
                url=item.get('productUrl','')
                full_url=f"https://thehouseofrare.com/collections/rare-rr-men-shirts/{url}"
                
                self.collection.insert_one({'link':full_url})

                logging.info(full_url)
            
            start+=20


if __name__=='__main__':
    crawler=Crawler()
    crawler.start()
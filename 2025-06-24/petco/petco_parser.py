from parsel import Selector
import json
import logging
from settings import MONGO_URI,MONGO_DB,COLLECTION_DETAILS
from petco_items import ProductItem
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        pass

    def start(self):
        with open("/home/user/Hashwave/2025-06-24/petco/pdp.html",'r') as f:
            html=f.read()
            self.parse_item(html)

    def parse_item(self,html):
        sel=Selector(text=html)
        script=sel.xpath("//script[@type='application/ld+json']/text()").get()
        data=json.loads(script)
        data_one=data[1]
        brand=data_one.get("brand","").get("name","")
        pdp_url=data_one.get("url","")
        product_description=data_one.get("description","")
        rating=data_one.get("aggregateRating",{}).get("ratingValue","")
        review=data_one.get("aggregateRating",{}).get("reviewCount","")
        breadcrumb=sel.xpath("//ul[@class='Breadcrumbs-styled__BreadcrumbContainer-sc-c1679431-0 hpGLvC']/li/a/text()").getall()
        nutritions=sel.xpath("//div[@class='details-tab-styled__GuaranteedAnalysisContainer-sc-400135db-7 NLDAL']/p/text()").get()
        ingredients=sel.xpath("//div[@class='details-tab-styled__IngredientContainer-sc-400135db-6 ghVVpS']/p/text()").get()
        varient_product=data_one.get("hasVariant",[])
        for item in varient_product:
            product_name=item.get("name","")
            selling_price=item.get("offers",{}).get("price","")
            currency=item.get("offers",{}).get("priceCurrency","")
            size=item.get("size","")
            product_sku=item.get("sku","")
            image_url=item.get("image",[])

            items={}
            items['product_name']=product_name
            items['brand']=brand
            items['selling_price']=selling_price
            items['currency']=currency   
            items['product_sku']=product_sku
            items['size']=size
            items['pdp_url']=pdp_url
            items['product_description']=product_description
            items['breadcrumb']=breadcrumb
            items['rating']=rating
            items['review']=review
            items['image_url']=image_url
            items['nutritions']=nutritions
            items['ingredients']=ingredients

            product_item=ProductItem(**items)
            product_item.save()
            logging.info(items)





if __name__=='__main__':
    parser=Parser()
    parser.start()
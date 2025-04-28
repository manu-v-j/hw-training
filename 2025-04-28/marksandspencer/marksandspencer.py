import requests
from parsel import Selector
import re

class Markandspencer:
    def __init__(self):
        self.url='https://www.marksandspencer.com/l/women/dresses'

    def parser(self):
        response=requests.get(self.url)
        selector=Selector(response.text)
        products=selector.xpath('//div[@class="product-card_rootBox__BcM9P"]')
        category_name=selector.xpath("//p[contains(@class,'eco-box_ecoBox__50nux')]/text()").getall()
        pagination_link = selector.xpath('//a[@class="pagination_trigger__YEwyN"]/@href').get()
        print(f'Total categories found: {category_name}')
        print(f"pagination_link:{pagination_link}")

        for product in products:
            product_url=product.xpath('.//a[@class="product-card_cardWrapper__GVSTY"]/@href').get()
            product_url='https://www.marksandspencer.com'+product_url
            content=self.properties(product_url)


    def properties(self,content):
        response=requests.get(content)
        selector=Selector(response.text)

        unique_id=selector.xpath('//div[contains(@class,"pdp-template")]/p/text()[2]').get()
        brand_name = selector.xpath('//div[contains(@class, "product-intro_left")]//p[contains(@class, "brand-title_title")]/text()').get()
        product_name=selector.xpath('//div[@class="product-intro_slot__MH6jv"]/h1/text()').get()
        selling_price=selector.xpath('//div[contains(@class,"product-intro_priceWrapper")]/p/text()').get()
        description=selector.xpath("//div[contains(@class, 'eco-box_ecoBox__50nux')]/p[@class='media-0_textSm__Q52Mz']/text()").get()
        breadcrumps=selector.xpath("//li[contains(@class,'breadcrumb')]//a/text()").getall()
        product_url=content
        currency=selling_price[0] if selling_price else None
        color = selector.xpath('//p[contains(@class,"selector-group_legend")][span[1][normalize-space(text())="Colour"]]/span[2]/text()').get()
        raw_list=selector.xpath("//span[contains(@class,'media-0_body__yf6Z_')]/text()").getall()
        sizes = [item for item in raw_list if re.fullmatch(r'\d+', item)]
        aria_label = selector.xpath("//div[contains(@class, 'star-rating_wrapper__')]/@aria-label").get()
        if aria_label:
            match=re.search(r'Average rating:\s*([0-9.]+)', aria_label)
            rating=float(match.group(1))
           
        raw_reviews=selector.xpath("//span[contains(@class,'media-0_textSm__Q52Mz media-0_strong__aXigV')]/text()").get()
        reviews=re.search('\d+',raw_reviews)
        if reviews:
            reviews=int(reviews.group(0))

        style=selector.xpath("//div[p[contains(text(), 'Fit and style')]]/div[@class='eco-box_ecoBox__50nux eco-box_ml__iGhc6 product-details_flexRow__iPTG4']/p[contains(@class, 'product-details_dimension__dy_UN')]/text()").getall()
        care_instructions=selector.xpath("//p[contains(@class,'product-details_careText__t_RPG')]/text()").getall()
        images = selector.css('button.product-imagery-gallery_clickableImage__2kzyJ img::attr(srcset)').getall()
        composition=selector.xpath("//p[contains(text(),'Composition')]/following-sibling::p[@class='media-0_textSm__Q52Mz']/text()").get()

        print(rating)

obj=Markandspencer()

obj.parser()    
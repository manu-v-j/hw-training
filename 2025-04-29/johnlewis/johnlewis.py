import requests
from parsel import Selector
import re

class Johnlewis:   
        def parser(self):
            with open("2025-04-29/johnlewis/Men's T-Shirts _ John Lewis & Partners.html", 'r', encoding='utf-8') as file:
                html_content = file.read()

            selector = Selector(text=html_content)
            products = selector.xpath("//article[contains(@class,'product-card_c-product-card__IiVba')]")
            pagination_link=selector.xpath("//a[contains(@class,'Pagination_c')]/@href").getall()
            category_name=selector.xpath("//li[contains(@class,'DesktopMenuItem')]/a/text()").getall()

            for product in products:
                product_url = product.xpath(".//a[@class='product-card_c-product-card__link___7IQk']/@href").get()

            with open("2025-04-29/johnlewis/pdp.html",'r',encoding='utf-8') as file:
                 pdp_content=file.read()

            selector=Selector(text=pdp_content)
        
            unique_id=selector.xpath("//div[contains(@class,'ProductDescriptionAccordion')]/p/strong/text()[2]").get()
            product_name=selector.xpath("//li[contains(@class,'breadcrumbs-carousel')][3]/a/text()").get()
            specifications=selector.xpath("//dt[contains(@class,'productSpecificationListValue')]/text()").getall()
            brand=specifications[0]
            category=selector.xpath("//li[contains(@class,'breadcrumbs-carousel')][2]/a/text()").get()
            selling_price=selector.xpath("//span[contains(@class,'price_price')]/text()").get()
            promotion_description=selector.xpath("//span[@class='Title_otherBrand__TOt2R']/following-sibling::text()").get()
            breadcrumb=selector.xpath("//li[contains(@class,'breadcrumbs-carousel')]/a/text()").getall()
            product_description = selector.xpath("normalize-space(//div[contains(@class,'ProductDescriptionAccordion_descriptionContent')])").get()
            currency=selling_price[0] if selling_price else None
            color=selector.xpath("//h4[@data-testid='colourlist:label']/span[2]/text()").get()
            size=selector.xpath("//li[contains(@class,'size_c-sizeItem')]/a/text()").getall()
            raw_rating=selector.xpath("//span[contains(@class,'rating_visuallyHidden')]/text()[3]").get()
            rating=re.search(r'\d+.\d+',raw_rating)
            if rating:
                 rating=rating.group()
            rawreview=selector.xpath("//span[contains(@class,'RatingAndReviews')]/text()").get()
            review=re.search(r'\d',rawreview)  
            if review:
                review=review.group()
            care_instructions=specifications[3]
            images=selector.xpath("//img[contains(@class,'ImageMagnifier_small-image')]/@src").getall()
            composition=specifications[1]
            print(images)


object = Johnlewis()
object.parser()

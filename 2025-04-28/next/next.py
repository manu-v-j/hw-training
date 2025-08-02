import requests
from parsel import Selector

class NextScraper:

    def parser(self):
        # Open the saved HTML file
        with open('2025-04-28/next/next.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Create a selector object
        selector = Selector(text=html_content)

        products=selector.xpath("//div[contains(@id,'plp-product-summary-entrypoint')]")
        categories=selector.xpath("///div[contains(@class,'header-g1t0hk')]/text()").getall()
        
        for product in products:
            product_url=product.xpath(".//a[contains(@class, 'MuiCardMedia-root')]/@href").get()
            content=self.properties(product_url)


    def properties(self,content):
        response=requests.get(content)
        selector=Selector(response.text)
        unique_id=selector.xpath("//span[contains(text(),'Product Code')]/following-sibling::span/text()").get()
        selling_price=selector.xpath("//div[contains(@class,'MuiTypography-root')]/span/text()").get()
        premotion_description=selector.xpath("//h1[contains(@class,'MuiTypography-root')]/text()").get()
        pdp_url=content
        product_description=selector.xpath("//div[contains(@class,'MuiTypography-body2')]/p/text()").get()
        currency=selling_price[0]
        color = selector.xpath("//span[contains(@class,'MuiTypography-body3') or @class='pdp-css-6pogpz']/text()").get()
        size=""
        raw_rating = selector.xpath("//figure[contains(@class, 'pdp-css-1uitb0y')]/@aria-label").get()
        rating=raw_rating.split()[0] 
        reviews=selector.xpath("//span[contains(@class,'pdp-css-1brzoas')]/text()[2]").get()
        material_composition=selector.xpath("//ul/li/text()").getall()
        style=""
        care_instructions=""
        features=""
        images=selector.xpath("//div[contains(@class,'carousel-slide')]/img/@src").getall()
        composition=selector.xpath("//p[contains(@class,'MuiTypography-body2')]/text()[3]").get()

        


obj=NextScraper()
obj.parser()
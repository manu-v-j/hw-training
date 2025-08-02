import requests
from parsel import Selector
import json
import re
import logging
logging.basicConfig(level=logging.INFO)

headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'priority':'u=0,i',
    'referer':'https://www.tesco.com/groceries/en-GB',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
#######################################CRAWLER#########################################
count=0
page=1

while True:
    url=f"https://www.tesco.com/groceries/buylists/finest-food/all-products/finest-ready-meals?count=24&page={page}#top"
    response=requests.get(url,headers=headers)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[contains(@class,'styled__ImageContainer-sc-1fweb41-0')]/@href").getall()
    if not product_urls:
        break
    for url in product_urls:
        logging.info(url)
        count+=1
        print(count)
    page+=1

###################################PARSER###########################################
with open('/home/user/Hashwave/2025-07-18/product_link.json','r') as f:
        product_list = json.load(f)
        for url in product_list:
            url="https://www.tesco.com/groceries/en-GB/products/320592270?_gl=1*1i8bfcz*_up*MQ..*_ga*MTg4NDAzNTc2My4xNzUzMDc5Njk1*_ga_33B19D36CY*czE3NTMwNzk2OTQkbzEkZzAkdDE3NTMwNzk2OTQkajYwJGwwJGgyNTA2MDcwOTU."
            response=requests.get(url,headers=headers)
            sel=Selector(text=response.text)
            product_name=sel.xpath("//h1[@data-auto='pdp-product-title']/text()").get()
            regular_price_raw=sel.xpath("//p[contains(@class,'ddsweb-text ac8f2b_FKk1BW_priceText')]/text()").get()
            if regular_price_raw:
                regular_price= regular_price_raw.replace('Â', '').replace('£', '').strip()
                regular_price = "{:.2f}".format(float(regular_price))
            currency="pound"
            pdp_url=url
            product_description=sel.xpath("//h3[contains(text(), 'Description')]/following-sibling::div[contains(@class, 'OobGYfu9hvCUvH6')]/span/text()").getall()
            product_description=''.join([description for description in product_description])
            ingredients=sel.xpath("//h3[contains(text(), 'Ingredients')]/following-sibling::div[contains(@class, 'OobGYfu9hvCUvH6')]/p//text()").getall()
            ingredients=''.join([item for item in ingredients])
            allergens=sel.xpath("//h3[contains(text(), 'Allergy Information')]/following-sibling::div[contains(@class, 'OobGYfu9hvCUvH6')]/span/text()").get()
            if product_name:
                match = re.search(r'(\d+(?:\.\d+)?)(\s?[a-zA-Z]+)', product_name)
                if match:
                    grammage_quantity=match.group(1)
                    grammage_unit=match.group(2)

            nutritions = {}
            rows = sel.xpath("//table[contains(@class,'product__info-table')]//tbody/tr")
            for row in rows:
                label = row.xpath("./th/text()").get()
                per_100g = row.xpath("./td[1]/text()").get()
                per_pack = row.xpath("./td[2]/text()").get()
                if label and per_100g and per_pack:
                    nutritions[label.strip()] = {
                        "per_100g": per_100g.strip(),
                        "per_pack": per_pack.strip()
                    }

            storage_instructions=sel.xpath("//div[@id='accordion-panel-storage']//div[@class='OobGYfu9hvCUvH6']/text()").get()
            if storage_instructions:
                storage_instructions=storage_instructions.strip()
            preparationinstructions=sel.xpath("//h3[contains(text(),'Cooking Instructions')]/following-sibling::div[@class='OobGYfu9hvCUvH6']//text()").getall()
            preparationinstructions=' '.join([instruction for instruction in preparationinstructions])
            recycling_information=sel.xpath("//div[@id='accordion-panel-recycling-info']//following-sibling::div[@class='OobGYfu9hvCUvH6']/text()").get()
            color=sel.xpath("//img[contains(@class,'ac8f2b_o7KQoq_dataLayerimage')]/@alt").getall()
            size=sel.xpath("//span[contains(@class,'ddsweb-button__inner-container b6325c_8WKJvW_container')]/text()").getall()
            material=sel.xpath("//h3[contains(text(), 'Material')]/following-sibling::div/span[@class='QhtPR2LZPKOnKcE']/text()").get()
            address=sel.xpath("//h3[contains(text(),'Manufacturer Address')]/following-sibling::div[1]//span/text()").getall()
            manufacturer_address = ''.join([line.strip() for line in address if line.strip()])
            return_address=sel.xpath("//h3[contains(text(),'Return to')]/following-sibling::div[@class='OobGYfu9hvCUvH6']/span/text()").getall()
            rating = sel.xpath("//p[contains(@class,'ddsweb-rating__hint')]/text()").get()
            rating=rating.replace(' stars','')
            review=sel.xpath("//a[@class='ddsweb-link ddsweb-link__anchor ddsweb-link__inline d7d27c_8WKJvW_inlineLink d7d27c_8WKJvW_link']/text()").get()
            if review:
                review=review.replace(' Reviews','')
            breadcrumbs=sel.xpath("//div[contains(@class,'ddsweb-breadcrumb__item')]//text()").getall()
            image_url=sel.xpath("//img[contains(@class,'ddsweb-responsive-image__image ')]/@src").get()
            date=sel.xpath("//p[contains(@class,'ddsweb-value-bar__terms fcea0c_l011wq_termsText')]/text()").get()
            # dates = re.findall(r"\d{2}/\d{2}/\d{4}", date)

            # if len(dates) == 2:
            #     offer_valid_from = dates[0]
            #     offer_valid_upto = dates[1]

            print(material)
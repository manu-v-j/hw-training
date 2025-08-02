import requests
from parsel import Selector
from urllib.parse import urljoin
import re
import logging
logging.basicConfig(level=logging.INFO)

headers = {
    "authority": "styleunion.in",
    "method": "GET",
    "path": "/collections/womens-dresses",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": "\"cacheable:58e66fce333102505eb36ada01ed4dc1\"",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

################CRAWLER#########################################
page = 1
count = 0
seen = set()
product_links = []
while True and count<=100:
    base_url = f"https://styleunion.in/collections/womens-dresses?page={page}"
    response = requests.get(base_url, headers=headers)

    if response.status_code != 200:
        break

    sel = Selector(text=response.text)
    product_urls = sel.xpath("//div[@class='product-info']/a/@href").getall()

    if not product_urls:
        print(f"No more products found on page {page}. Stopping.")
        break

    new_urls_found = False 
    for product_url in product_urls:
        full_url = f"https://styleunion.in{product_url}"
        if full_url not in seen:
            seen.add(full_url)
            product_links.append(full_url)
            count += 1
            logging.info(count)
            print(full_url)
            new_urls_found = True

    if not new_urls_found:
        break
    page += 1


#####################PARSER######################################
for full_url in product_links:
    response=requests.get(full_url,headers=headers)
    if response.status_code==200:
        sel=Selector(text=response.text)
        product_name=sel.xpath("//h1[@class='product__section-title product-title']/text()").get()
        regular_price_raw=sel.xpath("//span[contains(@class, 'price-item')]/text()").get()    
        if regular_price_raw:
            regular_price = regular_price_raw.replace('₹', '').strip()  
            currency=re.search('₹',regular_price_raw).group()
        size_list=sel.xpath("//label[@class='swatches__form--label']/text()").getall() 
        size=[item.strip() for item in size_list if item.strip()]
        color=sel.xpath("//span[@class='swatches__color-name']/text()").getall()
        material=sel.xpath("//div[@class='desc_inner acc__card active']/div[2]/strong/following-sibling::text()[1]").get()
        if material:
            material=material.strip()
        pattern=sel.xpath("//div[@class='desc_inner acc__card active']/div[4]/strong/following-sibling::text()[1]").get()
        if pattern:
            pattern=pattern.strip()
        clothing_length=sel.xpath("//div[@class='desc_inner acc__card active']/div[5]/strong/following-sibling::text()[1]").get()
        if clothing_length:
            clothing_length=clothing_length.strip()
        neck_style=sel.xpath("//div[@class='desc_inner acc__card active']/div[6]/strong/following-sibling::text()[1]").get()
        if neck_style:
            neck_style=neck_style.strip()
        clothing_fit=neck_style=sel.xpath("//div[@class='desc_inner acc__card active']/div[8]/strong/following-sibling::text()[1]").get()
        if clothing_fit:
            clothing_fit=clothing_fit.strip()
        product_description=sel.xpath("//div[@class='acc__title'][h3[text()='Description']]/following-sibling::div[@class='acc__panel']//text()").getall()
        product_description = ' '.join(part.strip() for part in product_description if part.strip())
        care_instructions=sel.xpath("//div[@class='acc__title'][h3[text()='Wash and Care']]/following-sibling::div[@class='acc__panel']//text()").get()
        if care_instructions:
            care_instructions=care_instructions.strip()
        image_url=sel.xpath("//div[@class='box-ratio']/img/@src").getall()
        image_url = ['https:' + url for url in image_url]
        product_sku=sel.xpath("//span[@class='variant_sku']/text()").get()
        logging.info(product_sku)
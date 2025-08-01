from curl_cffi import requests
from parsel import Selector
import base64


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://shop.rewe.de/",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"129.0.6668.58\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"129.0.6668.58\", \"Not=A?Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"129.0.6668.58\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-ch-ua-platform-version": "\"5.15.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

############################CRAWLER######################################
# product=[]
# page=1
# while True:
#     url=f"https://shop.rewe.de/c/monatshighlights/?source=homepage-category&page={page}"
#     response=requests.get(url,headers=headers,impersonate='chrome')
#     sel=Selector(text=response.text)
#     product_urls=sel.xpath("//a[contains(@class,'productDetailsLink')]/@href").getall()
#     if not product_urls:
#         break
#     print(url)
#     for url in product_urls:
#         full_url=f'https://shop.rewe.de{url}'
#         # print(full_url)
#     page+=1

###########################PARSER##########################################
url="https://shop.rewe.de/p/faber-castell-bleistift-grip-2001-2-stueck/2140470"
response=requests.get(url,headers=headers,impersonate='chrome')
sel=Selector(text=response.text)
product_name=sel.xpath("//h1[@class='pdpr-Title']/text()").get()
brand=sel.xpath("//span[contains(@class,'pdpr-Brand__Link__Content')]/span/text()").get()
country_of_origin=sel.xpath("//h3[contains(text(),'Ursprungsland')]/following-sibling::text() | //h3[contains(text(),'Ursprung')]/following-sibling::text()").get()
selling_price=sel.xpath("//meso-data[@data-price]/@data-price").get()
product_description= sel.xpath("//div[@class='pdpr-ArticleNumber']/text() | //div[@class='pdpr-ProductContent__Content']//text()").getall()
breadcrumb=sel.xpath("//a[contains(@class,'lr-breadcrumbs__link')]//text()").getall()
ingredients=sel.xpath("//h3[contains(text(),'Zutaten')]/following-sibling:: text()").get()
nutritions={}
rows=sel.xpath("//table[contains(@class,'pdpr-NutritionTable')]//tbody/tr")
for row in rows:
    key = row.xpath("./td[1]/text()").get().strip()
    value = row.xpath("./td[2]/text()").get().strip()
    nutritions[key] = value
storage_instructions=sel.xpath("//h3[contains(text(),'Aufbewahrungshinweise')]/following-sibling:: text()").get()
image_url=sel.xpath("//div[@class='pdsr-ResponsiveImage']/picture/img/@src").getall()
print(product_description)

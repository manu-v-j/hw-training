import requests
from parsel import Selector
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'OptanonAlertBoxClosed=2025-08-11T08:32:03.030Z; XSRF-TOKEN=7b67ecbf-759f-4200-ad29-e453dcedf735; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Sep+26+2025+10%3A04%3A19+GMT%2B0530+(India+Standard+Time)&version=202508.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=83a56ff1-cc91-413d-b261-4750df12cf1d&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false&intType=2&geolocation=%3B',
}

############################CRAWLER########################################
product=[]
base_url='https://shop.billa.at/kategorie/brot-und-gebaeck-13766'
while len(product)<500:
    response = requests.get(base_url,  headers=headers)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[@class='ws-product-tile__link']/@href").getall()
    if not product_urls:
        break
    print(base_url)
    for url in product_urls:
        full_url=f"https://shop.billa.at{url}"
        print(full_url)
        product.append(full_url)

    next_page=sel.xpath("//li[contains(@class,'ws-pagination__next')]/a/@href").get()
    if next_page:
        base_url=f"https://shop.billa.at{next_page}"
    else:
        print("No more pages. Finished.")
        break

print(len(product))

#############################PARSER#######################################
base_url="https://shop.billa.at/produkte/ja-natuerlich-kaisersemmel-00480904"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//h1[contains(@class,'ws-product-title')]/text()").get()
brand=sel.xpath("//a[@data-test='product-information-brand']/text()").get()
netweight=sel.xpath("//ul[contains(@class,'ws-product-information__piece-description')]/li/text()").get()
selling_price=sel.xpath("//div[contains(@class,'ws-product-price-type__value')]/text()").get()
product_description=sel.xpath("//div[contains(@class,'ws-product-slug-main__description-short')]//text()").getall()
ingredients=sel.xpath("//div[text()='Zutaten']/following-sibling::div/div//text()").getall()
allergens=sel.xpath("//div[text()='Allergene']/following-sibling::div//text()").getall()

nutritional_information = {}
rows = sel.xpath("//table[@class='ws-product-detail-nutrition-table']/tbody/tr")
for row in rows:
    key = row.xpath(".//th/text()").get()
    if key:
        key = key.strip()
    value = row.xpath(".//td/text() | .//td/br/following-sibling::text()").getall()
    value = " ".join([v.strip() for v in value])
    nutritional_information[key] = value

country_of_origin=sel.xpath("//div[text()='Produktionsland']/following-sibling::div/text()").get()
manufacturer_address=sel.xpath("//div[text()='Hersteller']/following-sibling::div//text()").getall()
label_information=sel.xpath("//div[text()='Labelinformationen']/following-sibling::div/div//text()").getall()
breadcrumb = sel.xpath("//ul[contains(@class,'ws-category-tree-navigation')]/li//span[not(@class)]/text()").getall()
image_url=sel.xpath("//img[contains(@class,'ws-product-image ')]/@src").get()
print(image_url)
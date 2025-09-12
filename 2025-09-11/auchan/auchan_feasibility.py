import requests
from parsel import Selector
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.auchan.fr/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'connect.sid=s%3Aol33HnyIpFO31VaZ1OKpoKyiLXDpYRxk.mkhvyA7n61sCk4NtaM%2FrJiGWGLRa42tau1nWmNjlV3Y; lark-consent=0; lark-consentId=8b25516c-0550-4512-ad48-1b34831f2d8f; lark-session=236442cb-2d62-4c02-ad37-6be60ca82dad+1757585390731; lark-browser-uuid=25c3e8c2-cead-4749-83bf-c08b5590b3a5; lark-dynamic-notification=1; OptanonAlertBoxClosed=2025-09-11T10:10:27.852Z; eupubconsent-v2=CQXkaSQQXkaSQAcABBFRB7FsAP_gAEPgAChQLlAABCAEAAAAAAAAAIAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAAAAAAAEABAAAAAAAQAAAAAAAAAAACAAACAABKT-9IEd_x8v4v4_F7pE2-eS1n_pGvp6D9-Yns_dBm19_baffzPn__rl_e7X_vf_n37v943H77v____f_-7_wXIAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwWAhJICViQQBcQTQAAEAAAUQIECKRswBBQGaLQXgyfRkaYBg-YJklMgyAJgjIyTYhN-Ew8chRCghyE2KWAAAAA.f_wACHwAAAAA; lark-ab=1; to_consent_v2={%22createAt%22:1757565628647%2C%22value%22:%22optin%22}; valiuz-id=236442cb-2d62-4c02-ad37-6be60ca82dad; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+11+2025+15%3A42%3A04+GMT%2B0530+(India+Standard+Time)&version=202503.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=46dfa01f-2b7f-4d23-b7ef-d798bf89dbb2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1%2CV2STACK42%3A1&hosts=H41%3A1%2CH35%3A1%2CH47%3A1%2CH48%3A1%2CH185%3A1%2CH34%3A1%2CH39%3A1%2CH138%3A1%2CH139%3A1%2CH107%3A1%2CH3%3A1%2CH141%3A1%2CH169%3A1%2CH70%3A1%2CH8%3A1%2CH142%3A1%2CH71%3A1%2CH72%3A1%2CH179%3A1%2CH36%3A1%2CH11%3A1%2CH182%3A1%2CH112%3A1%2CH113%3A1%2CH151%3A1%2CH77%3A1%2CH153%3A1%2CH154%3A1%2CH16%3A1%2CH79%3A1%2CH80%3A1%2CH20%3A1%2CH82%3A1%2CH83%3A1%2CH84%3A1%2CH181%3A1%2CH178%3A1%2CH85%3A1%2CH158%3A1%2CH24%3A1%2CH162%3A1%2CH91%3A1%2CH26%3A1%2CH57%3A1%2CH28%3A1%2CH95%3A1%2CH96%3A1%2CH31%3A1%2CH101%3A1%2CH166%3A1%2CH102%3A1%2CH120%3A1%2CH100%3A1%2CH6%3A1%2CH170%3A1%2CH62%3A1%2CH186%3A1%2CH118%3A1&genVendors=V20%3A1%2CV49%3A1%2CV46%3A1%2CV13%3A1%2CV32%3A1%2CV7%3A1%2CV29%3A0%2CV6%3A1%2CV30%3A1%2CV36%3A1%2CV34%3A1%2CV14%3A1%2CV28%3A1%2CV51%3A1%2CV31%3A1%2CV26%3A1%2CV11%3A1%2CV18%3A1%2CV37%3A1%2CV15%3A1%2CV21%3A1%2CV5%3A1%2CV4%3A1%2CV17%3A1%2CV23%3A1%2C&intType=1&geolocation=IN%3BKL&AwaitingReconsent=false',
}

#########################################CRAWLER###############################

products = []
page = 1

while len(products) < 300:
    base_url = f'https://www.auchan.fr/jouets-jeux-video-loisirs/jeux-jouets/ca-6856153?page={page}'
    print(f"Scraping page {page}: {base_url}")
    
    response = requests.get(base_url, headers=headers)
    sel = Selector(text=response.text)
    
    product_urls = sel.xpath("//a[contains(@class,'product-thumbnail__details-wrapper--column')]/@href").getall()
    print(f"Found {len(product_urls)} products on page {page}")
    
    if not product_urls:
        print("No more products found, stopping.")
        break
    
    for url in product_urls:
        full_url = f"https://www.auchan.fr{url}"
        if full_url not in products:
            products.append(full_url)
        if len(products) >= 300:
            break
    
    page += 1

print(f"\nCollected {len(products)} product URLs.")

#############PARSER##################################################
base_url="https://www.auchan.fr/playmobil-71077-couple-de-maries/pr-C1599023"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
country=''
retail_chain=''
brand=sel.xpath("//bold[@class='offer-selector__brand']/text()").get()
product_name=sel.xpath("//div[@class='offer-selector__name--large']/h1/text()").get()
pack_size=''
price_per_pack=sel.xpath("//div[contains(@class,'product-price--large')]/text()").get()
price_per_kg_l=''
promotion_description=sel.xpath("//span[@class='product-discount-old-price__sticker']/text()").get()
product_description=sel.xpath("//div[@class='product-description__content-wrapper']/div/text()").get()

ingredients=sel.xpath("//h5[contains(text(),'Ingrédients')]/following-sibling::div/span/text()").get()
legal_name=sel.xpath("//h5[contains(text(),'Dénomination légale de vente')]/following-sibling::div/span/text()").get()

category_path=sel.xpath("//span[@class='site-breadcrumb__item']/a/text()").getall()
category_path=' '.join(category_path)
product_image_url=sel.xpath("//div[@class='product-zoom__item galleryItem selected']/img/@src").get()
texts = sel.xpath("//span[contains(text(),'Réf / EAN :')]/following-sibling::div//text()").getall()
product_code = " ".join(t.strip() for t in texts if t.strip())

values=sel.xpath("//tr[@class='nutritionals__row nutritionals__row--header']/th/text()").getall()
if values:
    value_1=values[0]
    value_2=values[1]
    value_3=values[2]

nutritional={}
raws=sel.xpath("//tr[@class='nutritionals__row']")
for row in raws:
    key=row.xpath('./td[@scope="row"]/text()').get()
    label_one=row.xpath('./td[@class="nutritionals__cell"][2]/text()').get()
    label_two=row.xpath('./td[@class="nutritionals__cell"][3]/text()').get()

    key = key.strip() if key else ''
    label_one = label_one.strip() if label_one else ''
    label_two = label_two.strip() if label_two else ''

    # print(f"{key}: {label_one} | {label_two}")

print(product_name)
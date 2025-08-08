import requests
from parsel import Selector
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Fri, 01 Aug 2025 12:11:43 GMT',
    'if-none-match': 'W/0e8c5a5220a2eecc19831601b6851e39',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}

#############################################CRAWLER#################################
url="https://www.lancasterfarming.com/classifieds/farm_equipment/?l=15"
while True:
    response=requests.get(url,headers=headers)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//div[@id='classifieds-results-container']//div[@class='image']/a/@href").getall()
    if not product_urls:
        break
    for product in product_urls:
        full_url=f'https://www.lancasterfarming.com/{product}'
    next_page=sel.xpath("//li[@class='next']/a/@href").get()
    if next_page:
        url=f'https://www.lancasterfarming.com/{next_page}'
    else:
        break

################################PARSER############################

url='https://www.lancasterfarming.com/classifieds/farm_equipment/new-used-equipment/pdfdisplayad_76d85667-44c4-570d-aed6-70e6e0dc421e.html'
response = requests.get(url,
        headers=headers,
    )
sel=Selector(text=response.text)
product_name=sel.xpath("//h1[@class='title']/text()").get()
image=sel.xpath("//img[@class='img-responsive full']/@src").get()
details=sel.xpath("//div[@class='panel-body']/pre/text()").get()
category=sel.xpath("//h4[contains(text(),'Categories')]/following-sibling:: ul//a/text()").get()
selling_price=sel.xpath("//span[@class='asset-price']/text()").get()
phone_number=sel.xpath("//div[@class='card-phone']/text()").getall()
website=sel.xpath("//a[span[text()='Website']]/@href").get()

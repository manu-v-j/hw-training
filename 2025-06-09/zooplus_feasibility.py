import requests
from parsel import Selector
import re
headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

##############################CRAWLER##############################

# ean_list=[3182551055672,3182551055788,3182551055719,3182551055825,3182550704625,3182550706933,9003579013793,9003579013861,9003579008362,5425039485010,5425039485034,
#           5425039485317,5407009646591,5407009640353,5407009640391,5407009640636,5407009641022,5060184240109,5060184240598,5060184240703,5060184240512]

# for ean in ean_list:
#     url=f"https://www.zooplus.nl/search/results?q={ean}"
#     response=requests.get(url,headers=headers)
#     sel=Selector(text=response.text)
#     product_urls=sel.xpath("//a[@data-zta='product-info']/@href").getall()
#     print(product_urls)

###############################PARSER##############################
response=requests.get('https://www.zooplus.nl/shop/honden/hondenvoer_droog/royal_canin_size/mini/1995957?activeVariant=1995957.0',headers=headers)
sel=Selector(text=response.text)

product_name=sel.xpath("//h1[@class='z-h1 ProductTitle_title__FNHsJ']/text()").get()
currency_price=sel.xpath("//span[@class='z-product-price__amount']/text()").get()
selling_price=re.search(r'\d+\,\d+',currency_price).group()
currency=re.search(r'€ ',currency_price).group()
grammage_quantity_unit=sel.xpath("//div[@data-zta='ProductTitle__Subtitle']/text()").get()
grammage_quantity=re.search(r'\d+',grammage_quantity_unit).group()
grammage_unit=re.search(r'(kg|g|gr|ml|l)',grammage_quantity_unit).group()
product_description=sel.xpath("//div[@data-zta='productDescription']/following-sibling::p//text()").getall()
product_description = ' '.join([x.strip() for x in product_description if x.strip()])
breadcrumb=sel.xpath("//li[@class='z-breadcrumb__item']//text()").getall()
breadcrumb=[item.strip() for item in breadcrumb if item.strip()]
image_url=sel.xpath("//div[@class='ImageSwiperPicture_imageSwiperPictureWrapper__oINC_']/span/img/@src").getall()
nmaterial_composition=sel.xpath("//div[@class='anchors_anchorsHTML___2lrv']/strong[text()='Samenstelling']/following-sibling::br[1]/following-sibling::text()[1]").get()
nutritions=sel.xpath("//div[@class='anchors_anchorsHTML___2lrv']/em[text()='Nutritionele toevoegingsmiddelen:']/following-sibling::br[1]/following-sibling::text()[1]").get()
percentage_discount=sel.xpath("//span[@class='z-text-badge__label']/text()").get()
review_raw = sel.xpath("//span[@class='RatingSummary_reviewNumber__xWyiT']/text()").getall()
review_text = ''.join(review_raw) 
review=re.search(r'\d+', review_text).group() 
variants_raw=sel.xpath("//div[@class='ArticleSelectionBox_title__Six69']//text()").get()
variants=re.search(r'\d+',variants_raw).group()
brand=sel.xpath("//span[@class='brand brand-rc24']/text()").get()

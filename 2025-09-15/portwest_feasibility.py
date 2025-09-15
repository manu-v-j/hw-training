import requests
from parsel import Selector
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.portwest.com/products/clothing/all-weather-accessories/79/10',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'ci_session=f2ppb8dt07lsrdmpfc4n2njmjtmqhrps; geocode_cookie=IN; _lfa=LF1.1.e938938ab0113759.1757916001613; _gid=GA1.2.1252354376.1757916003; _hjSession_2645651=eyJpZCI6ImE5NGQyNTg1LTM0MGMtNGYxMC1hYmFkLTM1MTU3MDgyNDFjZCIsImMiOjE3NTc5MTYwMDMxNjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1757916003406.514977086830530916; _hjSessionUser_2645651=eyJpZCI6IjYzNzJmMzcwLTY3YzctNTE3ZC04Nzg3LWE3ODA0ZDc4MWE3NSIsImNyZWF0ZWQiOjE3NTc5MTYwMDMxNjEsImV4aXN0aW5nIjp0cnVlfQ==; wum_61f0e0cf3c35766f924dea9dcd91215f=1; _ga_NQ0DR51GP6=GS2.1.s1757916002$o1$g1$t1757916187$j48$l0$h996401656; _ga=GA1.2.1541383472.1757916002; _gat_gtag_UA_15701874_11=1',
}
###############################CRAWLER########################
products=[]
count=0
while True:
    base_url=f"https://www.portwest.com/products/load_more_category_products/X/12/61/{count}"
    response = requests.get(base_url,headers=headers)
    print(base_url)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//h2[@class='product-title']/a/@href").getall()
    if not product_urls:
        break
    print(len(product_urls))
    for url in product_urls:
        full_url=f"https://www.portwest.com{url}"
        products.append(full_url)
        print(full_url)
    count+=12
print(len(products))

##############################PARSER###########################
base_url="https://www.portwest.com/products/view/C735/BKR"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//div[@class='col-lg-6']/div/h2/text()").get()
size=sel.xpath("//div[@class='std_titles']/text()").get()
colour=sel.xpath("//div[@class='ratings-container']/h2/text()").get()
product_description=sel.xpath("//p[@class='text-justify']/text()").get()
features=sel.xpath("//h3[text()='Features']/following-sibling :: li/text()").getall()
material=sel.xpath("//div[contains(normalize-space(text()), 'Shell Fabric')]/following-sibling::div/text()").get()
brand=''
images=sel.xpath("//img[@class='product-single-image']/@src").get()
datasheets=sel.xpath("//a[text()='Datasheets']/@href").get()
declaration_conformity_EU=sel.xpath("//a[text()='Declaration of Conformity (EU)']/@href").get()
declaration_conformity_UK=sel.xpath("//a[text()='Declaration of Conformity (UK)']/@href").get()
sizing_chart=sel.xpath("//a[text()='Sizing Chart']/@href").get()


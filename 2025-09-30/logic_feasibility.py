import requests
from parsel import Selector
import urllib.parse
import re,json

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
    # 'cookie': '_gcl_au=1.1.132975533.1759217062; kameleoonVisitorCode=urn5udkq7ebgzraz; _ga=GA1.1.2031082155.1759217085; _ga_4XHT33K1PX=GS2.1.s1759221076$o2$g1$t1759221136$j60$l0$h0; __gads=ID=75d8e4894c4a9441:T=1759218059:RT=1759221179:S=ALNI_Ma3Rs0-FiU6nPGHlcC1xNHuRdpQ8w; __gpi=UID=0000119cad103d0f:T=1759218059:RT=1759221179:S=ALNI_MZ5rrBOVrZ_biyOr3IJVug_Et2-VA; __eoi=ID=95746f482f86af0e:T=1759218059:RT=1759221179:S=AA-AfjaG70bNMrp3pp_Sres55UaB; xtvrn=$492234$; xtat492234=-; xtant492234=1; LIN_LDID=0683248e-75d5-45a0-8b71-d3888e5b0ca6; page_viewed_buy=4; cto_bundle=OwQypV9VeDd3elRoOUppZ1hVVW45dzc3UGNxZ2RXYWdwUTVvOGpKJTJGRmk4U2JSJTJGVTdBUEQ4aGxvemolMkZpQlR4T2c4RGNWM2M2Y1pqT3prWSUyQjV0NjcybUE4VE0zUlhyeG9ySmNObVZ6UEliNFVORXp6NGRDWFJFUiUyQlROOEE2RVVIazYzR1lsc2tGQ21hdWplUFN3NU9DS3hyQ2FyeGJYYzFCeHpwMERreCUyRkUyakRNa0JmMmRLbUpvNERYcDlBMldUWHdZQ2xiV2ZBekhteVdhbjVvNnpuYmxINklMJTJGM2dXcXIzbkRzNDkzS2hRUjNaSFd5YjR0OW5SQWFBY003JTJGMUplMUVEMGRiNVJYYmt1aWdnYkMlMkI0NFpETmtYZyUzRCUzRA; datadome=pJY7oVNzppZFoDFAkfRgT3G1wDgkcqnuEAKw2GMXuYKuCm3oc_WQ_hk2sBPBkirEY3YWJf9VpxKYM16HMkO5Ifb83rUjLe7HRULncft5_0Np2uZ1pb~4tAFam3JzzkaA; leads_counter_buy=1; _ga_FE4LWMCN6M=GS2.1.s1759221143$o2$g1$t1759221251$j58$l0$h0',
}

page = 1  
product=[]
while len(product)<=300:
    base_url=f'https://www.logic-immo.com/classified-search?distributionTypes=Buy&estateTypes=House,Apartment&locations=POCOFR4452&priceMin=200000&projectTypes=Resale&page={page}'
    response = requests.get(
    base_url,
    headers=headers,
)
    print(base_url)
    sel = Selector(text=response.text)
    product_urls = sel.xpath("//button[@data-base]/@data-base").getall()

    if not product_urls:
        print("No more products found. Stopping.")
        break

    for url in product_urls:
        full_url = urllib.parse.unquote(url)
        product.append(product)

        print(full_url)

    page += 1
print(len(product))
base_url="https://www.logic-immo.com/detail-vente-249178873.htm"

# for base_url in product:
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
property_price=sel.xpath("//span[@data-testid='program-price-value']/text()").get()
city=sel.xpath("//div[@class='css-1ytyjyb']/text()").getall()
size=sel.xpath("//div[@class='css-7tj8u'][3]/span/text()").getall()
script_text = sel.xpath(
    '//script[contains(text(),"__UFRN_LIFECYCLE_SERVERREQUEST__")]/text()'
).get()


match = re.search(r'JSON\.parse\("(.+)"\)', script_text)
if match:
    raw_json = match.group(1)  
    cleaned_json = raw_json.encode("utf-8").decode("unicode_escape")
    parsed = json.loads(cleaned_json)  
    phone_number=parsed.get('app_cldp',{}).get('data',{}).get('classified',{}).get('contactSections',{}).get('sticky',{}).get('phoneNumbers',[])
print(size)
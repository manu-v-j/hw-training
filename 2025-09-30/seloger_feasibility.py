import requests
from parsel import Selector
import re,json
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.seloger.com/?tab=buy',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.223738213.1759216665; _ga=GA1.1.634173938.1759216668; ry_ry-s3oa268o_realytics=eyJpZCI6InJ5Xzc0NDExQTU0LUQxMDgtNDNBNS1BOTkyLTIzNEQ2QTk3Rjk5QiIsImNpZCI6bnVsbCwiZXhwIjoxNzkwNzUyNjcxMDAxLCJjcyI6bnVsbH0%3D; _tac=false~self|not-available; _ta=fr~1~1c27cd7cdaf3330364ddfd6a094df6ea; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; kameleoonVisitorCode=jcouexf0brjqmyly; kameleoonVisitorCode=jcouexf0brjqmyly; x-debug-info=human; __gsas=ID=c4674ce7df909032:T=1759217739:RT=1759217739:S=ALNI_MZ_LsR4SuiCeinuyw9ZAZszAIFzQw; _fbp=fb.1.1759217743462.896062880361656861; _lr_env_src_ats=false; _lr_sampling_rate=0; QSI_CT={"pre_user_saved_search_qualtrics_survey":0}; ry_ry-s3oa268o_so_realytics=eyJpZCI6InJ5Xzc0NDExQTU0LUQxMDgtNDNBNS1BOTkyLTIzNEQ2QTk3Rjk5QiIsImNpZCI6bnVsbCwib3JpZ2luIjpmYWxzZSwicmVmIjpudWxsLCJjb250IjpudWxsLCJucyI6ZmFsc2UsInNjIjpudWxsLCJzcCI6bnVsbH0%3D; _tas=fl5pqj48mx8; datadome=ngTcYoTQeu3P98J_RpBHVUbrZhjmRaNO_Aa36MAXleUjqXXhZU79MShgoiZcJZoOeLsrip9i2s~YPM1G6FStp3UEY1WWt15bSwesmBB6jBEWMIq7qhIVyZpQoyxRm9x9; _lr_retry_request=true; __gads=ID=083156c6ab4bb1f4:T=1759217752:RT=1759221414:S=ALNI_MYYwyxGhpDVSCMeAWH-gqjctnI4uw; __gpi=UID=0000119cac4e789d:T=1759217752:RT=1759221414:S=ALNI_MYTszk9Gb2NTWgYjfnHkFK0M4aplg; __eoi=ID=64e4dff4da1d3160:T=1759217752:RT=1759221414:S=AA-AfjYmHhT1xYSdO21cgv0F6GKo; page_viewed_buy=8; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222026-09-30T08%3A39%3A01.901Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22dk0dHglkncScfQMMoKG2%22%2C%22expiryDate%22%3A%222026-09-30T08%3A39%3A01.907Z%22%7D; _ga_MC53H9VE57=GS2.1.s1759220729$o2$g1$t1759221543$j48$l0$h0; cto_bundle=vnkZFV9jMnZuRVdqazlPT0xBZVVvNWRoSVJtdjR6Y1A4dmNrUGZUakFoN0VPRVRkN0lzSnV5amFzT1Z1dnoyZHg0eEdsYXI4ajZKdHVvbGY0ZVpFYSUyQlppSjElMkZGSkF4ZGZEZHpLNG1BZGNzSTkxS0g0N0QlMkZ5d3NpJTJCZ1R2YkJIU3pDVnR0ZzZTdXhadHR4a2gzYm5NNCUyQkZ3MVBsbU5HYlpjUExNMm9PY0RHT0tMVTJXVGVXM1JrRk0wN01POFlxT0FXV3I0N25JU3FudGlVMHpvU0R0bnBvS3hZdDdVelg1VVJvbElGZkMxem0lMkZxWHoyZHluZUFPanlSbW9mTnN0OTdTRDBq; _uetsid=939b3aa09dcd11f09782a326ed52b0cd|11ftny8|2|fzr|0|2099; _uetvid=939c6b009dcd11f087cde5877c6b48d5|h9g6xz|1759221565735|7|1|bat.bing.com/p/insights/c/o; _dd_s=aid=ea2fea3a-c6fb-4f85-820b-2382313eeb6e&logs=0&expire=1759222497422&rum=0; f0_uid=205a8473-44bf-4b46-926b-596802ce6a93.1759221607551; f0_sid=39c85ccd-f173-4a3a-89c5-db535751d472.1759221607553.30',
}
product=[]
page=1
while len(product)<300:
    base_url=f'https://www.seloger.com/classified-search?distributionTypes=Buy&estateTypes=House,Apartment&locations=POCOFR4452&priceMin=200000&projectTypes=Resale&page={page}'
    response = requests.get(base_url,
        headers=headers,
    )
    print(base_url)

    sel=Selector(text=response.text)
    product_urls=sel.xpath("//div[@class='css-79elbk']/a/@href").getall()
    if not product_urls:
        break
    for url in product_urls:
        product.append(url)
        print(url)
        
    page+=1

base_url="https://www.seloger.com/annonces/achat/appartement/lyon-8eme-69/le-grand-trou/243896883.htm"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
property_price=sel.xpath("//span[@class='css-9wpf20']/text()").get()
property_size=sel.xpath("//span[@class='css-1az3ztj']/text()").get()
type=sel.xpath("//span[@class='css-1b9ytm']/text()").get()
city=sel.xpath("//div[@class='css-1ytyjyb']/text()").get()
for script_text in sel.xpath('//script[contains(text(),"__UFRN_LIFECYCLE_SERVERREQUEST__")]/text()').getall():
    match = re.search(r'JSON\.parse\("(.+)"\)', script_text)
    if match:
        raw_json = match.group(1)
        cleaned_json = raw_json.encode("utf-8").decode("unicode_escape")
        parsed = json.loads(cleaned_json)
        phone_number=parsed.get('app_cldp',{}).get('data',{}).get('classified',{}).get('contactSections',{}).get('sticky',{}).get('phoneNumbers',[])

print(type)
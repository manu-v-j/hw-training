import requests
from parsel import Selector
import re

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://navigator-paper.com/en/key-brand-assets/digital-printing',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.1349069871.1758104226; XSRF-TOKEN=eyJpdiI6IjQ1elhrRDl0SEZZaU96Vnc1VzdkQ2c9PSIsInZhbHVlIjoiZWRmSW9uNFk0T0YrYUxkR0pMeEdKSVlMSUVmU2NjUkdvOElqU2VpT0VPMTNrTXdnYU0vaU5xK3U5em4rdTh2ZW9HVm5EbTEyRUdPazZpQTd2ZGpwd3dDODRzOUFVbUk2ZEVobWdwaGpPaEhqNGVyMWcyRnNBd0tycWVQeFBsNFgiLCJtYWMiOiJjYjAxOGFmNzgwYjljNzc1NTlhMjNmODYxZGI3NjMwNzgyZDNiMjE1M2FhYWJkYjFmMDI1NTEwMjE3Y2RmMjhiIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IjFrei9zSTliWm9mK0w1UU9FNUJIWkE9PSIsInZhbHVlIjoiZ25RVXFtRzNiNW9zUzhpU053WUc1REk3WGlMQXRzMEVNLy9Zb0RmM2NJMEdVbmQrQU93YWM5ODk2ZVhVMmE3cGhpNFFwNTFaUHpXa0dwdG11Q1dPUndUbThGODQyc3JLa1ZGN0JsQ3ZxWjJQSnlCYU10enlsV0VsSk04UlhPcEsiLCJtYWMiOiJhYzI5MWQ3MjQzNjBjMTc4MGIyMjVlMzNkMzcxZTAzOGNiOGIzZDgyNWIxZjk3MGUxZDhhZmM2NTEyMjA1NWI0IiwidGFnIjoiIn0%3D; _ga_2X6849QZ4H=GS2.1.s1758166502$o3$g1$t1758167658$j60$l0$h0',
}

# response = requests.get('https://navigator-paper.com/en/range/office', headers=headers)
# sel=Selector(text=response.text)
# product_details = sel.xpath("//div[@class='mx-auto max-w-7xl my-20']/ream-stack-slider/@*[name()=':slides']").getall()
# combined = " ".join(product_details)
# urls = re.findall(r"url:\s*'([^']+)'", combined)
# image_url = re.findall(r"image_2x:\s*'([^']+)'", combined)

base_url="https://navigator-paper.com/en/range/pro/preprint"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
product_name_raw=sel.xpath("//div[contains(@class,'text-navigator-ream')]/text()").get()
em=sel.xpath("//div[contains(@class,'text-navigator-ream')]/em//text()").getall()
product_name = product_name_raw + " " + " ".join(part.strip() for part in em if part.strip())
product_decsription=sel.xpath("//div[@class='flex flex-col space-y-5']/div//text()").getall()
product_decsription=' '.join([pro.strip() for pro in product_decsription if pro.strip()])
breadcrumb=sel.xpath("//div[contains(@class,'flex uppercase')]/div//text()").getall()
images=sel.xpath("//div[@class='pt-2 relative']/img/@src").get()

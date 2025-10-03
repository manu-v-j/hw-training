import requests
from parsel import Selector

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-none-match': '"myra-f252a4"',
    'priority': 'u=0, i',
    'referer': 'https://www.lidl.hu/c/szorolap/s10013623',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'LidlID=3b88fcdd-bd6d-4e6f-b03d-c7e886239ec8; OptanonAlertBoxClosed=2025-10-03T08:39:59.106Z; utm_source=chatgpt.com; ga4_utm_source=chatgpt.com; _gcl_au=1.1.262073137.1759480800; adSessionId=F24F7684-E4F0-4772-A4E3-A19C28637D93; _ga=GA1.1.1091792752.1759480801; FPID=FPID2.2.XshKozpHZzBKWSlXSmxW8a7OL8Gk46sT3V1ZWs%2BPkbw%3D.1759480801; FPLC=hQUufO2cmGvWtmErGhSleZAV1OcgVTqurSuifYG4bNHfRlQJ3mtGBXrT%2BAhtJP9wuf0HyBYFlKXNLRb%2Brpy2wExrQ3qFblABQHVhUEMRPanw9AOwFNRHCTP8yrPqdQ%3D%3D; _fbp=fb.1.1759480810333.361503365711655439; UserVisits=current_visit_date:03.10.2025|last_visit_date:03.10.2025; FPGSID=1.1759480802.1759481044.G-LJEMRH8YP2.vAZ8RoMC-MpKZ4Bi8ntwrA; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+03+2025+14%3A14%3A06+GMT%2B0530+(India+Standard+Time)&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=cdc186ef-df99-46a8-8ec5-2680de1fec63&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1&geolocation=IN%3BKL&AwaitingReconsent=false; _ga_LJEMRH8YP2=GS2.1.s1759480801$o1$g1$t1759481053$j47$l0$h517971697',
}

response = requests.get('https://www.lidl.hu/c/uzleteink/s10013634', headers=headers)
sel=Selector(text=response.text)
stores_list=sel.xpath("//div[@class='ATheLegalText__ContentContainer']/ul/li/text()").getall()
for store in stores_list:
    print(store)
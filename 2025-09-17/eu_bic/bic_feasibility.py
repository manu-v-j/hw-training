import requests
from parsel import Selector
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://eu.bic.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_fbp=fb.1.1758104866847.2484379646288823; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; didomi_token=eyJ1c2VyX2lkIjoiMTk5NTczNzQtN2YwMC02MTcxLWI5MTAtZDQ5MGI4MGQxMDJjIiwiY3JlYXRlZCI6IjIwMjUtMDktMTdUMTA6Mjc6NDQuNzUyWiIsInVwZGF0ZWQiOiIyMDI1LTA5LTE3VDEwOjI3OjQ4LjkxNFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYW1hem9uIiwiYzphYi10YXN0eSIsImM6bGlua2VkaW4iLCJjOnRpa3Rvay1LWkFVUUxaOSIsImM6Z29vZ2xlYW5hLUdNOGNURmhSIiwiYzpyZXF1aXN2LVJ0WHRRQ3liIiwiYzpmb25jdGlvbm5lLU5KQURldFljIiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOm1hcmtldGluZy14WTNLNGhQQiIsImM6c2VsbGlnZW50LWNEazRDVkNEIiwiYzpiYXRjaC1aZ01oUlQ5ZCIsImM6Y29udGVudHNxdWFyZSIsImM6bWljcm9zb2Z0IiwiYzpwaW50ZXJlc3QiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiZ2VvbG9jYXRpb25fZGF0YSIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiLCJhdWRpZW5jZW0taW56UEhHV24iLCJtYXJrZXRpbmctVjRVNm5hWFEiXX0sInZlbmRvcnNfbGkiOnsiZW5hYmxlZCI6WyJnb29nbGUiXX0sInZlcnNpb24iOjIsImFjIjoiQ2d5QUdBRmtBOHdLREFBQS5DZ3lBR0FGa0E4d0tEQUFBIn0=; euconsent-v2=CQX48QAQX48QAAHABBENB8FsAP_gAELAAAAAF5wBwAKgBFAC2AKQBGICvgF5gXnACAAqAvMAAAAA.f_wACFgAAAAA; _gid=GA1.2.707658524.1758104869; _ga_2GNDEY4LYW=GS2.1.s1758104906$o1$g1$t1758105743$j59$l0$h0; _ga=GA1.2.1959582522.1758104866; _ga_K3Y8QXF6KW=GS2.2.s1758104869$o1$g1$t1758106758$j16$l0$h0; _ga_SXD19SQ8CR=GS2.1.s1758104866$o1$g1$t1758106779$j60$l0$h0',
}

response = requests.get('https://eu.bic.com/en-gb/beauty/click-soleil', headers=headers)
sel=Selector(text=response.text)
rows = sel.xpath("//div[@class='push']")
for item in rows:
    product_name = item.xpath(".//div/h2//text()").getall()
    product_description = item.xpath(".//div/ul/li//text()").getall()

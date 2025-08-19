from curl_cffi import requests
from parsel import Selector
import re
cookies = {
    
 'ak_bmsc': 'AE37D7A268F4EF56426336FD35362F6B~000000000000000000000000000000~YAAQHbxWaDsaAaeYAQAA58t0wRxSOKpc2EDf+jF0ETEPaImLlTbaDxrrFcqbK0UAn8//WErWwSej2nLp/O9ql+rkvtP2z6yFavoxBUMtJA7n0noUx/oNF7l/tytZziT+u+3J43PT7MMyv70PgEVS2e1h8V1hr0VJ1NkD5LK6hgYF3imlDF3XqCVpfAigN5+LFSmKw953/dQ9V3VJ/IkIN9y2kB9yWtYc0GstWLERYqxC2qnGSgZinM8cH7ixxTZKuNb8kb4+XSFHA+Lp1X836um39xsJ2fl/2qMtcBfLWCsmiIIJogeo60gOqPHO5yIO7cEyNJeJhSlY1RQ4cHwbqdUMzSOyxLao2sTvo/l3+XdM0LN0SF4nAwrbWaeRaaqIwrCNRVD80EeXG1AZFhXyaK99raES2+OxsGn7KljNmIoz7syIYIagXTBgMQqwISPtD134BJ372wBMJr9BtDv3Uwa1DMNCgHjA8bek2a0QYl6SktcjiKl9TwxYp6BdOCRiGiioKBQyIbfEyUVe+K/VXZuFsQlc24/ubeWdFFdUxtpFn8sZFNjoFdkkLcJxlALmHyt83RRkpOLCc5MVoJ0/NaZN41xa1H8odFfZi0tlUzqRl/BFzMoRoMySBmEe0Jg='
 }
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
}
#########################CATEGORY##############################################
respose=requests.get('https://www.zara.com/ae/',headers=headers,cookies=cookies,impersonate='chrome')
print(respose.status_code)
sel=Selector(text=respose.text)
category_urls=sel.xpath("//li[contains(@class,'layout-categories-category') and contains(@data-layout,'products-category-view')]/a/@href").getall()
print(sel)

#########################CRAWLER###############################################
# product_link=[]
# page=1
# while True:
#     base_url=f"https://www.zara.com/ae/en/man-shirts-l737.html?page={page}"
#     response = requests.get(base_url, cookies=cookies, headers=headers,impersonate='chrome')
#     sel=Selector(text=response.text)
#     product_urls=sel.xpath("//a[contains(@class,'product-grid-product__link link')]/@href").getall()
#     print(len(product_urls))
#     if not product_urls:
#         break
#     print(base_url)
#     for url in product_urls:
#         product_link.append(url)

#     page+=1


########################PARSER###############
# url="https://www.zara.com/ae/en/faded-sweatshirt-p03253345.html"
# response=requests.get(url,headers=headers,cookies=cookies,impersonate='chrome')
# if response.status_code==200:
#     sel=Selector(text=response.text)
#     prices=sel.xpath("//span[@class='money-amount__main']/text()").get()

#     script_text = sel.xpath('//script[@data-compress="true"]/text()').get()
#     match = re.search(r'"productId":(\d+)', script_text)
#     product_id=''
#     if match:
#         product_id = match.group(1)
#     category_match=re.search(r'"section":"([^"]+)"', script_text)
#     department=''
#     if category_match:
#         department = category_match.group(1)
#     sub_department=''
#     product_description=sel.xpath("//div[@class='expandable-text__inner-content']/p/text()").get()
#     color=sel.xpath("//p[contains(@class,'product-color-extended-name ')]/text()").get()
#     product_type=''




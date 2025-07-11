import requests
from parsel import Selector
import logging
logging.basicConfig(level=logging.INFO)

headers={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'priority':'u=0,i',
    'referer':'https://www.homedepot.com/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'Linux',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

###################CATEGORY###############################################
# url='https://www.homedepot.com/b/Appliances/N-5yc1vZbv1w'
# response=requests.get(url,headers=headers)
# sel=Selector(text=response.text)
# category_url=sel.xpath("//li[contains(@class, 'side-navigation__li')]//a/@href").getall()
# print(category_url)

#############################CRAWLER#######################################
count=0
url='https://www.homedepot.com/b/Appliances-Kitchen-Appliance-Packages/N-5yc1vZ2fkpfuj'

response = requests.get(url, headers=headers)
sel = Selector(text=response.text)

product_urls = sel.xpath("//a[@class='sui-top-0 sui-left-0 sui-absolute sui-size-full sui-z-10']/@href").getall()

for product in product_urls:
    full_url = f"https://www.homedepot.com{product}"
    count += 1
    print(count, full_url)
    logging.info(full_url)

next_page = sel.xpath("//a[contains(@class,'sui-lab-btn-base') and @aria-label='Skip to Next Page']/@href").get()
print(next_page)

    
    # if next_page:
    #     url = f"https://www.homedepot.com{next_page}"
    # else:
    #     break
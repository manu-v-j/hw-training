import requests
from parsel import Selector
import json
import re
base_url="https://www.target.com/c/men-s-clothing-deals/-/N-g23gm"
headers={
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding":"gzip, deflate, br, zstd",
    "accept-language":"en-US,en;q=0.9",
    "cache-control":"max-age=0",
    "priority":"u=0,i",
    "sec-ch-ua":'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Linux",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}


##############################CRAWLER##############################

url="https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&category=g23gm&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&include_review_summarization=false&new_search=false&offset=0&page=%2Fn%2Fg23gm&platform=desktop&pricing_store_id=1092&spellcheck=true&store_ids=1092%2C1393%2C2483%2C1447%2C3254&useragent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F129.0.0.0+Safari%2F537.36&visitor_id=01971FF133CC02018723DC2974D00AA4&zip=69556"
response=requests.get(url,headers=headers)
data=response.json()
product_list=data.get("data",{}).get("search",{}).get("products",[])
for item in product_list:
    product_url=item.get("parent",{}).get("item",{}).get("enrichment",{}).get("buy_url","")

##############################PARSER##############################


response=requests.get('https://www.target.com/p/hanes-men-s-premium-5pk-slim-fit-crewneck-t-shirt/-/A-14068766',headers=headers)
sel=Selector(text=response.text)
product_name_xpath="//h1[@data-test='product-title']/text()"
size_xpath="//li[@class='styles_ndsCarouselItem__dnUkr']/a/span/text()"
breadcrumb_xpath="//a[@class='styles_ndsLink__GUaai styles_onLight__QKcK7']/text()"


product_name=sel.xpath(product_name_xpath).get()
size=sel.xpath(size_xpath).getall()
breadcrumb=sel.xpath(breadcrumb_xpath).getall()

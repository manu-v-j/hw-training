import requests
from parsel import Selector
import json

headers={
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding":"gzip, deflate, br, zstd",
    "accept-language":"en-US,en;q=0.9",
    "priority":"u=0, i",
    "referer":"https://www.aldi.nl/producten/brood-bakkerij-bakken/dagvers-brood.html",
    "sec-ch-ua":"\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Linux",
    "sec-fetch-dest":"document",
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"same-origin",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

}

##############################CRAWLER##############################
base_url="https://www.aldi.nl/producten/aardappels-groente-fruit/groenten.html"

url="https://2hu29pf6bh-2.algolianet.com/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.24.0)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.74.0)%3B%20react%20(18.2.0)%3B%20react-instantsearch%20(7.13.0)%3B%20react-instantsearch-core%20(7.13.0)%3B%20next.js%20(14.2.26)%3B%20JS%20Helper%20(3.22.4)&x-algolia-api-key=686cf0c8ddcf740223d420d1115c94c1&x-algolia-application-id=2HU29PF6BH"
payload={
  "requests": [
    {
      "indexName": "an_prd_nl_nl_products",
      "params": "filters=categories:groenten&highlightPostTag=__/ais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=1000&page=0"
    }
  ]
}

response=requests.post(url,headers=headers,json=payload)
if response.status_code==200:
    data=response.json()
    result_list=data.get("results",[])
    for item in result_list:
        hits_list=item.get("hits",[])
        for hit in hits_list:
            name=hit.get("productSlug","")
            id=hit.get("objectID","")
            product_url=f"https://www.aldi.nl/product/{name}-{id}.html"

##############################PARSER##############################
response=requests.get(
    'https://www.aldi.nl/product/verspakket-curry-madras-1230692.html',
    headers=headers
)

sel=Selector(text=response.text)
product_name_xpath="//h1[@class='product-header__variant']//text()"
price_xpath="//span[@class='tag__label tag__label--price']//text()"
breadcrumb_xpath="//li[@class='breadcrumbs__item']//text()"
product_name=sel.xpath(product_name_xpath).get()
price=sel.xpath(price_xpath).get()
breadcrumb=sel.xpath(breadcrumb_xpath).getall()
print(breadcrumb)
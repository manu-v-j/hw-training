import requests
from parsel import Selector
import re
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.petsplace.nl",
    "referer": "https://www.petsplace.nl/",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "x-algolia-api-key": "NzEyNTY1NzU4YTVhNTc3NzM0MGM3YzAyN2UzMjU4OTI1ZWRhYjk1MjQ3MTFjNmZjMjA4M2RmOGQ3NmI5NGE2ZHRhZ0ZpbHRlcnM9",
    "x-algolia-application-id": "C4JTU0L6ZX"
}

##############################CRAWLER##############################
ean_lists=[76344107521,76344107491,76344108115,76344107538,76344118572,76344105398,76344107262,76344108320,
           76344116639,76344106661,64992523206,64992525200,64992523602,64992525118,64992714369,64992714376,
           5425039485256,5425039485010,5425039485263,5425039485034,5425039485317,5407009646591,5407009640353,
           5407009640391,5407009640636,5407009641022,3182551055672,3182551055788,3182551055719,3182551055825,
           9003579008362,3182550704625,3182550706933,9003579013793]
count=0
for ean in ean_lists:
    page=0
    while True:
        payload={
                    "requests": [
                        {
                        "indexName": "PRO_Products_NL_NL",
                        "params": f"facetFilters=[\"active:Yes\"]&facets=[\"active\",\"brand\",\"category0\",\"category1\",\"category2\",\"price\",\"promo_details_special_type\",\"sub_product_group\"]&highlightPostTag=__/ais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=12&maxValuesPerFacet=10&page={page}&query={ean}&ruleContexts=[\"magento_filters\"]&tagFilters="
                        }
                    ]
                    }
        url="https://c4jtu0l6zx-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.3)%3B%20Browser%3B%20instantsearch.js%20(4.63.0)%3B%20Magento2%20integration%20(3.13.4)%3B%20JS%20Helper%20(3.16.1)"
        response=requests.post(url,headers=headers,json=payload)
        data=response.json()
        result_list=data.get("results",[])
        if not result_list or not result_list[0].get("hits"):
            break
        for result in result_list:
            hits_list=result.get("hits",[])
            for hits in hits_list:
                url=hits.get("link","")
                count+=1
                print(url)  
        page+=1

print(count)     

# ##############################PARSER##############################

response=requests.get('https://www.petsplace.nl/wellness-core-grain-free-dog-small-breed-hondenvoer-m-076344107521-pps?flavor_calc=12435')
sel=Selector(text=response.text)

unique_id=sel.xpath("//td[@class='col data' and @data-td='EAN']//text()").get()
product_name=sel.xpath("//span[@class='base']//text()").get()
brand=sel.xpath("//td[@class='col data' and @data-td='Merk']//text()").get()
grammage_quantity=(re.search(r'\d+(?:\.\d+)',product_name)).group()
grammage_unit=(re.search(r'\b(kg|g|ml|l)\b',product_name)).group()
instock=sel.xpath("//span[@class='in-stock-text']//text()").get()
regular_price=sel.xpath("//span[@class='price']//text()").get()
currency=sel.xpath("//span[@class='price-per_unit']//text()").get()
currency=(re.search(r'€', currency)).group()
breadcrumb=sel.xpath("//div[@class='breadcrumbs']//li//span[@itemprop='name']//text()").getall()
description_list=sel.xpath("//div[@class='product attribute description']/div//text()").getall()
description = ' '.join([x.strip() for x in description_list if x.strip()])
material_composition=sel.xpath("//td[@class='col data' and @data-td='Samenstelling']//text()").get()
vitamins=sel.xpath("//td[@class='col data' and @data-td='Analyse']//text()").get()
feeding_recommendation=sel.xpath("//td[@class='col data' and @data-td='Aanbeveling']//text()").get()
reviews=sel.xpath("//span[@class='counter']//text()").get()




# ##############################FINDINGS##############################
# # Success Percentage:83.33%
# # Failure Percentage:16.67%



     
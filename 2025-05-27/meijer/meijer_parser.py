from curl_cffi import requests
from settings import *
import re
payload={
            "c": "ciojs-client-2.64.2",
            "key": "key_GdYuTcnduTUtsZd6",
            "i": "e14167cf-a719-4007-9eb3-eda086d4084f",
            "s": 3,
            "us": "web",
            "page": 1,
            "num_results_per_page": 52,
            "filters": {
                "availableInStores": 20
            },
            "sort_by": "relevance",
            "sort_order": "descending",
            "fmt_options": {
                "groups_max_depth": 3,
                "groups_start": "current"
            },
            "_dt": 1748333663952
            }
response=requests.get(url,headers=headers,json=payload)
data=response.json()
response_list=data.get("response",{}).get("results",[])
for item in response_list:
    unique_id=item.get("data",{}).get("id")
    product_name=item.get("data",{}).get("summary")
    regular_price=item.get("data",{}).get("price")
    selling_price=item.get("data",{}).get("discountSalePriceValue")
    grammage_quantity=re.search(r'\d+(?=\D*$)',).group()
    print(grammage_quantity)
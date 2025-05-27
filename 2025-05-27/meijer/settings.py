
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9", 
    "content-type": "application/json; charset=UTF-8",
    "origin": "https://www.meijer.com",
    "priority": "u=1, i",
    "referer": "https://www.meijer.com/shopping/departments/beer-wine-spirits.html?icid=Header:BeerWineSpirits",
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
base_url="https://www.meijer.com/shopping/departments/beer-wine-spirits.html?icid=Header:BeerWineSpirits"
url="https://ac.cnstrc.com/browse/group_id/L1-918?c=ciojs-client-2.64.2&key=key_GdYuTcnduTUtsZd6&i=e14167cf-a719-4007-9eb3-eda086d4084f&s=3&us=web&page=1&num_results_per_page=52&filters%5BavailableInStores%5D=20&sort_by=relevance&sort_order=descending&fmt_options%5Bgroups_max_depth%5D=3&fmt_options%5Bgroups_start%5D=current&_dt=1748333663952"

MONGO_URI="mongodb://localhost:27017"
DB_NAME="meijer"
COLLECTION="product_link"
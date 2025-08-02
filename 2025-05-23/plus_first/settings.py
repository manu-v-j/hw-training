base_url="https://www.plus.nl/producten/kaas-vleeswaren-tapas/kaas"
headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "269",  
    "content-type": "application/json; charset=UTF-8",
    "origin": "https://www.plus.nl",
    "outsystems-locale": "nl-NL",
    "priority": "u=1, i",
    "referer": "https://www.plus.nl/producten/kaas-vleeswaren-tapas/kaas",
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
    'x-csrftoken': 'T6C+9iB49TLra4jEsMeSckDMNhQ='
}


url = "https://www.plus.nl/screenservices/ECP_Composition_CW/ProductLists/PLP_Content/DataActionGetProductListAndCategoryInfo"
url_pdp="https://www.plus.nl/screenservices/ECP_Product_CW/ProductDetails/PDPContent/DataActionGetProductDetailsAndAgeInfo"

MONGO_URI="mongodb://localhost:27017/"
DB_NAME='plus'
COLLECTION="product_link"
COLLECTION__DETAIL="product_details"

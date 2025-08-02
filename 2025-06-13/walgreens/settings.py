BASE_URL='https://www.walgreens.com/'
headers = {
    "authority": "www.walgreens.com",
    "method": "GET",
    "path": "/store/c/allergy-medicine/ID=361485-tier3",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "v2H=t; wag_sid=etm3kda9whk4c7xzi7gcdqnt; ... (TRUNCATED FOR BREVITY)",
    "priority": "u=0, i",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}


MONGO_URI="mongodb://localhost:27017"
MONGO_DB="walgreens"
COLLECTION="product_link"
COLLEC_DETAIL="product_details"
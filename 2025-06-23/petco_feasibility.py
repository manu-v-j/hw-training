from parsel import Selector
from curl_cffi import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://www.petco.com/shop/en/petcostore/category/dog/dog-food?__cf_chl_tk=6BJAfPoAZtSTfV.cf1xZumNzkNd9wq2EXWFA2CBd__U-1750701272-1.0.1.1-WDu00JmZSxolfVGnQ09T.abvK9PAQFQSqc8x240QEY0",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-arch": "\"\"",
    "sec-ch-ua-bitness": "64",
    "sec-ch-ua-full-version": "129.0.6668.58",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"129.0.6668.58\", \"Not=A?Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"129.0.6668.58\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform-version": "6.0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}



cookies = {
   
    "datadome": "8oYDng_RWtB8zgovQ~e_bmqArH65WnZJI__I2f0qR9lCQjDHd6X4QAAVBdS~gZnsUuzl2EvAv5yDsdZsmDpi6P_~UrdnQqV5tACnGNr6S1LHuOPZSgPaTjAYrtfkgvvP"

}
proxies = {
    "http": "http://51.81.245.3:17981",
    "https": "http://51.81.245.3:17981"
}


# ##############################CRAWLER##############################
url="https://www.petco.com/shop/en/petcostore/category/dog/dog-food"
resp_post = requests.get(url,headers=headers,cookies=cookies,impersonate="chrome101",proxies=proxies)
print(resp_post.status_code)

















# from playwright.sync_api import sync_playwright
# from parsel import Selector
# from urllib.parse import urljoin
# from settings import *
# import logging

# class Crawler:

#     def __init__(self):
#         pass
#     def start(self,url):
#         agent_links = []

#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
#             context = browser.new_context(user_agent=headers)
#             page=context.new_page()
#             try:
#                 page.goto(url, timeout=60000, wait_until="domcontentloaded")
#                 page.wait_for_selector(".site-roster-card-image-link", timeout=20000)

#                 content = page.content()
#                 selector = Selector(text=content)

#                 agent_links = [
#                     urljoin(url, link)
#                     for link in selector.xpath("//a[@class='site-roster-card-image-link']/@href").getall()
#                 ]
#             except Exception as e:
#                 print(f"[Error] {e}")
#             finally:
#                 browser.close()

#         return agent_links


# if __name__ == "__main__":
#     crawler=Crawler()
#     result = crawler.start("https://www.alliebeth.com/roster/Agents/0")
#     print(result)


from curl_cffi import requests
from parsel import Selector

baseurl = "https://www.alliebeth.com/roster/Agents/0"

headers = {
    "authority": "api.rlfrc.net",
    "method": "GET",
    "path": "/property-discovery/public/v1/property-visit/identifier?url=https%3A%2F%2Fwww.alliebeth.com%2Froster%2FAgents%2F0",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "text/plain",
    "origin": "https://www.alliebeth.com",
    "priority": "u=1, i",
    "referer": "https://www.alliebeth.com/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}

cookies = {
    "culture": "en",
    "currencyAbbr": "USD",
    "currencyCulture": "en-US",
    "_gcl_au": "1.1.1635660115.1746679384",
    "_yoid": "6f809a9c-41aa-4d98-a3ae-e57eb7e3c16b",
    "_gid": "GA1.2.1497772833.1747895341",
    "subsiteID": "326373",
    "subsiteDirectory": "",
    "ASP.NET_SessionId": "udn1hcmg50l5xi5oytnte000",
    "rnSessionID": "733781271487009719",
    "_gat_gtag_UA_11234653_1": "1",
    "cf_clearance": "qqZUWvXSxyiD50iaYomJd_fZuMrcA4N1s0RPp6.2l34-1747898564-1.2.1.1-Ug5cGClwu3Kinw4IroQifT.qw8YN9ePAIngHCqA_Xwwtft9cQAZzVJ.ZRSareMFQqijBgpO2_99fPeFp9JG.l52xBQWf9lRtdC00f1i3i3_6elgH1.K8u48BOvptK110NOEd1nxbDXj79ABCd8bVvioqrtAPvK2QbyIBK9kOIcojnTgXL_N8rqA1rD6V4ecdP8LrQsWJOiphqQ9nm7OU_OqauB41OUkdtB44FqqiD2T2ZEQyCWdFWaEyPt8C1TZc7DO_9NbTEyImUjy_3NMtk8uqQb2NMGL4gxiJvNYrCvAWiJY1HLTtjH5bj4B7yguyatRmn6AFMEkF6PEZ5NVHYaUkfWRR62GGD3b115Jecpo",
    "__cf_bm": "6ULfRCWY6tvtUxpgYnLCZXMgE0P3Rul6zLIuymf6nV4-1747898576-1.0.1.1-gZph.2yZJt1vnQ2h2xp54_Xx3Hnh4tE.YCCZNwpoF7d8qFBanD_gigvBVwBMRbFxCKaO4N0muTTrBdY4B4XthMlAKq6KMqRSgf5EWNBzc00",
    "_cfuvid": "SsTgKs0RYoNvPTRsM6pzh6y02D5o2OcICNjhNOfJm1k-1747898576627-0.0.1.1-604800000",
    "_ga_S01P508Z6Z": "GS2.1.s1747895338$o22$g1$t1747898577$j43$l0$h0$d1WLIcAikkmhbN0_XQFKqkJ4ehTgBeTX8ZA",
    "_ga": "GA1.2.925180383.1746679381"
}

response = requests.get(baseurl, headers=headers,cookies=cookies)

print(response.status_code)
print(response.text)



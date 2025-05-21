# from playwright.sync_api import sync_playwright
# from parsel import Selector
# from settings import *
# from urllib.parse import urljoin

# class Crawler:

#     def __init__(self):
#         pass
#     def start(self, url):
#         all_agent_links = []

#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
#             context = browser.new_context(user_agent=Headers["User-Agent"])  
#             page = context.new_page()
#             page_count=0

#             while url and page_count<1:
#                 page.goto(url, timeout=60000)

#                 for _ in range(5):
#                     page.evaluate("window.scrollBy(0, window.innerHeight)")
#                     page.wait_for_timeout(10000)

#                 response = page.content()
#                 agent_links = self.parse_item(response, url)
#                 all_agent_links.extend(agent_links)

               
#                 sel = Selector(text=response)
#                 next_page = sel.xpath("//a[@class='pagination-item' and @aria-label='Next']/@href").get()
#                 url = urljoin(url, next_page) if next_page else None
#                 page_count+=1

#             browser.close()
#         return all_agent_links

#     def parse_item(self, response, url):
#         sel = Selector(text=response)
#         links = sel.xpath("//div[@class='m-agent-item-results__card']/a/@href").getall()
#         return [urljoin(url, link) for link in links]  



# if __name__ == "__main__":
#     crawler = Crawler()
#     result = crawler.start(baseurl)  
#     print(f"\nTotal agent links collected: {len(result)}")
#     for link in result:
#         print(link)

from settings import baseurl, headers  
from curl_cffi import requests
from parsel import Selector

cookies="""AEC=AVcja2drEoqWnph2Vv_vPI3scGvRQSMko52wkG0SdPzfSbU8XgjDHVcVrQ; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20226%7CMCMID%7C64151053155853075771210439835530696177%7CMCAAMLH-1748060094%7C12%7CMCAAMB-1748060094%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1747462494s%7CNONE%7CMCCIDH%7C1764610590%7CvVersion%7C5.1.1; APISID=vkjnvTHN5hIZt5Ou/A5W-N_u9jxXocwJJN; ASP.NET_SessionId=3by45uam2f2jlqcdtuv4hy0a; AnalyticsSyncHistory=AQI01kFC2-_nvAAAAZbkFURAMSO3gTRfydovqtdv9JYvQHlk6xYxscSxk4hznnSENhlTzgAhkEuOl1UgQ7Cn3Q; HSID=A89jOg-l4awZCrv4f; IDE=AHWqTUlAeUhvT7bhsziyqFbS6xRrACzphclSpv8GnMlDsSI1t_RILAya-tm3lisCLjE; LanguagePreference=eng; LastLocationGetter={"data":{"SeoPart":"/int"}}; NID=524=MpaUK-5tNNp2kplx74Ytfw8Gbf8JCEVGLNh3w5PUGxxeb1kSV16e0pLkZ4PyltajyI280QxUpRFZ_S0lm_Kb00PrX-5P7DNC5Htj77Eqjrap5lB3tnWiKF8C4HYe9PBMx-faKfCUh3cMWecbrwavFcrI7o_qhNvyiEQySGcKSFAZfTAFy8ctDDrGqOXanWiVsyeo9O52tVtidhsI88aNu9ve5l__HsG_CUBfwirQLLDEp7lxucUCAcULaKZIO-_Lpfg8AMRHBzqrVBMJ_CZf3FUm-B9XfWBMb9PFv9l4jh5L3_r9v5Suy9Hq19CriQwiKqDjEfenVtBXnLQepLZgweMqXG1WPkt2hRFAG3K63IXujmzOELAOd7iLxKnjHgUtc5bkgUIbkFa1SP1zHoelviJzUbgjXUcs-C6_n7Tzgv-zUz17WMqfQS_5HhgD_H8aqynIuUMWDUbzyNnR9ZRNIDNlToibUGJBV49mSDt3I2X4WzqyJzQVA15j6xnG7H_nfvD_4q2m7uoWE0H0ze6SEM6NRfPKoeGsxFblPD88nbMWsUHFq_hDpYSWo8IFbIErdrCGreBo-fPN6ZC2fz-oKUFezY0tmqgA3SsEdIl3XwBImNY7XmAU4-X1SQHUVzpd4VpmAzKWZzCnBy7-0f5RIXd5oBlb7QnfkMolAh2082J4XhGtzyrNYXw; SAPISID=npB9KzfDbggDAzQh/ASWli2qAGVxNwjms9; SEARCH_SAMESITE=CgQIhJ4B; SID=g.a000xAhTwgRqwC7j-0sO4mS6Wi5UqQ8VwdQtwh4QqZPWMzCdiCaYK0xdI5ZJ_jN89QuSgVO97QACgYKAeoSARUSFQHGX2Mi_GIkYulzX2B-YIBPty7QjRoVAUF8yKrXtUWDSXbgVumpdZ3SMl5l0076; SIDCC=AKEyXzUt5hOTo4q4K50Dzi2ToNLtcrzUYTA6K_sozoC_BsWKVOBMHj_xYSkWt2x4hqdRRPEcGg; SSID=A7QKnRfbDvrRbBHjn; TAsessionID=37632def-7aae-44f4-92da-f4253fb0ff0b|NEW; TDCPM=CAESFgoHc3Z4OXQ1MBILCNSt9tq2-P09EAUSFwoIcHVibWF0aWMSCwi6_M3q5sKDPhAFEhQKBXRhcGFkEgsI_qaj3Muyiz4QBRIWCgdydWJpY29uEgsI7t68xabrgz4QBRIVCgZnb29nbGUSCwi4nZ-Ct4eMPhAFEhcKCGFwcG5leHVzEgsItJnluciFhz4QBRIXCghsaXZlcmFtcBILCMqop4T5t_49EAUSGwoMc2hhcmV0aHJvdWdoEgsIopPn3r3ogz4QBRIYCgliaWRzd2l0Y2g
"""
response = requests.get(baseurl,headers=headers,impersonate="chrome110")

if response.status_code == 200:
    selector = Selector(response.text)
    print(selector)
else:
    print(f"Request failed with status code {response.status_code}")

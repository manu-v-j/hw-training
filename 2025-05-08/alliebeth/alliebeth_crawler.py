from urllib.parse import urljoin
from parsel import Selector
import requests
from settings import headers

from alliebeth_parser import parser 
class Alliebeth:

    def crawler(self):
         all_data = []

         with open("/home/user/Hashwave/2025-05-08/alliebeth/agent.html", 'r', encoding='utf-8') as file:
             html_content = file.read()

         selector = Selector(text=html_content)
         agents_links = selector.xpath("//a[contains(@class, 'site-roster-card-image-link')]/@href").getall()

         for agent in agents_links:
             if agent:
                 agent_url = urljoin('https://www.alliebeth.com', agent)
                 data = parser(agent_url)
                 if data:
                     all_data.append(data)

         return all_data


obj = Alliebeth()
data = obj.crawler()
print(data)


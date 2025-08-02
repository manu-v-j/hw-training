

# import requests
# import xml.etree.ElementTree as ET

# url = "https://noragardner.com/sitemap_products_1.xml?from=6771738565&to=7391189172318"
# response = requests.get(url)

# if response.status_code == 200:
#     xml_content = response.content

#     root = ET.fromstring(xml_content)
#     namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

#     urls = []
#     for url in root.findall('ns:url', namespaces=namespace):
#         loc = url.find('ns:loc', namespaces=namespace)
#         if loc is not None:
#             urls.append(loc.text)

#     print(len(urls))
   
# else:
#     print(f"Failed to retrieve sitemap: {response.status_code}")


import requests
from xml.dom.minidom import parseString
import logging
logging.basicConfig(level=logging.INFO)

response = requests.get("https://noragardner.com/sitemap_products_1.xml?from=6771738565&to=7391189172318")
dom = parseString(response.content)
for loc in dom.getElementsByTagName("loc"):
    url = loc.firstChild.data
    logging.info(url)
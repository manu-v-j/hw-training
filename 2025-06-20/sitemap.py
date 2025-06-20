import requests
import xml.etree.ElementTree as ET

url = "https://www.walgreens.com/sitemap-pdp.xml"
response = requests.get(url)

if response.status_code == 200:
    xml_content = response.content

    root = ET.fromstring(xml_content)
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    urls = []
    for url in root.findall('ns:url', namespaces=namespace):
        loc = url.find('ns:loc', namespaces=namespace)
        if loc is not None:
            urls.append(loc.text)

    # for link in urls:
    #     print(link)
else:
    print(f"Failed to retrieve sitemap: {response.status_code}")


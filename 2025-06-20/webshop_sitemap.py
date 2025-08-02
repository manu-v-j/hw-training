import requests
import gzip
import io
import xml.etree.ElementTree as ET

url = "https://www.webshop.fressnapf.hu/sitemap-webshop_fressnapf_hu-1.xml.gz"
response = requests.get(url)

urls=[]
if response.status_code == 200:
    with gzip.GzipFile(fileobj=io.BytesIO(response.content)) as gz:
        xml_content = gz.read().decode('utf-8')
        root = ET.fromstring(xml_content)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        for url in root.findall('ns:url', namespaces=namespace):
            loc = url.find('ns:loc', namespaces=namespace)
            lastmod=url.find('ns:lastmod',namespaces=namespace)
            if lastmod is not None:
                urls.append(loc.text)

else:
    print("Failed :", response.status_code)


import requests
from bs4 import BeautifulSoup

class FlipkartParser:
    def __init__(self):
        self.url = "https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp,cil,1cu&otracker=categorytree"

    def start(self):
        try:
            response = requests.get(self.url)
            products = self.parse_item(response.text)  

            with open("flipkart_products.txt", "w") as f:
                for product in products:
                    f.write(f"Brand: {product['brand']}\n")
                    f.write(f"Price: {product['price']}\n")
                    f.write(f"Image URL: {product['image_url']}\n")
                    f.write(f"Product URL: {product['product_url']}\n")
                   


        except requests.RequestException as e:
            print(f"Failed to fetch data: {e}")

    def parse_item(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        brands = soup.find_all("div", class_="syl9yP")
        prices = soup.find_all("div", class_="Nx9bqj")
        images = soup.find_all('img', class_='_53J4C-')
        links = soup.find_all('a', class_='rPDeLR')

        brand_texts = [b.get_text(strip=True) for b in brands]
        price_texts = [p.get_text(strip=True) for p in prices]
        img_urls = [img['src'] for img in images if img.has_attr('src')]
        product_urls = ["https://www.flipkart.com" + a['href'] for a in links if a.has_attr('href')]

        products = []
        for i in range(min(len(brand_texts), len(price_texts), len(img_urls), len(product_urls))):
            product = {
                "brand": brand_texts[i],
                "price": price_texts[i],
                "image_url": img_urls[i],
                "product_url": product_urls[i]
            }
            products.append(product)

        return products



scraper = FlipkartParser()
scraper.start()

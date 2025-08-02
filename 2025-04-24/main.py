import requests
from bs4 import BeautifulSoup
from settings import target_url,DataMiningError

class FlipkartParser:
    def __init__(self):
        self.url = target_url

    def fetch_html(self):
        try:
            response=requests.get(self.url)
            response.raise_for_status()
            products = self.parse_item(response.text)  
            with open("flipkart_products.txt", "w") as f:
                for product in products:
                    f.write(f"Brand: {product['brand']}\n")
                    f.write(f"Price: {product['price']}\n")
                    f.write(f"Image URL: {product['image_url']}\n")
                    f.write(f"Product URL: {product['product_url']}\n")
            return response.text
        
        except requests.exceptions.ConnectionError:
            print("Connection error")
        except requests.exceptions.Timeout:
            print("Request timeout")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error{e}")


    def start(self):
        try:
            html_content=self.fetch_html()
            with open("raw.html","w") as raw_file:
                raw_file.write(html_content)

            soup=BeautifulSoup(html_content,"html.parser")
            cleaned_text = soup.get_text(separator="\n", strip=True)

            if not cleaned_text:
                raise DataMiningError("Parsed content is empty or invalid")

            with open("cleaned_data.txt","w") as clean_file:
                clean_file.write(cleaned_text)

        except DataMiningError as e:
            print(f"parsing error:{e}")
        except Exception as e:
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
        
def yield_lines_from_file(filename):
    try:
          with open(filename,'r') as file:
            for line in file:   
                yield line

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")


scraper = FlipkartParser()
scraper.start()
for line in yield_lines_from_file("cleaned_data.txt"):
    print(line.strip()) 
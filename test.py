import requests

cookies = {
   
    'RT': '"z=1&dm=oreillyauto.com&si=672a8zlfrta&ss=me82ukad&sl=0&tt=0"',
    '_fbp': 'fb.1.1754976656469.639953134206318731',
    '__pdst': '84bdaa4afb084141aedbbfeda7f755a3',
    'selectedStoreId': '3105',
    'lat': '64.83745',
    'lng': '-147.805121',
    'dtCookie': 'v_4_srv_13_sn_2MFHQ2T695SJPG4BJ46ELL030AP8HIAM_perc_100000_ol_0_mul_1_app-3A200c4c21b0fea6c6_1',
    '_abck': 'C1D7B82CACB73EA73E008C386CECA92B~-1~YAAQbzkgFyYfb1aYAQAA/J3CnA43kBYQnp+PM3/x99mvv7jQQL2JJJR97Jzp2pvQxgvnxXhGLj1RPn/F64D3GECaMR33lqm7Voe47rjJDkalATRScMmwbfNHfbg0DJXycf6/c0B14d/yvvqmAOByqMfACWU+LTF6lAWbcNYu2/EXS6Zpv88l9fGSqHi8zlFwIrSM90FXTU+ef5T36GeDL9ZJXuC5jlN7nezA1PYAZH3QhW/iG8Np40t1kVH5sqcLv5LcBW7HcCP8z14fwvMm1pGTzoP59SsQAMGnDt+eo2g03XOL1z/qyrow7WVruIb4fKT+XbTd63CM4tTkyHENq25NhQI0YrcOTqqRZtjcQW9m1/gjlQ6aoVQiob7Gd3TKTce4vQbfdDa/Sg3+sMMqCXs7StM4mi0O7O8rVTGEWmGGpTA+bP58cNPoUGtkT59d~-1~-1~-1',
    'bm_sv': '4C96BB013BB06E10D18A7D936FDFF423~YAAQbzkgFycfb1aYAQAA/J3CnByxOAAN8duORSTzfsW3G/PrWAz9BWu5yzJvgJSu4HLnuKvIMs7F1UA/Tlxu9harqySOINEei4UiAg1EUcT51yfxYtMDCcCUG3ozPQbTK5fZkPrJLqTAARe74p5glQBJEw10D3+l1vioVqpJ0N3XqTvm8MetYAw3KoIE2rD2nJyb6N2JgTkfACJKUYbKmffLqnMwxIFqAXKARaJm6GQslP/jrQjjfzcthOdJMr2T+WgxloOF~1',
    'forterToken': '67e1d7efc67e40f080aae2d101911cf3_1754976654103__UDF43_23ck_',
    'ak_bmsc': '0AC450582608B7AF454F4F6937B20198~000000000000000000000000000000~YAAQbzkgF0gfb1aYAQAAo5/CnBxGx1AHyhZzNssKyMKesDkzXgzff7Y55v5V6Mjyu+TBsbucnxb5hoskOqRV4vXKB2w+7weGf0n50xrQUxt1cDGarh77uBuZsG26rYTfwuw4gjx5ub9YnP39cnMmsOmXv6U+xcELn8pu6qn2jG61HdRvqG5ujxBxodseL1NkF/eQbFf/jW3gZE0DagBTO0q14qw2PorpPnItaq9V7+Y+vj66knyndQG96mIaswLr3yXXHldgbpT4mLkVCnD7GAqfkxe+BkT3STmIc5zd7w65BjLWc4lZcsXmaPIyz+GgBZQY1BudUaipoTwRElahPPRZnQnebRRzwiIqmUAi7Egqf02tUnFBxp4uXOdwzwG9ixIJ0P8/l4uAttbDYCt49L3Ab1EkHS0TLEbDthj+iyqf9uhXHb0SOJMI8PkeNyQq09HBtXfQiP9NFXSrKYgkcatDJobg8QJDS3RVpUN33WH5oQTxp+QJ4qdOGhLBTJ30+IVJ6N7KYCKPYS3CsZIQ880cC+WKmv7GcfauDQm9gHPwX7pWd4Vvb1DEdV2zjNsXgaJ/WJ2OmYZKrxdKX20X19Hck41+Ed6kYDRb4iRHa1MPVPuMg3O+',
    'rxvt': '1754978457403|1754975079329',
    'dtPC': '13$576652278_628h11vFCSJKQGUECECREHEOKUKOMVAKBONPONG-0e0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.oreillyauto.com',
    'priority': 'u=1, i',
    'referer': 'https://www.oreillyauto.com/detail/c/3m/tools---equipment/tapes/foam-mounting-tape/c9b4729e478c/3m-attachment-tape/mmm0/06378',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-csrf-token': '2Q6H-IP7Y-D20M-Y567-6NFH-E59Q-PGH3-V8PK',
    'x-dtpc': '13$576652278_628h11vFCSJKQGUECECREHEOKUKOMVAKBONPONG-0e0',
    # 'cookie': 'dtSa=-; uws_session=%7B%22start%22%3A1754975089980%2C%22count%22%3A3%2C%22referrer%22%3A%22%22%7D%7Csession_timeout; uws_visitor=%7B%22vid%22%3A%22175497508998127406%22%2C%22start%22%3A1754975089980%2C%22count%22%3A3%7D%7C1762751437968; JSESSIONID=DB8E3AB4BA5E5B0362DF0C371BF121FC-n1; ga_session=8b46d97a-56d3-44a7-95ca-6d6f33e3dcb6; ActiveID=PED6-8JFM-MS8D-P74G-DH8Q-PJQ4-OLGJ-QPF2; cust_id="Wf1+Rb3r0rEvGsBXKjrEgMnXuTfXEHKk+5MQzkt2y0k="; OSESSIONID="17d6b0d6a5bf1a94"; akacd_ost-prod-lb-2=1755019850~rv=69~id=0f932f7f8f4351a2a3b4ba5a5a5bbdea; uws_prop_8jo1u2t0=%228b46d97a-56d3-44a7-95ca-6d6f33e3dcb6%22%7Csession_timeout; EPCRVP="MMM-6378,c9b4729e478c"; AKA_A2=A; bm_mi=70428E38028C572A120AFD4B993D90BB~YAAQbzkgF0Qeb1aYAQAATorCnByY1VjisnQVoY0OYS2eit7bKyLP73Tao2YgpTeEVXnwmAaZaChkai2P2ACsALBpr6sOX9y24/mC+Ff9rIZGc7yDK2qf8Y6eloMCaYcy1KNVvlZoD9LfTeI2kBQQSF1rDST3bmjif0PoS3tfm/Uut8lZ7R5z/488wQVqHBhCwaEWhybqVX2wX6+TdjvapENynD3H3VTfgwowrIikKMWbayjWWbJKI5Fi6uhMzZbvs2cjcrH+7Hlituy3Q4Q5vfar5Mw9Do8EPhpMEp/Z49Skc8Kye0coODuBSQ8x87rHitf5EvApRNqUR6rxyFjCfaDAPV6N1EMtU0yJslMbCsoOAFCwLuRG1a+RB0EBMKB7U1J/mP2qD8kSZHgZ6UTnc5WDChDFVlFrm34VLGTJ3sBw7H/Z5ie8Ql77Rxai/kXEebrMCw==~1; bm_sz=3420C72F8D52337BE998873B008843E5~YAAQbzkgF0Yeb1aYAQAATorCnBwfg1ZZ6rCSv2Iu6R6wrsurmgoBsqdf+itHDeJ9OGkFfBF8cfls7/3E021Ysjou/C1mHeXwP/TsCl3dutSYVJUtks3/znU834PXvehWzluCR2WCSdqUMLG5muqTsxddTFv+yEMtFDy/OVLDO582L/nSXrLaR6sC42h9e9Vh19VMOou1HBYFnX3cy8a3OvikYVJKypD0QHsoCLREAa1HqfM7zD7bfZXzRbqtm5fIV46/qjGs2qWBorIsUUNRFIIEPv+VjVea/DAnoOWjcRmrrnUdI28ePco0Q7uJ5aioklbZJHKO8n1gjAjngGiKXZqZiTjk1gmae9ZgDPzBXvHE6pcO8xtxYkHmR7o9T8uZXlPhVYyQsS6FVFdro9xMyrQhoMu1jE20wD8HmlhtGa/XQqft6TM+tIn7N14=~4408385~3683393; rxVisitor=1754976651930USG9BST6T4C2DE0SCAQ2OETMLN1VL4JO; _ga_TV3LS85R98=GS2.1.s1754975081$o1$g1$t1754976651$j60$l0$h0; mt.v=2.1862213886.1754976652357; RT="z=1&dm=oreillyauto.com&si=672a8zlfrta&ss=me82ukad&sl=0&tt=0"; _fbp=fb.1.1754976656469.639953134206318731; __pdst=84bdaa4afb084141aedbbfeda7f755a3; selectedStoreId=3105; lat=64.83745; lng=-147.805121; dtCookie=v_4_srv_13_sn_2MFHQ2T695SJPG4BJ46ELL030AP8HIAM_perc_100000_ol_0_mul_1_app-3A200c4c21b0fea6c6_1; _abck=C1D7B82CACB73EA73E008C386CECA92B~-1~YAAQbzkgFyYfb1aYAQAA/J3CnA43kBYQnp+PM3/x99mvv7jQQL2JJJR97Jzp2pvQxgvnxXhGLj1RPn/F64D3GECaMR33lqm7Voe47rjJDkalATRScMmwbfNHfbg0DJXycf6/c0B14d/yvvqmAOByqMfACWU+LTF6lAWbcNYu2/EXS6Zpv88l9fGSqHi8zlFwIrSM90FXTU+ef5T36GeDL9ZJXuC5jlN7nezA1PYAZH3QhW/iG8Np40t1kVH5sqcLv5LcBW7HcCP8z14fwvMm1pGTzoP59SsQAMGnDt+eo2g03XOL1z/qyrow7WVruIb4fKT+XbTd63CM4tTkyHENq25NhQI0YrcOTqqRZtjcQW9m1/gjlQ6aoVQiob7Gd3TKTce4vQbfdDa/Sg3+sMMqCXs7StM4mi0O7O8rVTGEWmGGpTA+bP58cNPoUGtkT59d~-1~-1~-1; bm_sv=4C96BB013BB06E10D18A7D936FDFF423~YAAQbzkgFycfb1aYAQAA/J3CnByxOAAN8duORSTzfsW3G/PrWAz9BWu5yzJvgJSu4HLnuKvIMs7F1UA/Tlxu9harqySOINEei4UiAg1EUcT51yfxYtMDCcCUG3ozPQbTK5fZkPrJLqTAARe74p5glQBJEw10D3+l1vioVqpJ0N3XqTvm8MetYAw3KoIE2rD2nJyb6N2JgTkfACJKUYbKmffLqnMwxIFqAXKARaJm6GQslP/jrQjjfzcthOdJMr2T+WgxloOF~1; forterToken=67e1d7efc67e40f080aae2d101911cf3_1754976654103__UDF43_23ck_; ak_bmsc=0AC450582608B7AF454F4F6937B20198~000000000000000000000000000000~YAAQbzkgF0gfb1aYAQAAo5/CnBxGx1AHyhZzNssKyMKesDkzXgzff7Y55v5V6Mjyu+TBsbucnxb5hoskOqRV4vXKB2w+7weGf0n50xrQUxt1cDGarh77uBuZsG26rYTfwuw4gjx5ub9YnP39cnMmsOmXv6U+xcELn8pu6qn2jG61HdRvqG5ujxBxodseL1NkF/eQbFf/jW3gZE0DagBTO0q14qw2PorpPnItaq9V7+Y+vj66knyndQG96mIaswLr3yXXHldgbpT4mLkVCnD7GAqfkxe+BkT3STmIc5zd7w65BjLWc4lZcsXmaPIyz+GgBZQY1BudUaipoTwRElahPPRZnQnebRRzwiIqmUAi7Egqf02tUnFBxp4uXOdwzwG9ixIJ0P8/l4uAttbDYCt49L3Ab1EkHS0TLEbDthj+iyqf9uhXHb0SOJMI8PkeNyQq09HBtXfQiP9NFXSrKYgkcatDJobg8QJDS3RVpUN33WH5oQTxp+QJ4qdOGhLBTJ30+IVJ6N7KYCKPYS3CsZIQ880cC+WKmv7GcfauDQm9gHPwX7pWd4Vvb1DEdV2zjNsXgaJ/WJ2OmYZKrxdKX20X19Hck41+Ed6kYDRb4iRHa1MPVPuMg3O+; rxvt=1754978457403|1754975079329; dtPC=13$576652278_628h11vFCSJKQGUECECREHEOKUKOMVAKBONPONG-0e0',
}

json_data = {
    'pricingLineCodeItemNumbers': [
        {
            'itemNumber': 'DS71',
            'lineCode': 'SCP',
        },
    ],
    'availabilityLineCodeItemNumbers': [
        {
            'itemNumber': 'DS71',
            'lineCode': 'SCP',
        },
    ],
}

response = requests.post(
    'https://www.oreillyauto.com/product/pricing-availability/v2',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pricingLineCodeItemNumbers":[{"itemNumber":"6378","lineCode":"MMM"}],"availabilityLineCodeItemNumbers":[{"itemNumber":"6378","lineCode":"MMM"}]}'
#response = requests.post(
#    'https://www.oreillyauto.com/product/pricing-availability/v2',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

from settings import headers, MONGO_URL, MONGO_DB, CATAEGORY_COLLECTION, COLLECTION
import requests
from parsel import Selector
from pymongo import MongoClient,errors
import re, json, json5, logging
import logging
logging.basicConfig(level=logging.INFO)

class Crawler:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[COLLECTION]
        self.collection.create_index('link',unique=True)

    def extract_child_categories(self, sel):
        script_text = sel.xpath("//script[contains(text(), 'window._ost.childCategories')]/text()").get()
        if script_text:
            match = re.search(r"window\._ost\.childCategories\s*=\s*(\[.*?\]);", script_text, re.S)
            if match:
                data_str = match.group(1)
                try:
                    return json.loads(data_str)
                except json.JSONDecodeError:
                    return json5.loads(data_str)
        return []
    
    def start(self):
        for cat in self.db[CATAEGORY_COLLECTION].find():
            url = cat.get('link')
            response = requests.get(url, headers=headers)
            sel = Selector(text=response.text)

            categories = self.extract_child_categories(sel)
            category_list = [c.get('url', '') for c in categories]

            for sub_url in category_list:
                full_url = f'https://www.oreillyauto.com{sub_url}'
                print(f" Subcategory: {full_url}")

                resp = requests.get(full_url, headers=headers)
                sel = Selector(text=resp.text)

                page_num = 1
                while True:
                    product_links = sel.xpath("//a[contains(@class,'product__link')]/@href").getall()
                    if product_links:
                        product_links = [f"https://www.oreillyauto.com{link}" for link in product_links]
                        for url in product_links:
                            print(url)
                            # try:
                            #     self.collection.insert_one({'link':url})

                            # except errors.DuplicateKeyError:
                            #     logging.info(f"Duplicate: {url}")

                    else:
                        sub_categories = self.extract_child_categories(sel)
                        if sub_categories:
                            print(f"Found deeper subcategories: {sub_categories}")
                        break

                    next_page = sel.xpath("//a[contains(@class,'pagination__next')]/@href").get()
                    if not next_page:
                        break

                    next_url = f"https://www.oreillyauto.com{next_page}"
                    resp = requests.get(next_url, headers=headers)
                    sel = Selector(text=resp.text)
                    page_num += 1



if __name__ == '__main__':
    subcategory = Crawler()
    subcategory.start()

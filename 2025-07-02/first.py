import requests
from parsel import Selector
from PIL import Image
from io import BytesIO
import pytesseract
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "host": "freesearchigrservice.maharashtra.gov.in",
    "origin": "https://freesearchigrservice.maharashtra.gov.in",
    "referer": "https://freesearchigrservice.maharashtra.gov.in/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
  
}


year = "2025"
district = "30"  
village_input = "d" 
property_no = "9"

url = "https://freesearchigrservice.maharashtra.gov.in/"

res = session.get(url, headers=headers, verify=False)
sel = Selector(text=res.text)

viewstate = sel.xpath('//input[@name="__VIEWSTATE"]/@value').get()
eventvalidation = sel.xpath('//input[@name="__EVENTVALIDATION"]/@value').get()
viewstategen = sel.xpath('//input[@name="__VIEWSTATEGENERATOR"]/@value').get()

captcha_rel_url = sel.xpath('//img[@id="imgCaptcha"]/@src').get()
captcha_url = f"https://freesearchigrservice.maharashtra.gov.in/{captcha_rel_url}"
captcha_img = session.get(captcha_url, headers=headers, verify=False)
img = Image.open(BytesIO(captcha_img.content))
captcha_text = pytesseract.image_to_string(img).strip()
print("CAPTCHA:", captcha_text)

payload_area = {
    '__EVENTTARGET': 'txtAreaName',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategen,
    '__EVENTVALIDATION': eventvalidation,
    'ddlFromYear': year,
    'ddlDistrict': district,
    'txtAreaName': village_input,
    'txtImg': captcha_text,
    'txtAttributeValue': '',
    'ddlareaname': '-----Select Area----',
}
res_village = session.post(url, headers=headers, data=payload_area, verify=False)
sel = Selector(text=res_village.text)
viewstate = sel.xpath('//input[@name="__VIEWSTATE"]/@value').get()
print(viewstate)

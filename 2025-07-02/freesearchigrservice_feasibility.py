import requests
from parsel import Selector
from PIL import Image
from io import BytesIO
import pytesseract
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://freesearchigrservice.maharashtra.gov.in/",
    "Content-Type": "application/x-www-form-urlencoded"
}
url = "https://freesearchigrservice.maharashtra.gov.in/"
year = "2025"
district = "30"
village_input = "p"
property_no = "11"

session = requests.Session()
response = session.get(url, headers=HEADERS, verify=False)
sel = Selector(text=response.text)

def extract_tokens(sel):
    return {
        "__VIEWSTATE": sel.xpath('//input[@name="__VIEWSTATE"]/@value').get(),
        "__VIEWSTATEGENERATOR": sel.xpath('//input[@name="__VIEWSTATEGENERATOR"]/@value').get(),
        "__EVENTVALIDATION": sel.xpath('//input[@name="__EVENTVALIDATION"]/@value').get()
    }

tokens = extract_tokens(sel)

payload_area = {
    '__EVENTTARGET': 'txtAreaName',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    **tokens,
    'ddlFromYear': year,
    'ddlDistrict': district,
    'txtAreaName': village_input,
    'txtAttributeValue': '',
    'ddlareaname': '-----Select Area----',
    'txtImg': ''
}

res_area = session.post(url, headers=HEADERS, data=payload_area, verify=False)
sel_area = Selector(text=res_area.text)
tokens = extract_tokens(sel_area)

village_options = sel_area.xpath('//select[@id="ddlareaname"]/option/text()').getall()
valid_areas = [v.strip() for v in village_options if v.strip() and "Select" not in v and v.lower().startswith(village_input.lower())]


selected_area = valid_areas[0]

payload_area_select = {
    '__EVENTTARGET': 'ddlareaname',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    **tokens,
    'ddlFromYear': year,
    'ddlDistrict': district,
    'txtAreaName': village_input,
    'ddlareaname': selected_area,
    'txtImg': ''
}

res_area_select = session.post(url, headers=HEADERS, data=payload_area_select, verify=False)
sel = Selector(text=res_area_select.text)
tokens = extract_tokens(sel)

captcha_url = sel_area.xpath('//img[@id="imgCaptcha"]/@src').get()
captcha_url = f"{url}{captcha_url}"
captcha_img = session.get(captcha_url, headers=HEADERS, verify=False)
img = Image.open(BytesIO(captcha_img.content))
captcha_text = pytesseract.image_to_string(img).strip()


HEADERS.update({
    "X-MicrosoftAjax": "Delta=true",
    "X-Requested-With": "XMLHttpRequest"
})

payload_search = {
    "ScriptManager1": "UpMain|btnSearch",
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    **tokens,
    "__ASYNCPOST": "true",
    "ddlFromYear": year,
    "ddlDistrict": district,
    "txtAreaName": village_input,
    "ddlareaname": selected_area,
    "txtAttributeValue": property_no,
    "txtImg": captcha_text,
    "FS_PropertyNumber": "",
    "FS_IGR_FLAG": "",
    "btnSearch": "शोध / Search"
}

response = session.post(url, headers=HEADERS, data=payload_search, verify=False)

HEADERS.pop("X-MicrosoftAjax", None)
HEADERS.pop("X-Requested-With", None)

payload= {
    "ScriptManager1": "upRegistrationGrid|RegistrationGrid",
    "__EVENTTARGET": "RegistrationGrid",
    "__EVENTARGUMENT": "indexII$0",
    "__LASTFOCUS": "",
    **tokens,
    "__ASYNCPOST": "true",
    "ddlFromYear": year,
    "ddlDistrict": district,
    "txtAreaName": village_input,
    "ddlareaname": selected_area,
    "txtAttributeValue": property_no,
    "txtImg": captcha_text,
    "FS_PropertyNumber": "",
    "FS_IGR_FLAG": ""
    }



response_index = session.post(url, headers=HEADERS, data=payload, verify=False)

with open("indexII_result.html", "w", encoding="utf-8") as f:
    f.write(response_index.text)


import requests
from parsel import Selector
from PIL import Image
from io import BytesIO
import pytesseract
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
}

year = "2023"
district = "30"
village_input = "b"
property_no = "1"

url = "https://freesearchigrservice.maharashtra.gov.in/"

# Step 1: Load the main page
res = session.get(url, headers=HEADERS, verify=False)
sel = Selector(text=res.text)

def extract_hidden_fields(selector):
    return {
        '__VIEWSTATE': selector.xpath('//input[@name="__VIEWSTATE"]/@value').get(),
        '__VIEWSTATEGENERATOR': selector.xpath('//input[@name="__VIEWSTATEGENERATOR"]/@value').get(),
        '__EVENTVALIDATION': selector.xpath('//input[@name="__EVENTVALIDATION"]/@value').get(),
    }

hidden_fields = extract_hidden_fields(sel)

# Step 2: Solve CAPTCHA
captcha_rel_url = sel.xpath('//img[@id="imgCaptcha"]/@src').get()
captcha_url = f"https://freesearchigrservice.maharashtra.gov.in/{captcha_rel_url}"
captcha_img = session.get(captcha_url, headers=HEADERS, verify=False)
img = Image.open(BytesIO(captcha_img.content))
captcha_text = pytesseract.image_to_string(img).strip().replace(" ", "").replace("\n", "")
print("CAPTCHA:", captcha_text)

# Step 3: Submit village name to populate area dropdown
payload1 = {
    '__EVENTTARGET': 'txtAreaName',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    'ddlFromYear': year,
    'ddlDistrict': district,
    'txtAreaName': village_input,
    'txtImg': captcha_text,
    'txtAttributeValue': '',
    'ddlareaname': '-----Select Area----',
    **hidden_fields
}

res_village = session.post(url, headers=HEADERS, data=payload1, verify=False)
sel_village = Selector(text=res_village.text)
hidden_fields = extract_hidden_fields(sel_village)

# Step 4: Get actual village dropdown values
area_options = sel_village.xpath('//select[@id="ddlareaname"]/option[not(contains(text(), "Select"))]')
if area_options:
    selected_area = area_options[0].xpath('./@value').get()
    print(area_options)
    # print(f"Selected Area: {selected_area}")
else:
    print("No area found")
    selected_area = ''

# # Step 5: Final search request
# payload2 = {
#     '__EVENTTARGET': 'btnSearch',
#     '__EVENTARGUMENT': '',
#     '__LASTFOCUS': '',
#     'ddlFromYear': year,
#     'ddlDistrict': district,
#     'txtAreaName': village_input,
#     'ddlareaname': selected_area,
#     'txtAttributeValue': property_no,
#     'txtImg': captcha_text,
#     **hidden_fields
# }

# response = session.post(url, headers=HEADERS, data=payload2, verify=False)
# with open("cersai_result.html", "w", encoding="utf-8") as f:
#     f.write(response.text)

# print("Saved final HTML to cersai_result.html")

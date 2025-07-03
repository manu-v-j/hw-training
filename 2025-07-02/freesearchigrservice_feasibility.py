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


year = "2024"
district = "30"  
village_input = "p" 
property_no = "11"

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
sel_village = Selector(text=res_village.text)

area_options = sel_village.xpath('//select[@id="ddlareaname"]/option[not(contains(text(), "Select"))]')

matched_areas = []
for option in area_options:
    text = option.xpath('./text()').get()
    value = option.xpath('./@value').get()
    if text.lower().startswith(village_input.lower()):
        matched_areas.append((text.strip(), value.strip()))

if matched_areas:
    print("\nMatched Areas (starting with '{}'):".format(village_input))
    for text, value in matched_areas:
        print(f"- {text} ({value})")
    selected_area = matched_areas[1][1]
    print(f"\nSelected Area: {selected_area}")
else:
    print(f"No areas found starting with '{village_input}'")
    selected_area = ""


payload_search = {
    "ScriptManager1": "UpMain|btnSearch",
    "ddlFromYear": "2024",
    "ddlDistrict": "30",
    "txtAreaName": "p",
    "ddlareaname": "Parela-shiwadi",
    "txtAttributeValue": "11",
    "txtImg":captcha_text,
    "FS_PropertyNumber": "",
    "FS_IGR_FLAG": "",
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATE": "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",
    "__VIEWSTATEGENERATOR": "BE9F1233",
    "__EVENTVALIDATION": "/wEdAEA1zES8+CA0LCJmkiAcStJ1ulgC2aBQeC21QDjK2HKD1K9JYTNtGDAGC8ioLPY8T8BjLqQLA99yEL8su3qcPmKqxkOHiG8yvbGJgdi+fvjbTLJBEfAUAzLyBRengr3hF98l4+5qnlyXUbVCorG6n5McLf4y42ZSmmgeWLZ6l53R8Uo1uDc5ZMEJj0rT5wjXWabLDjMKAvcNI3xzZn9Au+eJyKgrj6svcjydKabUyovPxvYiTgGEUm0yOF6g2/QaggdoABYuOAQFT6Btnz2rxraX4CYQV57eHDMGHXZnFBikzSUl7yt7IPOas38iLJqSxlnVUPOSOdjHKKU28JOkNEfBeKT13VHz9tFL1SIABVappWGJjSx3lR1FNySauw01clkVk2BGEKhSa3V8lvDYlA2SRSkpA8mk4mKFEB2lp0wxREc167AAjICz+x/wM94HK4CDKOoYGYU7s/3rr3ppuOjmWzA49bxGP0TsCW4B9m8scHiAZ4dQHzOq54sjQf9+6Men+o2NXzhPdVp1rfESCREfUm3gesdW62FhOnyH2FGrV/k9ZcFhMpZysYrbZbF6dej6Ui7d8Waley0M7o9wzyms6TJwuTC9CWRvL3k+iiKWzEmib0T9Ka969WgnvyOiKs+BEh22ZVmN33CKf6U6EDeXluJZCHsUAnw79Du4aGYgHGsyxju68OMCIB5BrAV0zY9z3cckcolFi7nVzRtZxOYnULrkFBZvvxhN7x467QutGzAhZU8TTPvWDUqfwN45bi42HBt75sXCFX0ujB8WHsnCoSte16JSLPosg2h8AxTvZ30ydHNHOskRTuUB2nTzagg0T2hi8tHnVi3FzQ20WVPjXScJcq4kPR/Oz0ctG5lKYgnPkWds2U/bJ9deeVbkHw6ZQBguMBpZacCSG1KVsaVF2uBlzNDqbaSrh7zxcXDytWoxkp/CJEEy+nYBtv7qJE4KwdFoAQcivvvbMqCCB1D79jvQKC4xSxjPBdaEBhDyunDGl3u+1yb9/30S8VcwzG59Pv9epfYXjrqXq94VBJ/u7RQbWhAezV15CSAFAXyLqFrOaRV6g0+gUGWJ4uBUGxmMgt0K0fp/8DHaINuVdJ2OmHlAZ0yiY8DSLm2xBIDfubBRzYLBK9VjnMbZLlh5TFy1r1niLt+vt40fC5Bu8QvOqc26ek2VYHGl8OazsF779J/2+QbOIBr7znKx3F1p0TD463fugIQRc/cSMEVxsmEojtTdVzRZn7DFyWrI8V/OY1GMDLkNC/3ciVTMvjNLwkpTqYOcayAElR+ZDgZ1Y6JmTvatLwOkZea8cagILyPUUUawC8X7HTibahW8mQtzRp3c34k3FIz8K3ej/QT9ck5X8HmW/jPWaJglh48pbvPs1iDizE+uhrt0IxNWWtCWjnY=",
    "__ASYNCPOST": "true",
    "btnSearch": "शोध / Search"
}

final_res = session.post(url, headers=headers, data=payload_search, verify=False)

with open("property_search_result1.html", "w", encoding="utf-8") as f:
    f.write(final_res.text)


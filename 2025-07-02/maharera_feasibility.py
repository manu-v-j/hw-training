import requests
from parsel import Selector
import re
import urllib3

# Disable SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Headers
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "host": "maharera.maharashtra.gov.in",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}
cookies = {
    "_ga": "GA1.1.1033835535.1751430732",
    "_ga_GDQ94DH7QZ": "GS2.1.s1751599530$o4$g1$t1751599575$j15$l0$h0",
    "JSESSIONID": "F2F6742AA57BD164C3FA5C4B923B9BC6"
}

# Step 1: Search request
url = "https://maharera.maharashtra.gov.in/projects-search-result"
payload = {
    "project_type": "0",
    "project_location": "",
    "project_name": "",
    "project_completion_date": "",
    "project_state": "27",
    "project_division": "",
    "project_district": "",
    "form_build_id": "form-3fInj71DquaCzr8idcYlB-WyZb8OWzrQsWSnmIBdsNM",
    "form_id": "projects_form",
    "op": "Search"
}

response = requests.post(url, headers=headers, data=payload, verify=False)
sel = Selector(text=response.text)

# Extracting data from HTML
state = sel.xpath('//div[text()="State"]/following-sibling::p/text()').getall()
pincode = sel.xpath('//div[text()="Pincode"]/following-sibling::p/text()').getall()
district = sel.xpath('//div[text()="District"]/following-sibling::p/text()').getall()
last_modified = sel.xpath('//div[text()="Last Modified"]/following-sibling::p/text()').getall()
details_url = sel.xpath("//a[contains(@class, 'click-projectmodal') and contains(@class, 'viewLink')]/@href").getall()

# Step 2: Loop through detail URLs and fetch contact details
# for url in details_url:
#     print(url)
    # project_id = re.search(r'/view/(\d+)', url).group(1)
  

import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIzNHFoLWJQZ1Nyck5WdG92Z1FROUhuX3JfZHhGeV9mUDVJVjkzT1VXMVVjIn0.eyJleHAiOjE3NTE4NjYwNzAsImlhdCI6MTc1MTg2MDA3MCwianRpIjoiNGMyNDJjODYtYTYyYy00ZGU4LTk5ZjQtYjM1ZGEzNjc4MDQ1IiwiaXNzIjoiaHR0cDovL2JhY2tlbmQtc3RhbmRhbG9uZS1rZXljbG9hay1zdmMtcHJvZDo4MDg5L2F1dGgvcmVhbG1zL2RlbW8iLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiODJkMjlhYzktNDVlYi00YzI1LWJiOTAtZmRlYWJjZGU3OGZjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZGVtb2NsaWVudDEiLCJzZXNzaW9uX3N0YXRlIjoiNWY3Y2UyYzMtMjJmNS00NzA0LThkOTktMWUxZDg5NGNlYTAyIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImFwcF9hZ2VudCIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiZGVtb2NsaWVudDEiOnsicm9sZXMiOlsiQUdFTlQiXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiQG1haGFyZXJhX3B1YmxpY192aWV3In0.ZMypqN92IMn7gTmupGnfSeWK2Efu-LsXnIbticV8mBEj3eVj3N3-NHN2EtQtHp8OrGruGbQ99pi3IDGMWkVwlDOYcPaliw3YcF6RYoe-uf6fsk7UpRXoOsJ3dNb4khOuu2qoUDStREo02ocIieDMd5qDm7ui8y_Z3hi-Fzmky_yUbMpia1VQQb_Vf2sRYk2ccgS6w8gTJ6z6ZHEIsIu9IXVa2e-Qgz7W9jikmDai7B-cR5NjwBthy0YISdOsLv-It9Hx-5bouOZBMdt7gSnO29PYuk19VQac7AJWQkT9HW_fpdkCafUSjiSLW3bAGqf4hkrfm0Urwoi45qYhqyuYAg"
api_url = "https://maharerait.maharashtra.gov.in/api/maha-rera-public-view-project-registration-service/public/projectregistartion/getProjectAndAssociatedPromoterDetails"

headers = {
    "accept": "application/json, text/plain, */*",
    "authorization": bearer_token,
    "content-type": "application/json",
    "origin": "https://maharerait.maharashtra.gov.in",
    "referer": "https://maharerait.maharashtra.gov.in/public/project/view/1",
    "user-agent": "Mozilla/5.0"
}


payload = {
    "projectId": 3 
}

response = requests.post(api_url, headers=headers, json=payload, verify=False)
if response.status_code==200:
    try:
        data=response.json()
        project_details=data.get("responseObject",{}).get("projectDetails",{})
        project_registration_no=project_details.get("projectGeneralDetails",{}).get("projectRegistartionNo","")
        date_of_registration=project_details.get("projectGeneralDetails",{}).get("reraRegistrationDate","")
        project_name=project_details.get("projectGeneralDetails",{}).get("projectName","")
        survey_nos_CTS_no=project_details.get("projectLegalLandAddressDetails",{}).get("addressLine","")
        proposed_completion_date_orignal=project_details.get("projectGeneralDetails",{}).get("projectProposeComplitionDate","")
        district=project_details.get("projectLegalLandAddressDetails",{}).get("districtName","")
        taluka=project_details.get("projectLegalLandAddressDetails",{}).get("talukaName","")
        village=project_details.get("projectLegalLandAddressDetails",{}).get("villageName","")
        pincode=project_details.get("projectLegalLandAddressDetails",{}).get("pinCode","")
        user_profile_id=project_details.get("projectGeneralDetails",{}).get("userProfileId","")
        print(user_profile_id)
    except Exception as e:
        print("Raw response:", response.text)


api_url_two="https://maharerait.maharashtra.gov.in/api/maha-rera-public-view-project-registration-service/public/projectregistartion/getMigratedBuildingDetails"
response = requests.post(api_url_two, headers=headers, json=payload, verify=False)
if response.status_code==200:
    data=response.json()
    summary_appartment=data.get("responseObject",[])
    for item in summary_appartment:
        building_name=item.get("buildingNameNumber","")
        apartment_type=item.get("apartmentType","")
        carpet_area=item.get("carpetArea","")
        number_apartment=item.get("numberOfApartment","")
        number_booked_apartment=item.get("numberOfBookedApartments")
        print(number_booked_apartment)
    


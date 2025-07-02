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
for url in details_url:
    project_id = re.search(r'/view/(\d+)', url).group(1)
    print(f"Fetching contact for Project ID: {project_id}")

    contact_api_url = "https://maharerait.maharashtra.gov.in/api/maha-rera-public-view-project-registration-service/public/projectregistartion/fetchPromoterPersonnelContactAddressDetails"
    payload = {
        "userProfileId": "121110",  # Make sure this ID is valid or required
        "projectId": project_id
    }

    try:
        response = requests.post(contact_api_url, headers=headers, json=payload, verify=False)
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
    except Exception as e:
        print(f"Error for Project ID {project_id}: {e}")

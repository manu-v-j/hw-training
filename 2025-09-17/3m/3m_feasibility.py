import requests
from parsel import Selector
import json,re
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'maverics_session=eyJpc3N1ZXIiOiJodHRwczovL3d3dy4zbS5jb20iLCJzZXNzaW9uX2lkIjoiMzVjMmFjN2ItYTg1Zi00MmMyLThlZmYtMzdkMzRhYzlhZmE5In0=; dtCookie=v_4_srv_7_sn_0890585F08FB36E4D1256FDAB319F54D_perc_100000_ol_0_mul_1_app-3A51e330a77f3260d5_1; ak_bmsc=6F4CF9A07EDAB6C1945C3CA8EAF2084A~000000000000000000000000000000~YAAQbbxWaEylHzOZAQAAMKPeVR3gwbJCN648zOBGy/CLcevt/XvYuvLEUZQ5iCMFI7OAnU+CAh87IAQ9eua5iJoJbijz6GjF7fTNRaHzPQqGZHriL4E8Im2WFVBL+WMRtSk56O+P5umDSqajqApM/CmlEhM3sogvqc01Om82QW5U8sRetICzKrDv4h91tNk2+OT648H20oLwW3AXmfobPX6jKPxwV6l0yPFqZxvS710degtWyDB9nHzM5+owxWUtaSC6fB/GSJHYqz14429q7gpQbp4kVAKj0UkuU8XsLJ7MqhsKrJtv9wku8Y0IS/e0AKn7iOS4YfEkYrIYtHvUN+8b3H8pR+DA8aLBSZMi5RUtgORc3Xq2LUP/krCF7v1rkYGG1C72Cl4=; rxVisitor=17580822797903ETH77KUFTN8HVOBEGGNCBRL29QCL5V6; dtSa=-; BVBRANDID=56f52633-0e6f-434b-94d0-bce44deb3c53; __privaci_cookie_consent_uuid=a0d32b72-9e78-4992-9fd0-e2c08cf1a6a3:10; __privaci_cookie_consent_generated=a0d32b72-9e78-4992-9fd0-e2c08cf1a6a3:10; AMCVS_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1; s_ecid=MCMID%7C45043749043018740420472954516726563472; AMCV_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1585540135%7CMCIDTS%7C20349%7CMCMID%7C45043749043018740420472954516726563472%7CMCAAMLH-1758687096%7C12%7CMCAAMB-1758687096%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1758089497s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20356%7CvVersion%7C4.4.0; ELOQUA=GUID=EA6B87B358134F7BB7505789BCF3F687; s_cc=true; _gcl_au=1.1.378398900.1758082302; _fbp=fb.1.1758082302792.964445710201931847; kampyle_userid=9490-dd6e-13f5-d0dc-1ff4-e8fe-7034-421a; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; __privaci_cookie_consents={"consents":{"13":1,"14":1,"15":1,"16":1},"location":"KL#IN","lang":"en","gpcInBrowserOnConsent":false,"gpcStatusInPortalOnConsent":true,"status":"record-consent-success","implicit_consent":false}; __privaci_latest_published_version=185; purpose_groups={"advertising":1,"analytics_customization":1,"essential":1,"performance_function":1}; AKA_A2=A; BVBRANDSID=c86b99cc-c3f3-4069-964f-011e5cb00fdc; utag_main=vapi_domain:3m.com$_sn:2$_se:1%3Bexp-session$_ss:1%3Bexp-session$_st:1758088635821%3Bexp-session$ses_id:1758086835821%3Bexp-session$_pn:1%3Bexp-session$v_id:019955def3150082d8ea8ca4161005065004105d0086e3m-cdp$dc_visit:2$dc_event:1%3Bexp-session$dc_region:me-central-1%3Bexp-session$_prevpage:MMM-ext%3Bexp-1758090435274; s_pers=%20gpv_pN%3D%252F3M%252Fen_US%252Fp%252Fc%252Foffice-supplies%252Fnotes-dispensers%252F%7C1758088639193%3B%20gpv_pURL%3Dwww.3m.com%252F3M%252Fen_US%252Fp%252Fc%252Foffice-supplies%252Fnotes-dispensers%252F%7C1758088639211%3B; adcloud={%22_les_v%22:%22c%2Cy%2C3m.com%2C1758088639%22}; rxvt=1758088640505|1758086831359; _uetsid=6b6ce5b0937c11f0a83d2352f77fe3d9; _uetvid=6b6d2ca0937c11f0b71b4fac51b0cdfa; dtPC=7$86831353_696h-vMEFMHTMUHMENIMMHHPLHGHHVDUEGRURI-0e0; kampyleUserSession=1758086842880; kampyleUserSessionsCount=2; kampyleUserPercentile=66.64431039205016; kampyleSessionPageCounter=1; s_sess=%20tp%3D7939%3B%20s_ppv%3D%252F3M%252Fen_US%252Fp%252Fc%252Foffice-supplies%252Fnotes-dispensers%252F%252C21%252C15%252C1694%3B; AWSALB=2gGu41pqQkCx35deW+c+J+DFPS9siazHDD+JG3wHCICwK0gcrBjRpWzwoXMRsaQnKNhn2vHqu1QW8ft7NuTqShoCO8TyDwYq3dEY5GazvRFLxtm5Rf/C8jiPEx3x; AWSALBCORS=2gGu41pqQkCx35deW+c+J+DFPS9siazHDD+JG3wHCICwK0gcrBjRpWzwoXMRsaQnKNhn2vHqu1QW8ft7NuTqShoCO8TyDwYq3dEY5GazvRFLxtm5Rf/C8jiPEx3x; ee1b5d445b4a4f48723fa58a17090439=ae44e6b3611455acd32031b91f260a88; bm_sv=D067843417788291BA14A05E53E6018A~YAAQVjkgF+X6SzSZAQAAA/MkVh3WLSIAgwi531XLb67H5PvCOIkrOslr2fOskIkgYJ9zcT9KpIzm6MePIpUdfkkveQDcmbzXOH5ktioiOP/61zHFJgRHWvPVfvB/1Yye1VFYpsJMsEAHLeaCLL/RMS5tv/Aq6Vm4kFFtFSBejQIfUp4H2jpoUXl5nRxp9hbQPaui8RsGnlYIHN1HAmRf+IU9/ASOYe4RHcnaqZPM9mbsInEm/EHCOKdxTPRs~1',
}
############################CRAWLER###################
start=0
product=[]
while True:
    params = {
        'size': '51',
        'start': str(start),
    }

    response = requests.get(
        'https://www.3m.com/snaps2/api/pcp-show-next/https/www.3m.com/3M/en_US/p/c/office-supplies/notes-dispensers/',
        params=params,
        headers=headers,
    )
    data=response.json()
    item_list=data.get('items',[])
    if not item_list:
        break
    for item in item_list:
        prooduct_url=item.get('url','')
        print(prooduct_url)
        product.append(prooduct_url)
    print(len(product))
    start+=51

########################PARSER######################
base_url="https://www.3m.com/3M/en_US/p/d/b40070717/"
response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
script_text = sel.xpath("//script[starts-with(text(), 'window.__INITIAL_DATA')]/text()").get()
json_text = re.sub(r'^window\.__INITIAL_DATA\s*=\s*', '', script_text).strip()
data = json.loads(json_text)
product_name=data.get('productDetails',{}).get('name','')
stock_number=data.get('productDetails',{}).get('stockNumber','')
upc=data.get('productDetails',{}).get('upc','')
images=data.get('productDetails',{}).get('imageUrl','')
resource_list=data.get('resources',[])[0]
safety_data_sheet=resource_list.get('url','')
breadCrumb_list=data.get('breadCrumb',[])
for item in breadCrumb_list:
    breadCrumb=item.get('value','')

product_description=sel.xpath("//div[@class='sps2-pdp_details--upper_details']/p/text()").getall()

from parsel import Selector
from curl_cffi import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.petco.com",
    "priority": "u=0, i",
    "referer": "https://www.petco.com/shop/en/petcostore/category/dog/dog-food?__cf_chl_tk=5xrWz8o.jGNvSw7CIaId2fYBx4vgjnMLA7oXJuklRkA-1750674766-1.0.1.1-iNa7W2LacDl_KiJ3oVmggpL5hIgA3Wa6yAgLTnyUnUU",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-arch": "\"\"",
    "sec-ch-ua-bitness": "64",
    "sec-ch-ua-full-version": "129.0.6668.58",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"129.0.6668.58\", \"Not=A?Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"129.0.6668.58\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform-version": "6.0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"
}

cookies={
  "rmn_session_id": "40f66624-7070-4c56-a187-7e0fcf4df3e7|1758429879827",
  "Edgescape-Country": "IN",
  "Edgescape-City": "Kanayannur",
  "Edgescape-State": "Kerala",
  "Edgescape-Zip": "683514",
  "Edgescape-Lat": "9.96667",
  "Edgescape-Long": "76.26667",
  "at_check": "true",
  "s_plt": "2.58",
  "s_pltp": "undefined",
  "AMCVS_4BED2CAD546FC7A60A4C98C6@AdobeOrg": "1",
  "s_ecid": "MCMID|64148766332738406291210738888735790525",
  "at_plp_filter_bopus": "yes",
  "at_pdp_view_plp": "test",
  "ConstructorioID_client_id": "c40816eb-4438-4a0e-ae6e-4532ad6dbaf9",
  "JSESSIONID": "0000JvjIU-gdri3nxhny8c-l56V:1ckhenqp4",
  "_fbp": "fb.1.1750653887481.935436826417690833",
  "CUSTOMER_ID": "-1002",
  "_cs_c": "0",
  "ck_oneTrustGTMconsent": "{\"GoogleAnalytics\":\"granted\",\"MediaAnalytics\":\"granted\"}",
  "_gcl_au": "1.1.1238002181.1750653888",
  "IR_gbd": "petco.com",
  "WC_bopusStoreId": "12356",
  "WC_preferredStoreId": "1147",
  "sm_uuid": "1750654533500",
  "_ga": "GA1.1.376915352.1750653890",
  "s_cc": "true",
  "_ScCbts": "[\"265;chrome.2:2:5\"]",
  "__adroll_fpc": "120a35e19439efecb68bf0e7ed1b7a71-1750653891928",
  "_sctr": "1|1750617000000",
  "_pin_unauth": "dWlkPVl6TTRNamczWkdNdE9UVm1OUzAwTVRnMExUazFPR0l0TWpaaVptTTBZakppWkdKag",
  "__idcontext": "eyJjb29raWVJRCI6IjJ5dFZYdmhVa1FTcmdGUGgxcVk2RFBqVldpWiIsImRldmljZUlEIjoiMnl0Vlh2TkI1UWxLUnlhaVF5dTY2ZjFBYkRMIiwiaXYiOiIiLCJ2IjoiIn0=",
  "kampyle_userid": "4b50-1ba6-3d02-81ad-0586-5a17-c98a-d159",
  "_scid": "fQVI4oR0iZW1vNmd8oIOX2CaBGEszDj0vXobng",
  "at_sticky_mobile_filter": "control",
  "_tt_enable_cookie": "1",
  "_ttp": "01JYDKEBX012MCWJAQDPT3NK6B_.tt.1",
  "WC_physicalStores": "12356,12356,12356,12356,12356",
  "at_app_smartbanner_mob_pdp": "control",
  "AT_RDSN_option": "var_B",
  "WC_PERSISTENT": "aPlYd2oa7Nq1d3KCbPktBeca9DLYHpihMBh+kAncNsI==;2025-06-22 23:20:28.596_1750659628596-262737_0",
  "WC_DeleteCartCookie_10151": "true",
  "targetCategoryAffinity": "\"Dog Food\"",
  "AMCVS_petcoprod@AdobeOrg": "1",
  "at_pdp_expose_variant_pricing": "new_design",
  "_gtmeec": "eyJwaCI6ImUzYjBjNDQyOThmYzFjMTQ5YWZiZjRjODk5NmZiOTI0MjdhZTQxZTQ2NDliOTM0Y2E0OTU5OTFiNzg1MmI4NTUifQ==",
  "_clck": "e94wjy|2|fx0|0|2000",
  "_iiq_fdata": "{\"pcid\":\"7df24e45-8b9e-8023-7ed8-65515700094d\",\"pcidDate\":1750669079498}",
  "s_sq": "[[B]]",
  "ttcsid": "1750669076900::2yKbaZQHrg9BgHxlTBIu.2.1750669919667",
  "ttcsid_C19NTGBQIA5GK7IN27CG": "1750669076898::xa90egR02HDVOuSOOg7-.2.1750669919943",
  "AMCV_4BED2CAD546FC7A60A4C98C6@AdobeOrg": "179643557|MCIDTS|20263|MCMID|64148766332738406291210738888735790525|MCAAMLH-1751275596|12|MCAAMB-1751275596|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1750677997s|NONE|MCAID|NONE|vVersion|5.5.0",
  "at_elevate_atc_desktop_pdp": "stickyatc",
  "_cfuvid": "A9w257pI1fnLX_tYCbBhJqzzHLMe48TS2Kc6mWRceXw-1750673953629-0.0.1.1-604800000",
  "_cs_mk_aa": "0.1862245181878881_1750673957086",
  "AMCV_petcoprod@AdobeOrg": "179643557|MCMID|64148766332738406291210738888735790525|MCIDTS|20263|MCOPTOUT-1750681163s|NONE|vVersion|5.5.0",
  "ck_OptanonConsent_fallback": "isGpcEnabled=0&datestamp=Mon Jun 23 2025 15:49:28 GMT+0530 (India Standard Time)&version=202503.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie Unique Id&hosts=&consentId=be27b49c-7a9e-469f-97cd-baf4ecef4a42&interactionCount=0&isAnonUser=1&landingPath=https://www.petco.com/shop/en/petcostore/product/purina-pro-plan-focus-sensitive-skin-and-stomach-salmon-and-rice-entree-wet-dog-food&groups=BG86:1,CADNS:1,C0004:1,C0001:1,C0003:1,C0002:1",
  "_clsk": "nxw3xm|1750673972351|2|1|i.clarity.ms/collect",
  "mbox": "PC#c38f07fd0bb54e858635dbf7b87b00bb.41_0#1813918783|session#00442eb58c3e4d2ead36bfcede6f7d2f#1750675843",
  "_scid_r": "eAVI4oR0iZW1vNmd8oIOX2CaBGEszDj0vXobqA",
  "__ar_v4": "MFVBQ7P6GFDI7MSZXFZSXC:20250623:25|7U2SBRJHSZE3ZFFXLXA23C:20250623:25",
  "IR_10290": "1750673988481|1792725|1750673988481||",
  "_cs_id": "06efa229-e482-aff8-eb90-f02d47b8e0aa.1750653889.4.1750673990.1750673935.1587060397.1784817889223.1.x",
  "IR_PI": "ec540c88-4fed-11f0-9316-65bae9208666|1750673988481",
  "_uetsid": "d05581404fec11f0bec2d3cf1c19b37f",
  "_uetvid": "d055d0c04fec11f08672cf5ca1347497",
  "datadome": "n1FoDNoue_~Z4DxODDzXBnNfCvkBU5QHFX0Ey~OG8kHFznkrkblSTqaiyetSSzphSJevJ9mMpfixSj8g4NsnlO0qabSrfZ7N5pk9xaw87Uv72M0e5q0qZWneoKFmL3A6",
  "_cs_s": "4.0.1.9.1750675821750",
  "kampyleUserSessionsCount": "4",
  "kampyleUserSession": "1750674081364",
  "kampyleSessionPageCounter": "1",
  "kampyleUserPercentile": "59.671109852237514",
  "ConstructorioID_session_id": "5",
  "ConstructorioID_session": "{\"sessionId\":5,\"lastTime\":1750674082007}",
  "OptanonConsent": "isGpcEnabled=0&datestamp=Mon Jun 23 2025 16:02:44 GMT+0530 (India Standard Time)&version=202503.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie Unique Id&hosts=&consentId=33ebf6fb-b452-4a36-9be0-68f64f148cec&interactionCount=1&isAnonUser=1&landingPath=https://www.petco.com/shop/en/petcostore/category/dog/dog-food&groups=BG86:1,CADNS:1,C0004:1,C0001:1,C0003:1,C0002:1",
  "__cf_bm": "GiyCcUXGqrfrtWPec_wOaCPfGc8Lmpby5K8h.ZbFlS4-1750674766-1.0.1.1-izpxaIYlon4vFItM2O7.djty3cbCl.ZBKVScFoMBD779wRUmhy4OdZ1iqR.YcLhzR21hPc4qYa1SaUyzMiHlOFerimZfEvStZv7qcAM5ZoYBEn8Yvvf_Mh7gZ49W6gWZ",
  "_ga_QS0VYFL03W": "GS2.1.s1750673949$o5$g1$t1750674766$j60$l0$h432748074",
  "_ga_3WR3LVE2JB": "GS2.1.s1750653889$o1$g1$t1750674766$j60$l0$h0",
  "cf_clearance": "jjp.0pBUCs6Cl0KTHr_eQ9M6mQtOJaXv5ni6AH5ezrg-1750680983-1.2.1.1-Lt25taoUar7juFhSjKKD_k4FU1TUI6V8oRG.amCJ5yVafD8gwC6mHusP0_Qn1mlc58ptkYXMt4FUzPn1bG8JYE4tCVrZZnbtyPziyWN2QxwMHFpu96lsBKczElYIzxq8TOypoj14mA9G4FbUAZL5k7_7naA_X1SnJfh2zjq0KXNt5quGjytDsPot66oK7l0oMgu7SeVzh6X8v7lTveZWbtSWQ4TYi2vID3GSOWig7X5t76qW5VIe48tB329u9Tbvyx_z1eYdF5AqPArhe3unKRZDQ.TAN798qc_.8U9_J1phkurR4zIrm03ChH3ZtELC60xCbaHQ67rST6yqUbrRjHLzlh_s8UZgStoQmdFzVD9jihPM9vKje7CLE25V1Nhj",
  "datadome":"BWJJGYLkeiqVsQBAhFfq4EkC1agu5SfWWQOWf3d01Q1CXDMv7RhKTViFSFyAGb9tDzDWdSQqt7zB4f~V4JOSSyWgPCE6CNrHursinuWE8uDIFFw~_AAOEpdtcHGSJuMb",
  "mbox":"PC#c38f07fd0bb54e858635dbf7b87b00bb.34_0#1813925788|session#38e29265ad8d45129cb45112679ba6f9#1750682848"}
payload={
  "c4a82114fa13151907f98bb901d03ddff8a811e8e36137fdbd8177b4127932c7": "KsFnF1M.U_Bvf.8W7CXprjN4tGwzSMPUS95jS_GRLLk-1750674766-1.2.1.1-imH6ANclVjRj3_D7VfVrOGQFGcxpeWQVb3uHQmgEoJe.RWwRcFgBVqfjLbuXCqjcp2a.HyvuI.4Ih3PI7puafZXJiYUoPPeP0yHu_8XNJup4k7Um4jP1a3dvG004XXs2RMTelRJXWMvHRivY6DzhsMYZvazlpYRQtF7VoYlLv2wuwp9to0FyE3pylM4H_LvUZW7ZAVQlHntUf88StsyVDLh2xH2U2eCuvy8v5DpL4YLA54CLDPVxr5ilLVT2zMxuofarDHaVK4p5odYhNOcdYcLN9xwic8fR.dalJ0oz_LNnNZHgpMo8dd3vIw2xXWacwLPdcQasQDSePc7lCdswCd9R9tXM.un9gtyDLo29WkOF1XMAHODbNQeKW41DyRw9cTKazgMlZOuHpNePg3HABPflkGi8AkqeOOIyK7fTpTKsSsq0obnbRtOCIoi1AkU2PYXLpo4NVghQREVgrLAdPZ1IMVuSI3Djznrw0n6qiMf.GG4GlsOwv54xP2hL7I543mahJtW5L3r_lS6VBuQQjSCtfC_kPb_DOjRu31SN7UYlHudajkqKKvsxBmXM15R8wvenS61ctJEj5C..U6lQqFhH3MXRdK8kwwxT105vC5Kat.mkfvVmL2YBf15teblRXPQC_MELZFAlKCwRe9xmyGA2JTBaiGRXVtv5CNziCTu0cgRX0XeneZmbQF3gHqPYqMphR.0BVGjrH7mbVwAGiEDUN87OfINTFthMiskNyaHN82XAdLmxMU26vJBXwC46ZEdHkuwm9urlE_Ajr3oGxO83aJi2vRU1Fq5LkLcIYAwkAQVdLKGgqQJInnW8j_mB4LitzD1oCLErE6YUc27AlUxCSiOEz3Eb4MCvlOYBaOVjM.0wF9qYUrrQTv88v7EoTsUNGR4g..sTtYmjZ9kYs1GITkelq8mDE9wXf1Rt.CBmWgjDanUsvoTTa539cBa9ANYsVIyq4183c3xy__Lexwd5zjgHsT.WYQtXlWE23iegojzvNaEedcRsKk0.P1zrwfzJ_yRpQXxeLoumNSVJ3dutAfs11JjGw3uP3rVr7g4",
  "03adcb242f87a86c3c276f84929dc4df4aa6c49bc3cda3efcb026ea97cc7aadc": "S4oztY0J1wfo_hijx6ejLUtx4EOrHrmSiRrqDRFeLcY-1750674766-1.2.1.1-xxPJiQs9SAtimdIuc6mcfaQLFfYLMd1GyZlxlf8zxOJAl0zchw7ZBC294NLcMpZDNo9zX4WzZXD6r7lwzivyTw.0DqK6p5Owj6wEN5bAGJWpfZNOA7I4wiROdbJKMgT6ommkWvfufN4AfuFxT9DXdgxVJxgazwWssxiklV8wb6blb5yqJX66iRv.OQpdn0uu6q6jRs4IBuQDZZ_8b.ZE3wDlqTkO0sYAKgqan8eTQBvTD6QFFIUO6UbR38lfavYyHXx1lLpXOOmohKAsx2ym7DWrQbaTLynmO5tELXUTzBmucuU_FfmlwvUgfoMlHzCTqAcrAi0nTlQLHzWwKL8C4psadmBu3TvgHKcabUQMU_B7kj4AoFTsOjFm7wUYyvbMD6KiM0ytHEPuLOML_kaF_tw02.NoJ8ht84us8m4qjBJT9LisjZkDDwMaUdvxFcETF5NAkqfnFYEFKwEYV_BI4PzJLxQA0KmdnXXh.uDMkcl0zsT7vVFWr8eYXrudGvMeQxDbMkBzE1O.CikQVcuUkzU6oGm4NGRJvwXVxliQbYYSGBUEAcAMgaLYkfFVQcyuIEjIy12lSc3AJ7kT0B2fFCudAax9TaiuiGl._o3gk3F5rzfu7q0NXcDC69zQ8n1ix6OqMejIRFTKxM1GRnoiqTMMA.D_7knaDQPo3mYlZxdSda1.0GAvGNmSICWOiDGQdK4orfmQOP2Bz_UnSrDSdRyRKeFRWarfte06z4rUvPUZaT1s8HDNsV7z1lQEP7s1vjZQISygU6JZvItEQC11CoM1GZNYiYyhJjyvhxzMGSlEZbGelqxdX1SEvAdDzzpoSL3CqO01eCazGxoo71jZhroU1uqb3snrSLC0CK5gFQoehfOBLRqJJS9WirP6GBEC6ZnimaCtyjEVXKDjqgMSffyo9tFj1yB8lhgpd14hgoFUUGu_zJlgxbQ.tb24MnWUlSFZUUDEP.AVCNQat3K1etUjA5jsPk8dbJ0M9EbJ8qeyDHDMiME5llXLx9YBCcxupJ8NNsJjCio2KcBQ2ZgkvROr20a7OAGOaVqYzUojK.YzEPTPv5z06LiAMUbeTICIRlQllKCBsxQnYshwbe4lFbukSzJlosBv0zuzd0xRu3F08SnOQ23G6nH4xXBAH556bFhkz969iOcg.wftejeosTwYw3ie4HV9ACV0Z0EBXZOXuh74e5aC7trGi0V6yQDiarqGLwUP4csewXfuON9Vk1OuY1jDuS0nKOrHLdHgvTtRWQpA0810aVeWWRKztSO.UJ9pqaJ_sPFbjFE2HeviMheMaesvAQIaZ0ZArXmD8Mj6E9z5bACxG2UVJOTfmx3E7R7aTDkbqEK9DyZU0x3wWSPHFxG.pkzjD_dOdAexzOydkyInND...",
  "1bdafd004c0e873ccf6b208787704bec986b34f843233b7c9a85ce8ca81e2ab8": "4qBU6M4qQuFOF1JmMWFsgvE2V.fze.m5BFx11NcJA5w-1750674789-1.0.1.1-ULQoC6e2iAXt8EYRrzvfbPDgj0Eo6ol2q1qcDyo9PMS83_dmiU63QdddvQPSHtXWKbgLRsmZkeTu.OE8_KJVew.wSrewQnkPvOaRcONoV3mY6LPfwedEPNKPEH6q6BrZKfg5LYVLu4Eku3_fGmgE1lq39kPwsAW8.1JrE7TsUuOIuAvAciMFzt_Hydy9HQfj"
}


# ##############################CRAWLER##############################
url="https://www.petco.com/api/proxy/header"
resp_post = requests.get(url,headers=headers)
print(resp_post.status_code)
print(resp_post.text)

















# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)  # visible browser
#     context = browser.new_context(
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
#         java_script_enabled=True
#     )
#     page = context.new_page()
#     page.goto("https://www.petco.com/shop/en/petcostore/category/dog/dog-food", timeout=60000)


#     print(page.title())
#     print(page.content())


###############################PARSER##############################
# from playwright.sync_api import sync_playwright
# from playwright_stealth import stealth_sync

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=100)  # headful mode
#     context = browser.new_context(
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#         locale="en-US",
#         viewport={"width": 1366, "height": 768}
#     )

#     page = context.new_page()
#     stealth_sync(page) 

#     page.goto("https://www.petco.com/shop/en/petcostore/category/dog/dog-food", timeout=60000)
#     page.wait_for_timeout(5000)  

#     if "captcha" in page.url or "captcha" in page.content():
#         print("Still blocked or CAPTCHA present.")
#     else:
#         print("✅ Page loaded. Start scraping.")
#         print(page.title())
#         html = page.content()
#         print(html[:1000]) 



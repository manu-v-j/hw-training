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
    # 'cookie': 'OptanonAlertBoxClosed=2025-09-17T04:09:08.328Z; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Sep+17+2025+09%3A41%3A43+GMT%2B0530+(India+Standard+Time)&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=&consentId=7f79226c-9ee9-44fc-9816-61f7b559fa29&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=IN%3BKL&AwaitingReconsent=false; SSID_Olv0=CQDNBh0qAAAAAAA-NMpoS_4CED40ymgBAAAAAAAAAAAAPjTKaAB8xApkAQHmHisAPjTKaAEAaGMBA_wRKwA-NMpoAQDjZAEBpTIrAD40ymgBAA; SSSC_Olv0=961.G7550905166401306187.1|90984.2822652:91146.2825958:91363.2831013; ai_user=D+N+35zir6MSgYUI6eiwes|2025-09-17T04:08:34.157Z; _fbp=fb.1.1758082115995.2023299779; _ga=GA1.1.1300466262.1758082115; _gcl_au=1.1.1013587649.1758082148; FPID=FPID2.2.S7tdMtMLtEYCoN5jjSLrFB6DPx4LQu7yLMl8tvTMFys%3D.1758082115; FPLC=q0IJ6yFQ04kEG2U2OkU2Lns0Ugu0i4sokveuMOhD4XUhNePAIG0IJi3wwEpfeY28NrPnLg0tK7XkIsr%2BvEfKltMEEn0kI9VgDaxNR4XQBq74YGaYLk8TawkkMmgLBQ%3D%3D; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; _hjSession_2068204=eyJpZCI6IjVjYmUxMmIwLWM3ODYtNDBlYS05NmNjLWQ4OTE4N2UwODM2OCIsImMiOjE3NTgwODIxNTgyNzYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; smc_ls_session=1758082158521; _clck=1mvyew4%5E2%5Efze%5E0%5E2086; tfpsi=1c85f35e-4b8b-4ca5-b45f-39fcbc8fa625; _hjSessionUser_2068204=eyJpZCI6ImQ4NjFlNTY2LTZmYzMtNTRlYy04YTYyLWU4M2NiNjhiYzZiZCIsImNyZWF0ZWQiOjE3NTgwODIxNTgyNzMsImV4aXN0aW5nIjp0cnVlfQ==; _uetsid=1450a270937c11f0ab932d6327bf3b85; _uetvid=14512b60937c11f0a7dc9746a3e8df45; SSRT_Olv0=ADXKaAADAA; FPGSID=1.1758082148.1758082310.G-2TB7ZSLYMJ.7-vVflvaOfRxP_RRVJpyZg; _clsk=ns50zm%5E1758082315078%5E2%5E1%5Eo.clarity.ms%2Fcollect; _ga_2TB7ZSLYMJ=GS2.1.s1758082115$o1$g1$t1758082328$j43$l0$h2125786545; ai_session=A1HrXj50UIiB3ASsZO+7YB|1758082116247|1758082375232',
}

MONGO_URL="mongodb://localhost:27017"
MONGO_DB="lorespresso"
COLLECTION_CATEGORY="category_details"
COLLECTION="product_link"
COLLECTION_DETAILS="product_details"
COLLECTION_ERROR='error_link'

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


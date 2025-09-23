import requests

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
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '__privaci_cookie_consent_uuid=1eda76f3-0805-4cf7-9979-71d5d581e53f:10; __privaci_cookie_consent_generated=1eda76f3-0805-4cf7-9979-71d5d581e53f:10; BVBRANDID=d7a61f2a-8f87-41e6-ae9d-6be8e1efff50; liveagent_oref=https://www.3m.com/3M/en_US/p/c/cleaning-supplies/chemicals-disinfectants/degreasers/; liveagent_vc=3; liveagent_ptid=57813b30-65b3-474b-94aa-e9e81798b910; s_ecid=MCMID%7C45043749043018740420472954516726563472; ELOQUA=GUID=94631ED07A024EF9917CB770D9AB006A; _fbp=fb.1.1758100532116.328181584795329501; _gcl_au=1.1.929425903.1758100532; kampyle_userid=619a-0f7f-07a8-9a5c-619a-45aa-59cd-a8f0; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; __privaci_cookie_consents={"consents":{"13":1,"14":1,"15":1,"16":1},"location":"KL#IN","lang":"en","gpcInBrowserOnConsent":false,"gpcStatusInPortalOnConsent":true,"status":"record-consent-success","implicit_consent":false}; __privaci_latest_published_version=185; _gd_visitor=69340f6f-01ed-4336-8174-226021af82b8; _ga=GA1.1.1316907243.1758102361; _ga_4V9QC0J8WQ=GS2.1.s1758102361$o1$g1$t1758102610$j41$l0$h1837676743; _uetvid=dc808e4093a611f0ae8423515be4912a; AKA_A2=A; ak_bmsc=D24688C638C056B3E3909C1F57AF8ED4~000000000000000000000000000000~YAAQOKIauBkdW1CZAQAACJW/bx2fH22j87vI3so7i3vBz4wV9Qqgx+CtVUxY1PLMSU1cVMcnbxp2jgJEWSnXZmlhFxMGLXKm0dMT60+BIIa+DeTDP7tuogbtv1pJHaETZo1TOO+fq4iU6o+5oi//vzb2AGRnwdf1YUHYDw+7kk2oYx5wqm/U7Loxm4xXSqeJatdrtzI8aSeIqcWt9Jad8b05DwShboqlMMC5T9PadfepDppe1gjowF4Z9YA+7Xra2ci6XfQOj6kZt6PEEjPm/70vkkVwpYYFt07uzUI10fOHYzXF5KGLmXEdIxXnqXhovqilXPK0fHFgzyC93k43tD27cym2sTGE3z0V339XWXXohsaYZtyMc49dwgon3sH+emS/lIJzhn884uVWiKBTifSUvWW4v1UIgYbkwyIgoTur; rxVisitor=175851645122146C4VO65JBP4D3OABTK0SOP275QHJMBN; dtSa=-; purpose_groups={"advertising":1,"analytics_customization":1,"essential":1,"performance_function":1}; rxvt=1758518252807|1758516451224; dtPC=-6138$516451212_653h-vMPDFNMEFOUMSSAMSITUWJUKCCVUWTHBW-0e0; maverics_session=eyJpc3N1ZXIiOiJodHRwczovL3d3dy4zbS5jb20iLCJzZXNzaW9uX2lkIjoiZWQ1NWJhZTYtOTI0YS00ZTM2LWExYTQtZjI5OTJiNTY3YTQxIn0=; dtCookie=v_4_srv_8_sn_4SIPHGR201FH88CGSDD8KHFOG4KIIVS6_perc_100000_ol_0_mul_1_app-3A51e330a77f3260d5_1; AMCVS_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1; AMCV_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1585540135%7CMCIDTS%7C20354%7CMCMID%7C45043749043018740420472954516726563472%7CMCAAMLH-1759121255%7C12%7CMCAAMB-1759121255%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1758523655s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; utag_main=vapi_domain:3m.com$_sn:5$_se:1%3Bexp-session$_ss:1%3Bexp-session$_st:1758518255367%3Bexp-session$ses_id:1758516455367%3Bexp-session$_pn:1%3Bexp-session$v_id:019955def3150082d8ea8ca4161005065004105d0086e3m-cdp$dc_visit:4$dc_event:1%3Bexp-session$dc_region:me-central-1%3Bexp-session$_prevpage:MMM-ext%3Bexp-1758520054950; kampyleUserSession=1758516456793; kampyleUserSessionsCount=4; kampyleUserPercentile=10.609678435221849; kampyleSessionPageCounter=1; kampylePageLoadedTimestamp=1758516456852; s_cc=true; adcloud={%22_les_v%22:%22c%2Cy%2C3m.com%2C1758518256%22}; s_pers=%20gpv_pN%3D%252F%7C1758518263597%3B%20gpv_pURL%3Dwww.3m.com%252F%7C1758518263600%3B; AWSALB=WqjLrImrzYiGWDAkTh9tGTFroW2jNOAlKdbOkVCKC+RHJeOCmdylMEAgrxEjqgPfiQtL2Ue5ccSYT22nQsIRzuXnX9OaSuw+U2h3rLJvRx0PDcBQUJJcXj2Wzn2O; AWSALBCORS=WqjLrImrzYiGWDAkTh9tGTFroW2jNOAlKdbOkVCKC+RHJeOCmdylMEAgrxEjqgPfiQtL2Ue5ccSYT22nQsIRzuXnX9OaSuw+U2h3rLJvRx0PDcBQUJJcXj2Wzn2O; bm_sv=EF6706CF557241513DC51477916F9E28~YAAQOKIauMcdW1CZAQAA9NG/bx3xodcR5h0SPv4/lTaszodbKIarfq+RbdPOms+dtxVxNrflH9TNM85krOTJqg5BcyMeauWG0pHrgXoOMbUSZckiz9rRAg5ai3k8H3DV+UZxCbo6CO1OylHWfTsmdERfdv8EAUicO/bvYuRMznzzZUjy3StUC3N3w3i4/UVFEYyuR31ptyqTfbHRCHf9VbK5IR2yKVFXW7GaV7GiQGCinThIlRgErTo4MHM=~1; s_sess=%20tp%3D4138%3B%20s_ppv%3D%252F%252C39%252C15%252C1610%3B; RT="z=1&dm=www.3m.com&si=2a642e5f-aa4d-4a9b-be31-7c252c61e3a0&ss=mfunagru&sl=1&tt=2b4&rl=1&ld=2ba&ul=1xru"',
}

MONGO_URL="mongodb://localhost:27017"
MONGO_DB="3m"
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
# import requests
# from parsel import Selector
# import json,re,csv,os
# cookies = {
#     'tc_ts': '6',
#     'CAID': '202508200543544880226720',
#     'FRONTONE_ONLINE': '1759915583',
#     'FRONTONE_SESSION_ID': '49246b692df462a03083191003c1dbbdcd14e1c5',
#     'FRONTONE_SESSID': '1kmrtukkuud8oo9mjver6iu0og',
#     'OptanonAlertBoxClosed': '2025-09-08T09:26:47.933Z',
#     'eupubconsent-v2': 'CQXaheQQXaheQAcABBFRB7FsAP_gAAAAAChQJCQDAAIQAYABkALYAYQBCACkAGuAQMAwgBoAF5gSEAAAAKEgAgLzHQAQF5jgAIEhCUAEBeZSACAvMAAA.f_wAAAAAAAAA',
#     'OneTrustGroupsConsent': '%2CC0048%2CC0001%2CC0040%2CC0032%2CC0039%2CC0036%2CC0041%2CC0042%2CC0044%2CC0043%2CC0045%2CC0049%2CC0047%2CC0023%2CC0056%2CC0038%2CC0082%2CC0026%2CC0177%2CC0113%2CC0089%2CC0092%2CC0190%2CC0166%2CC0222%2CC0231%2CC0263%2CC0100%2CC0280%2CC0004%2CC0054%2CC0274%2CC0022%2CC0052%2CC0034%2CC0063%2CC0157%2CC0003%2CC0212%2CC0243%2CC0081%2CC0051%2CC0136%2CC0135%2CC0007%2CV2STACK42%2C',
#     'loopCd': 'adloop_click_1',
#     '_ga': 'GA1.2.2117932018.1757323614',
#     '_cs_c': '0',
#     '_fbp': 'fb.1.1757323631882.488890235557044486',
#     '_scid': '11SmMJXE0nyzt4wVtZuXpehpYrHKqMUt',
#     '_lr_geo_location_state': 'KL',
#     '_lr_geo_location': 'IN',
#     '_sctr': '1%7C1757269800000',
#     'adv_ui': 'LsjHwHhcEfCAXxVMcghr2g',
#     'beyable-TrackingId': '5eec4893-96f0-4cac-86a2-15779172ff3f',
#     'beyable-MustBeDisplayed': 'true',
#     '_pin_unauth': 'dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg',
#     'iadvize-8787-vuid': '%7B%22vuid%22%3A%22f21cc0fcd4de4f2594953b4bd9cd449ce46d9543f0214%22%2C%22deviceId%22%3A%226a45388d-c0cb-4081-bb0f-1f83ba5395f0%22%7D',
#     'tc_cj_v2_cmp': '',
#     'tc_cj_v2_med': '',
#     '_ScCbts': '%5B%2282%3Bchrome.2%3A2%3A5%22%5D',
#     'rlvt_tmpId': 'cmfc5c55c00002vax7iyk39be',
#     'QSI_SI_dpbRpgdj5NeO5PE_intercept': 'true',
#     'tc_ab': '1',
#     'cf_clearance': 'Mp2qZB8XGO9kwvodoVkK6H3pvyipgdlL7Bosff5QXWo-1757416102-1.2.1.1-9R97x63eo1qloXUcPQIRPdvpFKc_vXG9uvd955Zk0G0Gu5z.hYLDgTVz4dfzzpoKToz21ewvOSeRTuGl9igci_MVwPsgI.d4xAMJl.SxiXQ387SRrQs_JvURvkb..VcOYa8tENt.Sm0AYlOgCdyKL3b986ZkDkWkEgNoD5U.XzIjnDtUFiJn0Qux.oqPijupM3MjeHdBaTrhBVWHhV3W.RWoJjUOGSj_wH8KBaKHRNY',
#     '_cs_mk': '0.5197409494972385_1757416105296',
#     'loop_num': 'eff27220-0934-4573-c7d3-68528d1d9e5a%3ALSUdd%7CDR%7C%2Fp%2Fbiscuits-chocolats-bubble-chock-carrefour-sensation-3560071530303',
#     'tc_cj_v2': '%5Ecl_%5Dny%5B%5D%5D_mmZZZZZZKQOQNKPLRNMJMZZZ%5D',
#     'pageCounterCrfOne': '30',
#     'random_id': '690170408',
#     'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fwww.carrefour.fr%252Fp%252Fbiscuits-bio-avoine-pepites-de-chocolat-bjorg-3229820794525',
#     '_rdt_uuid': '1757323638025.f5838232-c844-4a52-9353-77258e977637',
#     '_rdt_em': ':ef55e52f905081ab72d1b8b1425aa3f63c86aa07a151b1e1ae8f7e5e3776d2ed,3ef2d1568335e3c241b0a0466356844ab34657fcc9353ccb8f68b7663414ddf5,7b8e8b8f2f7c1cc694587a0780a2d596c90e8b56edb09191f65c2deaf20f038a,7b8e8b8f2f7c1cc694587a0780a2d596c90e8b56edb09191f65c2deaf20f038a',
#     '_scid_r': '7dSmMJXE0nyzt4wVtZuXpehpYrHKqMUtcIOkDw',
#     '_uetsid': 'f81da8408c9511f0954a23edb4412dab',
#     '_uetvid': 'f81e0f408c9511f0b467058efd29d9b8',
#     '_ga_T8GFZP2DDH': 'GS2.2.s1757416111$o7$g1$t1757416287$j56$l0$h0',
#     'cto_bundle': '_taFAF9mWGclMkJJd3hoSWtYZmJ3ZVZrWWhKdTJkemZZNFI2M3dhT2ZHU0tlakdZRDc3dHZRY1lRMnU5QnR1d0RWMnMlMkZ2QVQydm1yTThFUHRKb3Zja3h5Y1RtMWFOSW9pdTJNdGZiJTJGVHI3M1F5R3lHbHR2Vk5XTGlSdjlodkdlRmI4SjdvUkg4V2RlQm5SRVpkN1hFbEZrNG9wOW8yVHY5OSUyRnRFZVYwREQ5OVFlYXE1VSUzRA',
#     '_gcl_au': '1.1.1619292720.1757323614',
#     'ABTasty': 'uid=37smrptyzzvzfbrc&fst=1757323618618&pst=1757414203538&cst=1757416105833&ns=6&pvt=45&pvis=4&th=1497485.0.18.18.1.1.1757325453053.1757400097780.0.2_1497487.0.19.19.1.1.1757325448256.1757400091738.0.2_1497491.0.24.4.2.1.1757323620896.1757416289336.0.6',
#     'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Sep+09+2025+16%3A41%3A30+GMT%2B0530+(India+Standard+Time)&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f4347bc5-3d44-474b-b2ce-2679431884d8&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0048%3A1%2CC0001%3A1%2CC0040%3A1%2CC0032%3A1%2CC0039%3A1%2CC0036%3A1%2CC0041%3A1%2CC0042%3A1%2CC0044%3A1%2CC0043%3A1%2CC0045%3A1%2CC0049%3A1%2CC0047%3A1%2CC0023%3A1%2CC0056%3A1%2CC0038%3A1%2CC0082%3A1%2CC0026%3A1%2CC0177%3A1%2CC0113%3A1%2CC0089%3A1%2CC0092%3A1%2CC0190%3A1%2CC0166%3A1%2CC0222%3A1%2CC0231%3A1%2CC0263%3A1%2CC0100%3A1%2CC0280%3A1%2CC0004%3A1%2CC0054%3A1%2CC0274%3A1%2CC0022%3A1%2CC0052%3A1%2CC0034%3A1%2CC0063%3A1%2CC0157%3A1%2CC0003%3A1%2CC0212%3A1%2CC0243%3A1%2CC0081%3A1%2CC0051%3A1%2CC0136%3A1%2CC0135%3A1%2CC0007%3A1%2CV2STACK42%3A1&intType=1&geolocation=IN%3BKL&AwaitingReconsent=false',
#     '_cs_s_ctx': '%7B%22firstViewTime%22%3A1757410121594%2C%22firstViewUrl%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2Fr%2Fepicerie-sucree%2Fbiscuits%3Fpage%3D3%22%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2Fr%2Fepicerie-sucree%2Fbiscuits%3Fpage%3D3%22%2C%22previousViewUrl%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2Fp%2Fbiscuits-tablette-chocolat-lait-simpl-3560070936106%22%2C%22currentViewUrl%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2Fp%2Fbiscuits-au-chocolat-au-lait-delichoc-3116430218483%22%7D',
#     '_cs_id': '15572d0c-6740-a07c-a6f1-7b0241f070ac.1757323631.4.1757416291.1757410121.1743092064.1791487631528.1.x',
#     'aaaaaaaaa944fac35b02f4d9a99619247b88ad463': 'ddf15341-90b0-466c-8206-7e114c159923.1757416347417.1757416347417.$bey$https%3a%2f%2fwww.carrefour.fr%3a443%2fp%2fbiscuits-au-chocolat-au-lait-delichoc-3116430218483$bey$1',
#     'aaaaaaaaa944fac35b02f4d9a99619247b88ad463_v': '6.26.7911590.FP:1:17$bey$C:0:9....$:$.C$b$1757416347417',
#     'aaaaaaaaa944fac35b02f4d9a99619247b88ad463_cs': 'ODI5NDc5NTUtMGE1NC00MzlkLTg5OWMtMzNiZjRhYWUzNmEw',
#     '_cs_s': '13.5.U.9.1757418653524',
#     '_ga_S8S9P3NTNV': 'GS2.2.s1757416109$o8$g1$t1757416854$j60$l0$h2043037708',
#     'carrefour_counter': '1757416855253%7C13172905193958%7Cp11%7Ce11%7Cv1%7Cc257.34%7CServerSide',
#     '__cf_bm': '1s4eBJKNDO1mN_H9q0fFelAcp4pHVl2h0HT_N334UkQ-1757416855-1.0.1.1-CLL_84HEJmtIS4P8XiLjyiVIIMJ49JW4j.p9Ig2rHjjLoU8UXZce5kKwLn_ZB6HYjbr2rwWPGOtDG2IukRhUvZcqGCigd6Lj998y_bd0J5c',
#     '_dd_s': '',
# }
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'max-age=0',
#     'priority': 'u=0, i',
#     'referer': 'https://www.carrefour.fr/',
#     'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#     'sec-ch-ua-arch': '"x86"',
#     'sec-ch-ua-bitness': '"64"',
#     'sec-ch-ua-full-version': '"138.0.7204.183"',
#     'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.183", "Google Chrome";v="138.0.7204.183"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-model': '""',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-ch-ua-platform-version': '"6.11.0"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'service-worker-navigation-preload': 'true',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
#     # 'cookie': 'tc_ts=6; tc_ab=0; CAID=202508200543544880226720; FRONTONE_ONLINE=1759915583; FRONTONE_SESSION_ID=49246b692df462a03083191003c1dbbdcd14e1c5; FRONTONE_SESSID=1kmrtukkuud8oo9mjver6iu0og; OptanonAlertBoxClosed=2025-09-08T09:26:47.933Z; eupubconsent-v2=CQXaheQQXaheQAcABBFRB7FsAP_gAAAAAChQJCQDAAIQAYABkALYAYQBCACkAGuAQMAwgBoAF5gSEAAAAKEgAgLzHQAQF5jgAIEhCUAEBeZSACAvMAAA.f_wAAAAAAAAA; OneTrustGroupsConsent=%2CC0048%2CC0001%2CC0040%2CC0032%2CC0039%2CC0036%2CC0041%2CC0042%2CC0044%2CC0043%2CC0045%2CC0049%2CC0047%2CC0023%2CC0056%2CC0038%2CC0082%2CC0026%2CC0177%2CC0113%2CC0089%2CC0092%2CC0190%2CC0166%2CC0222%2CC0231%2CC0263%2CC0100%2CC0280%2CC0004%2CC0054%2CC0274%2CC0022%2CC0052%2CC0034%2CC0063%2CC0157%2CC0003%2CC0212%2CC0243%2CC0081%2CC0051%2CC0136%2CC0135%2CC0007%2CV2STACK42%2C; loop_num=eff27220-0934-4573-c7d3-68528d1d9e5a%3ALS82N%7CIN%7Cwww.carrefour.fr; loopCd=adloop_click_1; _ga=GA1.2.2117932018.1757323614; _cs_c=0; _fbp=fb.1.1757323631882.488890235557044486; _scid=11SmMJXE0nyzt4wVtZuXpehpYrHKqMUt; _lr_geo_location_state=KL; _lr_geo_location=IN; _sctr=1%7C1757269800000; adv_ui=LsjHwHhcEfCAXxVMcghr2g; beyable-TrackingId=5eec4893-96f0-4cac-86a2-15779172ff3f; beyable-MustBeDisplayed=true; _pin_unauth=dWlkPU5ESmlOek0wWVRFdE16RmtaQzAwWVRVeUxUazVNMk10TldObU16aG1NREUzWkRjeg; iadvize-8787-vuid=%7B%22vuid%22%3A%22f21cc0fcd4de4f2594953b4bd9cd449ce46d9543f0214%22%2C%22deviceId%22%3A%226a45388d-c0cb-4081-bb0f-1f83ba5395f0%22%7D; tc_cj_v2_cmp=; tc_cj_v2_med=; _ScCbts=%5B%2282%3Bchrome.2%3A2%3A5%22%5D; tc_cj_v2=%5Ecl_%5Dny%5B%5D%5D_mmZZZZZZKQOQMLPSSRJQOZZZ%5D; aaaaaaaaa944fac35b02f4d9a99619247b88ad463_v=1.10.3349929.FP:10:10....$:$.C$b$1757323658251; cf_clearance=kS0bEvvnMRfpHd7cNaD4XsPdmypeisPYKrK7qynhf5A-1757397880-1.2.1.1-hNYXrJFRJ6yYHP8nKcuHCi7Rf3jA2EFkPRtrhVJ7Z97E4WOia3F7W5gLU6FVovmMn0gs2siosaO262ukS7K4oyL11AV9WQsuzMHQrQ6OKYJQZXpTnX4zRvYwuPbp.q9628lpSYgXc9wf6OVFuNltU6Fii.jCncm4YiPNAT9wsnnwGWL1TknkdKJk_Y8FWO0yzfbeJvfpwUAp52HQtyPLZ7CdNycPC.Jt2APPFgVRMvc; _cs_mk=0.894330628706784_1757397884679; rlvt_tmpId=cmfc5c55c00002vax7iyk39be; pageCounterCrfOne=6; random_id=108641876; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.carrefour.fr%252F; _scid_r=5NSmMJXE0nyzt4wVtZuXpehpYrHKqMUtcIOk9w; _rdt_uuid=1757323638025.f5838232-c844-4a52-9353-77258e977637; _rdt_em=:7b8e8b8f2f7c1cc694587a0780a2d596c90e8b56edb09191f65c2deaf20f038a,7b8e8b8f2f7c1cc694587a0780a2d596c90e8b56edb09191f65c2deaf20f038a; ABTasty=uid=37smrptyzzvzfbrc&fst=1757323618618&pst=1757323618618&cst=1757397886067&ns=2&pvt=21&pvis=6&th=1497485.0.10.10.1.1.1757325453053.1757327021884.0.1_1497487.0.10.10.1.1.1757325448256.1757327016883.0.1_1497491.0.15.15.1.1.1757323620896.1757327004692.0.1; cto_bundle=Lr1GA19mWGclMkJJd3hoSWtYZmJ3ZVZrWWhKdXl1aSUyRnFYdEh3UlptNXVSZ2ZDT3JjRnpjVFN3eFNGJTJCR2tlTkJEaDFOJTJGOVBHZ1dtUXFWRzUxQXJYNWNFQUY1OFc0b1VwQkczZFFNTyUyQkNRQll2T0VMRVhwMjRsOEJWJTJGWGFKQVh1bmYyNHg3bkR0cHRjQU9Iclh0bnMlMkJINTRtVG1pY0xKRDc2Rk4lMkZ4UnFTJTJCeXFlZ0IySGslM0Q; _uetsid=f81da8408c9511f0954a23edb4412dab; _uetvid=f81e0f408c9511f0b467058efd29d9b8; _ga_T8GFZP2DDH=GS2.2.s1757397893$o3$g1$t1757397968$j54$l0$h0; _gcl_au=1.1.1619292720.1757323614; __cf_bm=zCutyaJrxGaHr1j1u1XQ9xnqKzOh.JS2z.nZNyALUxI-1757397971-1.0.1.1-tZfqcnP2MLAn.RSIh3a3V882bPflM4F7kdp8UnlRemPNkSEPiL3xUho4ShnM4YV6FLJuXuPKiNnVlte2.NCekKHwfgkNRfl.1bDQzEnjhfY; _ga_S8S9P3NTNV=GS2.2.s1757397889$o3$g1$t1757397972$j40$l0$h500566867; carrefour_counter=1757397972667%7C14907833304244%7Cp41%7Ce41%7Cv1%7Cc257.34%7CServerSide; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Sep+09+2025+11%3A36%3A12+GMT%2B0530+(India+Standard+Time)&version=202505.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f4347bc5-3d44-474b-b2ce-2679431884d8&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0048%3A1%2CC0001%3A1%2CC0040%3A1%2CC0032%3A1%2CC0039%3A1%2CC0036%3A1%2CC0041%3A1%2CC0042%3A1%2CC0044%3A1%2CC0043%3A1%2CC0045%3A1%2CC0049%3A1%2CC0047%3A1%2CC0023%3A1%2CC0056%3A1%2CC0038%3A1%2CC0082%3A1%2CC0026%3A1%2CC0177%3A1%2CC0113%3A1%2CC0089%3A1%2CC0092%3A1%2CC0190%3A1%2CC0166%3A1%2CC0222%3A1%2CC0231%3A1%2CC0263%3A1%2CC0100%3A1%2CC0280%3A1%2CC0004%3A1%2CC0054%3A1%2CC0274%3A1%2CC0022%3A1%2CC0052%3A1%2CC0034%3A1%2CC0063%3A1%2CC0157%3A1%2CC0003%3A1%2CC0212%3A1%2CC0243%3A1%2CC0081%3A1%2CC0051%3A1%2CC0136%3A1%2CC0135%3A1%2CC0007%3A1%2CV2STACK42%3A1&intType=1&geolocation=IN%3BKL&AwaitingReconsent=false; _cs_s_ctx=%7B%22firstViewTime%22%3A1757397892979%2C%22firstViewUrl%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2F%22%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2F%3F__cf_chl_tk%3D2sgA1HVrUSOSNM1b3xFPN47wZN_Mxgp3DOK1J5GQ83c-1757397852-1.0.1.1-jUz1uuLz2YeLykGVuqp3LI1Um037ktssWXWW3GzJaRE%22%2C%22previousViewUrl%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2Fr%2Ffruits-et-legumes%2Ffruits%2Fpommes-poires-et-raisins%2Fraisins%22%2C%22currentViewUrl%22%3A%22https%3A%2F%2Fwww.carrefour.fr%2Fr%2Ffruits-et-legumes%22%7D; _cs_id=15572d0c-6740-a07c-a6f1-7b0241f070ac.1757323631.3.1757397973.1757397892.1743092064.1791487631528.1.x; _cs_s=6.0.U.9.1757399773188; _dd_s=logs=1&id=71fd7535-5019-47a6-946a-c2550db2c929&created=1757397889561&expire=1757398876674',
# }



# category_urls = [
#     "https://www.carrefour.fr/r/epicerie-sucree/chocolats-et-bonbons",
#     "https://www.carrefour.fr/r/epicerie-sucree/gateaux-moelleux",
#     "https://www.carrefour.fr/r/epicerie-sucree/compotes-fruits-au-sirop-et-cremes-desserts",
#     "https://www.carrefour.fr/r/epicerie-salee/pour-laperitif",
#     "https://www.carrefour.fr/r/fruits-et-legumes/fruits-et-legumes-secs"
# ]



# all_product_urls = []  

# for category_url in category_urls:
#     print(f"\nScraping category: {category_url}")
    
#     url = f"{category_url}?noRedirect=0&page=1"
#     response = requests.get(url, cookies=cookies, headers=headers)

    
#     sel = Selector(text=response.text)
#     product_urls = sel.xpath("//a[@data-testid='product-card-title']/@href").getall()
    
#     if not product_urls:
#         print(f"No products found in {category_url}")
#         continue
    
#     for relative_url in product_urls[:25]:
#         full_url = f"https://www.carrefour.fr{relative_url}"
#         all_product_urls.append(full_url)
#         print(full_url)

# print(f"\nTotal product URLs found across all categories: {len(all_product_urls)}")

# csv_file = "carrefour_20250909.csv"
# headers_csv = ['Pdp Url','Brand', 'Product Name', 'Pack Size', 'Price Per Pack', 'Price per Kg or L', 
#                'Promotion', 'Product Description', 'Ingredients', 'Legal Name']
# write_header = not os.path.isfile(csv_file)

# with open(csv_file, mode='a', newline='', encoding='utf-8') as file:  
#     writer = csv.writer(file)
#     if write_header:
#         writer.writerow(headers_csv)

#     for base_url in all_product_urls: 
#         response = requests.get(base_url, cookies=cookies, headers=headers)
#         sel = Selector(text=response.text)

#         try:
#             script = sel.xpath("//script[@type='application/ld+json'][2]/text()").get()
#             data = json.loads(script) if script else {}
#         except json.JSONDecodeError:
#             data = {}
#         pdp_url=data.get('url')
#         brand = data.get('brand', {}).get('name', '')
#         product_name = data.get('name', '')
#         pack_size = data.get('description', '')
#         offer_list = data.get("offers", {}).get("offers", [{}])
#         price_per_pack = offer_list[0].get('price', '') if offer_list else ''

#         price_text = sel.xpath("//p[contains(@class, 'product-title__per-unit-label')]/text()").get() 
#         price_per = re.search(r'\d+(\.\d+)?', price_text)
#         price_per = price_per.group() if price_per else ''

#         promotion = sel.xpath("//p[contains(@class, 'sticker-promo__text')]/text() | //span[@data-testid='promotion-label']/text()").get()
#         product_description = sel.xpath(
#             "//p[contains(text(),'Description')]/ancestor::div[@class='product-content__title']/following-sibling::div//div/text()").get() 
#         ingredients = sel.xpath(
#             "//p[contains(text(),'Ingrédients')]/ancestor::div[@class='product-content__title']/following-sibling::div//div/text()").get() 
#         legal_name = sel.xpath(
#             "//p[contains(text(),'Nom légal')]/ancestor::div[@class='product-content__title']/following-sibling::div//div/text()").get() 

#         row = [pdp_url,brand, product_name, pack_size, price_per_pack, price_per, promotion, 
#                product_description, ingredients, legal_name]

#         writer.writerow(row)

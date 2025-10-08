from curl_cffi import requests
from parsel import Selector

cookies = {
    'BUI': 'f97eb38b-3bba-4d2d-9039-aafcca9e7ba8',
    'XSC': 'wXYN5LWK7In1JXyGPhtDX8Wvpq5PpfkV',
    'shopping_session_id': '26cbaaf55cf700073c54cd735e8b5824d38748f3cc582baf73f9813780045f5f',
    'bltgSessionId': '0143cda3-d77b-40be-aff2-17f59b1bf98d',
    'XSRF-TOKEN': 'adf1344f-a92a-4317-be79-851a72234b5c',
    'sbsd_o': '33BF51F21E4EC539E73DE8E556DEDB65FA43E098D7E5DEBFF278AD29A933CEF0~sd9F2BjSI5JhI+//7o/StGOp6DnrMDkrVTkY8SYjSMhxdRyylBvxubd5IbQqjt+CEMaadBU+rDTn0RZZFIx6lY3tETl1OUfsIG8PzvMVZY6HQKmmc64zFAJkwX+VyVKOc/JQKnikN2VjeU6aRW6KSIR6VbJbUQ609DolXyl8J3cdoDiJZT8b9MCE/BFdbeSOv2vzfoWfYWfwLrBupRSLwNSRyGkG99eJig/Ru4XsyBHE=',
    '_abck': '191291018293DCB288D65841344C904D~-1~YAAQHEPHF+zsDZaZAQAAXnYvww6LB3Bfwsv5IAP3tO+nBKrYtOCmRuMAyauAGr4/aBmOBTQORERuNt0p68+xD+zg8mmFhUCpTlJ3jJd9hYRQsla/uqs2vQDNjj0ir7loaCWF3708l/qvS44+BHsiPNvbr8QWAYVt6uytU4RHStErt980lA/MCIras23+oxS2fPk2vZNX2vs64X3jGY5m0vKlW+PeuSn/twFF91r0WOCn0/0bMK/1IL8otjjhXc6gxP2bbRm+kzcHUOwJvJfyiL8IfMdEw5YJIBKH1ve/BBHLv9aPa2uq0f6+X1MVHy2pQht7gvp/7dosuQyqJ8VSwRFSKdtj3Z4xJ2L7aXiB4tJc1AtfKuScPGXr5Y6nk8cSTtXTDByK3nEOzl631GsNJLvTLNH1pUBkTfhs/B5V8sgtwJvcD22R/ceGSJzJhBbWkVo5MQ==~-1~-1~-1~-1~-1',
    'ak_bmsc': '49CB7C9176CA2DF872BC38E837EE7B4B~000000000000000000000000000000~YAAQHEPHF+3sDZaZAQAAXnYvwx1YebNt1t6xUcuyvJ0zwzi200M2Mg6MAIGwKi8XZMQy5eChwKMv+v+IgIUPCcCtu1pHLrHRUpwTyWpfjUY8+/P/kifC4vGI1HIC7h4RHteFulvgbNAF7hyZNk/8QfXGKF7ZxwGQe0kAX1/re8t4R1KPxddPWs43av0P/uAAcDD91zRcDzUWVQo3+8sGze+/AjShM5AkeHXrsd8VC9/bTXXcz/MF2sVUScG8y2rRtyt7IggNe33jwvSXFr4F2a0SiyOE2pUSj+bGAPmwuhmPh0O/5eB6K+j38wi8+ycr8PQnkpbuuxCgfC/Jbh1G+pkMURjOHbEPwczRvuiNUWzaqb3ukHtdXZGguGysvXbHlw==',
    'bm_sz': '71993C9015CFD64E24ECACF9AC31787E~YAAQHEPHF+7sDZaZAQAAXnYvwx0HSl7UgUtuA7F5g2uSfCU6z6bOPI22dPebo49cEtlpQWjQ6pucnIjunbANdlfD7ubcGP2A7hpvnDoCppNZKNhkVJvDQS/iZ/eBTnFpi8Mzwccf18fri6tk93ssBN0FgwG7jITRe7LyJ42KjHcmfA0gAm+NuM/Gjv2j0gdLKSkhi6xBniFTeBB0Rt+UBlgIP9XgMXzdvcdj0IK4xoVygDpyc0y2PT+cgtAhZdf3JiykaMTVV6zed+sKub19f2FZ+gD6rRlIyY9RqCpqsMgSm80g2iHc3SJd3Hxdq6iyvtsLxhi2Sbme5/d9Z9kbx1OUWEu9FuNifKzCfL817Bu640zSBoxmraHVIV+dUkfYAMTkXk9jy+XdEXBBaA==~3422262~3290421',
    'bm_lso': '33BF51F21E4EC539E73DE8E556DEDB65FA43E098D7E5DEBFF278AD29A933CEF0~sd9F2BjSI5JhI+//7o/StGOp6DnrMDkrVTkY8SYjSMhxdRyylBvxubd5IbQqjt+CEMaadBU+rDTn0RZZFIx6lY3tETl1OUfsIG8PzvMVZY6HQKmmc64zFAJkwX+VyVKOc/JQKnikN2VjeU6aRW6KSIR6VbJbUQ609DolXyl8J3cdoDiJZT8b9MCE/BFdbeSOv2vzfoWfYWfwLrBupRSLwNSRyGkG99eJig/Ru4XsyBHE=^1759916294190',
    'locale': 'NL',
    'language': 'nl-NL',
    'P': '.wspc-deployment-597bf947d6-lqbcb',
    'sbsd': 'sF8rgnIfG/vknkUFAyw4UxRyUvA9zb4dXKgE18aFBza9+sAkIMdV7fx81ow0cRQssilwxuwbkiuBfJ0Fskce/7fRr915xbGz1DMFAl7gpEDlXLFEfuUoWdKQRlboK1JyX2EQrAtjuEhZPfujZQShYIF8Q81eWyeSI5oW96wFicegXgjjKSmExSLp7BMyBFKDv9ZNXt70l6mCWj7m8NGWMmMU8VKvcsAAvl+M0A4A33/oelJZrQSMHzPHJYDrKeC+/WzgfSkI3zlFjX7EvhMUeAUyi3bD1PgK5AWK9mfIf+XRBfNzbLEJ3yUfM1y5oQKAf75msk+dRnOFeOyXnct0fGmBgsE7E/8DBCn45DtI5lRoXfXi7tFJaqg9tlN6+y7Tj9MbrVsEktqEyPUFXL2vHxw==',
    'rl_anonymous_id': 'RS_ENC_v3_Ijc4OTVmYjg0LTRkM2YtNGU4Ni05ZmY0LTFhYTFmZjBmOTQ0NCI%3D',
    'rl_page_init_referrer': 'RS_ENC_v3_Imh0dHBzOi8vd3d3LmJvbC5jb20vbmwvbmwvbC90ZWxlZm9vbmhvdWRlcnMtYXV0by84MTAwLz9ibHRnaD01ZGM2NTBjMy05ZDQxLTRiNjEtOGMxNi03MjdhZTVlNTI2YjAuZy5pLlF1ZXJ5Q29udGV4dEhvb2si',
    'rl_page_init_referring_domain': 'RS_ENC_v3_Ind3dy5ib2wuY29tIg%3D%3D',
    'rl_trait': 'RS_ENC_v3_eyJjbGllbnRJZCI6ImY5N2ViMzhiLTNiYmEtNGQyZC05MDM5LWFhZmNjYTllN2JhOCIsInJlY29nbml0aW9uVHlwZSI6ImFub255bW91cyIsInNob3BDb3VudHJ5IjoibmwiLCJzaG9wTGFuZ3VhZ2UiOiJubCJ9',
    'rl_session': 'RS_ENC_v3_eyJpZCI6MTc1OTkxNjMwMTc3OCwiZXhwaXJlc0F0IjoxNzU5OTE4MTAxODYwLCJ0aW1lb3V0IjoxODAwMDAwLCJhdXRvVHJhY2siOnRydWUsInNlc3Npb25TdGFydCI6ZmFsc2V9',
    '_ga': 'GA1.1.655852812.1759916304',
    '_gcl_au': '1.1.345353315.1759916304',
    '_uetsid': '68692a90a42411f09f1cafaedf3616c4',
    '_uetvid': '68698290a42411f0a2901f682279587c',
    '_fbp': 'fb.1.1759916304130.997467042493434565',
    'bolConsentChoices': 'source#OFC|version#6|int-tran#true|ext-tran#true|int-beh#true|ext-beh#true',
    '_ga_MY1G523SMZ': 'GS2.1.s1759916303$o1$g1$t1759916304$j59$l0$h0',
    'bm_sv': '2855A9E19A7ABE2C22C6DF99D3A97E80~YAAQDUPHF0FsrpeZAQAAGMkvwx1aktJUOJeJR+5sDyT0yZ/OM6vizRbJyBWkiNA9qCQq0x4YJXX4wSGaKGUVCvAGZ9WpaR40e8YLTuKYt6Ry2m8R9t0abPy9KkPkhEkqy4ENL/Vo23UrcGsKs2LwQF6BMYARt7Ly6wVzG+dGfYPb5miF0PkCvlK82kElV44rFb5JZxWsLznWe4FWaox+GAwNmUVvwEcoi+xbgPjkeQTJ6/weDYrDdIO7Bt3GVw==~1',
}


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.bol.com/nl/nl/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'BUI=52e4b411-ad74-4560-aac6-3e21168283a7; XSC=w4r3ynarlSbpoNmIHZ3WITan8uijog3x; locale=NL; rl_anonymous_id=RS_ENC_v3_Ijc1ZGU4MWY5LTM2MWUtNDNjNy1hNzg3LWI5YTNhYzJmY2E5YyI%3D; rl_page_init_referrer=RS_ENC_v3_IiRkaXJlY3Qi; rl_trait=RS_ENC_v3_eyJzaG9wQ291bnRyeSI6Im5sIiwic2hvcExhbmd1YWdlIjoibmwiLCJyZWNvZ25pdGlvblR5cGUiOiJhbm9ueW1vdXMiLCJjbGllbnRJZCI6IjUyZTRiNDExLWFkNzQtNDU2MC1hYWM2LTNlMjExNjgyODNhNyJ9; _fbp=fb.1.1755586286802.311891541524109627; _ga=GA1.1.121214253.1755586287; _gcl_au=1.1.1724885285.1755586288; _abck=A789670AAEEF775A5DC17891126085CC~-1~YAAQDmU+F0YVwpeZAQAAGy8zwg54RbDoPHYhIBx807jpOvNqXTR1SZ5m86IwcT1AgOaNSFr2oSyrZQW1J3/fARGyjqCOKVPuRpZm2iQEFFIOH0KzpnHJwgibPvX7c2xUg5kW5fcw5J4qdbmvdLtznHQ/4LwwzCn1ti+QA7WXtccpE+n1jZmEC+uiXZBN2/STS7eOwD7tqt96BPbBotw94102PQ4sIDigsCA/e3pLatR/lGnp+iny4gJSr2tEH/7UbWhjGLwDvnf89J5gmxISEl1szSCOGKwzsvk4ksMXWfOYihEnfpyLnMX7HGzz2UltCjkn9jzioXduaBnfMgwsnfRC8N4ze7LqBoku1DKY69DRyRBsdPvb8XaMNSApzP1lkQi7t4TCllVe6VH9yqvreOZI6RDgVApSA3Khj6DDuPbGPJPOIMhmRmee4epzh7HyXEH2HXxKWGtRwfCzCIz6XX4hnvX8/cidprpnykboAhClxjdqFCA/DYnZfQ==~-1~-1~-1~-1~-1; ak_bmsc=810985699440CD90BA0A0EAE83AD4C0C~000000000000000000000000000000~YAAQDmU+F0cVwpeZAQAAGy8zwh2uDP9/2Qbl385g52GR1rBCGVz5xrJuBGksSnaFRoVanQE63eZUCZw8VdwXQSJ6pUmZbgu+VyTbin1nZE1iKbRflUM1keuwrFrWaK0rRP8oJKmfOeyxeGmkMAhlYIhUrMixz78/M6J+fuNcbO3h+3wPlXlOIiluXAYPvls1gZq0Iu4MNBx1ROQrGwROE3qcdtNa3pO+7TZzyNlqeZX3fktMW097HqNl3fA+Q+a74XdwMQtq6Yu1gmwN4j5tPKCbE3gD8e+ZmiUEi0vhRDYy+eHNtLbnBTskZ4VWcRIj9BezGRcp3PW6Mn7Mr/AWInMwLkxTL2dUDHNBpOktWxQuqEo1MJu8CVtvpxWGvcu4; shopping_session_id=8d9978ab881be0bec74633f75cd9a63f98a4d7854a8c301b196ee69c45617446; bltgSessionId=1f8e1304-ce48-47c4-90bb-6a2d93bbed88; XSRF-TOKEN=07ba1645-fd37-4781-8135-218b05edfd54; bolConsentChoices=source#OFC|version#6|int-tran#true|ext-tran#true|int-beh#true|ext-beh#true; sbsd_c=4~1~881197967~pl0pJjoaByE8kiBwRyX9xG0xD5TYNy0MWpWLcgx43nm0x3J4Ufmk3R3viZpG/tZ94yXCHTMKox9fs4wu8koC63eVytvMBJQLtXsKFFJenaIzjgws98DgPDKujb60EQp1AzuMqrKhH3heWOTAovMqSZs/vEH5gYWOwihBANdsLx9RjI3WKBVwJr8+sJxlUUHRPSOaEuhfTGr8BzLF0DNsLhaw==; language=nl-NL; __eoi=ID=4b801c569e2797b8:T=1755587444:RT=1759899767:S=AA-AfjaIie8oyK6cGFqCsiVe8ydg; sbsd_o=D5E5B051F32DEA5E4971A8C8BADD59B294F69620D2C0ADBCC027E0B9C25E8948~sj1UHaYAzGkK49Xl2aDO1x5DMwogdxqlxVFFNBl9OBEN5/wgaPvZWXl62pi+uTz2mYzgaAMZIUy8FQAYHG/qK8+lLThebLdvnVFJHdEuXKAfoAYeQc3LdhEGpbNUUUdx6kC6Z2o3/WO8TWknSJ3XfBYC8TBLFrpukXz587LPZVeKsD8Wc/dBRh2e1erG/kunKByOFFIssjFGuTiO85covd4w845l2YD8uHxgx0PUfza8=; sbsd=swPPfPOS6+uDhmTS/bfRJZSQVc/4W1mpZLUoFWfwjGdr8brt/RE/Oxl4RT1nHnPq2PDuy2qsB48xLVL1C2UGuwl2dcfR8N5+UZBLAhSKbqkpzTXNdMTdXr6wCHdLaII4GzhHHGdgorp2j+2ni42kGFqK9nSWI47Uu/QaIouDUvvkramUoodvMinarOVqQAdunTfWNmw+sF6RcxK4Ste8YsTyzUE02g2qjXEINZ8xQEKy2q/lsPq90hziO0OAhmN/YNVVy+uuoCAO0NKqFPf9DN6AJPqkRkgaT2qtG8M60omWMbbRnfz+nYff9xk40C8WmgwAgLXOiuXq4TgICY4VzjyYmQDqPCoI3K38vRJ2sTUh5wwZCg/H0ekdsvC6VXw+f1fFeCRV5gKvaoSdUQqRNoQ==; bm_sz=460E9FDBD97F24A13831AE004000CACA~YAAQHEPHF5ZQ/ZWZAQAAQMY3wh2c5eTXkA3BkvCiafoa9GN6XjsF9Yl71MjwX/938fdOj87Y34MvQnEo3uks2s6UNHra0Ra8JTK8fttddCOBBWB6cuihDLPfZPaGbs+DXkfOxO0OIWlMJL7/a9gvkU8q5guCM9ePQCLWKw5K0iSp5LSc7bcQrIzsQmK7cW3SgiDpv1A1Dhd//mCIMIxbCEQc5UzXb8cpWVq2osvIX4eGIURpmmCukQ4ZoqBv01uwWzSibD3HeQJGc3s6sOjplNybCNoloE0Ni7otMURXbLhAzYIKQnnRSZWsY2auk+3BKiurUDTDA41lV+XXUPYViEKkcMIULOpMzjqJwGUgGWR6Zv8nOv6lQ0gUCueRbL+87K/Mbw/FJzaJJZZ6fZusmlPHXxv68nrDoyzhib+Bs+c33g==~3682615~4539459; _ga_MY1G523SMZ=GS2.1.s1759899771$o4$g1$t1759900064$j60$l0$h0; P=.wspc-deployment-85b574575d-kbg4q; _uetsid=736f6cc0a40411f0a4ff810c87616a13; _uetvid=edaf60b07cc811f0921bfbb30a02cb1c; ga_client_id=121214253.1755586287; ga_session_id=1759899771; rl_session=RS_ENC_v3_eyJhdXRvVHJhY2siOnRydWUsInRpbWVvdXQiOjE4MDAwMDAsImV4cGlyZXNBdCI6MTc1OTkwMTg2NjU5OCwiaWQiOjE3NTk4OTk3NzAyMTgsInNlc3Npb25TdGFydCI6ZmFsc2V9; bm_lso=D5E5B051F32DEA5E4971A8C8BADD59B294F69620D2C0ADBCC027E0B9C25E8948~sj1UHaYAzGkK49Xl2aDO1x5DMwogdxqlxVFFNBl9OBEN5/wgaPvZWXl62pi+uTz2mYzgaAMZIUy8FQAYHG/qK8+lLThebLdvnVFJHdEuXKAfoAYeQc3LdhEGpbNUUUdx6kC6Z2o3/WO8TWknSJ3XfBYC8TBLFrpukXz587LPZVeKsD8Wc/dBRh2e1erG/kunKByOFFIssjFGuTiO85covd4w845l2YD8uHxgx0PUfza8=^1759900066633; bm_sv=23E4483A7BB05FE9CEF2717ADE74C9A6~YAAQHEPHF6ZT/ZWZAQAAeAE4wh3LPg85KYddjlhlOqfj2h10ECOPrB+V7J2jv3Lr4fYK/IYHcDCaK3E/cMCmdv0HiLMYpyMkRqoISAKPohsjUYHwS3LQOrZpCydy5bOs2lg77toSzSddwAaKucjYl/gjCyLnHR4LT1ok/5ZeQuJ3EcrIkS2Z93wcX/0a4Tdf/4pPGJx2CgvbZcw5aaoPvVIZ/NhuiydMD6XYpkz2238wfG+jE+Y5OgXPEd6IGw==~1',
}

####################################CRAWLER#####################################
product=[]
page=1
while len(product)<=30:
    base_url=f"https://www.bol.com/nl/nl/l/draadloze-opladers/04349/?page={page}"
    response = requests.get(base_url, cookies=cookies, headers=headers,impersonate='chrome')
    print(response.status_code)
    # print(base_url)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[@class='w-full']/@href").getall()
    # if not product_urls:
    #     break
   
    for url in product_urls:
        full_url=f'https://www.bol.com{url}'
        product.append(full_url)
        print(full_url)
    page+=1

print(len(product))
#############################PARSER#########################
# for base_url in product:
# base_url="https://www.bol.com/nl/nl/p/autohouder-telefoon-smartphone-telefoon-houder-auto-ventilatie-telefoonhouder-auto/9200000105111982/"
# response=requests.get(base_url,cookies=cookies,headers=headers)
# print(response.status_code)
# sel=Selector(text=response.text)
# product_name=sel.xpath("//span[@class='u-mr--xs']/text()").get()
# brand=sel.xpath("//a[@data-role='BRAND']/text()").get()
# rating=sel.xpath("//div[@class='text-neutral-text-high']/text()").get()
# review=sel.xpath("//div[@data-test='rating-suffix']/text()").get()
# breadcrumb=sel.xpath("//p[@class='breadcrumbs__link-label']/text()").getall()
# selling_price=sel.xpath("//span[@class='promo-price']//text()").getall()
# image_url=sel.xpath("//img[@data-test='product-main-image']/@src").get()
# product_description=sel.xpath("//div[@class='product-description']//text()").getall()
# ean=sel.xpath("//dt[contains(text(),'EAN')]/following-sibling::dd/text()").get()
# mpn=sel.xpath("//dt[contains(text(),'MPN (Manufacturer Part Number)')]/following-sibling::dd/text()").get()
# product_information={}
# rows = sel.xpath("//h3[text()='Productinformatie']/following-sibling::dl/div")
# for row in rows:
#     title = row.xpath("normalize-space(.//dt[@class='specs__title']/text())").get()
#     value = row.xpath("normalize-space(.//dd[@class='specs__value']//text())").get()
# manufacturer_address=sel.xpath("//dt[contains(text(),'Fabrikant Adres')]/following-sibling::dd/text()").get()
# documents=sel.xpath("//h3[text()='Documenten']/following-sibling::div/a/@href").getall()

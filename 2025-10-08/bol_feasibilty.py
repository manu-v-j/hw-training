from curl_cffi import requests
from parsel import Selector

cookies = {
    'BUI': 'fb8ae9d0-3ce5-4583-9fe7-2c004768beb4',
    'XSC': 'wEmBMSjPogCLOYIpl0eky2Kg5p3m6KV8',
    'rl_anonymous_id': 'RS_ENC_v3_ImZkZTZkNGIwLTVkOWEtNDkwNC1hMDYwLTcxNTc1MmI1NTVhZCI%3D',
    'rl_page_init_referrer': 'RS_ENC_v3_IiRkaXJlY3Qi',
    '_fbp': 'fb.1.1759910973018.559396921600489205',
    '_ga': 'GA1.1.392313674.1759910975',
    '_gcl_au': '1.1.537497710.1759910975',
    'rl_trait': 'RS_ENC_v3_eyJzaG9wQ291bnRyeSI6Im5sIiwic2hvcExhbmd1YWdlIjoibmwiLCJyZWNvZ25pdGlvblR5cGUiOiJhbm9ueW1vdXMiLCJjbGllbnRJZCI6ImZiOGFlOWQwLTNjZTUtNDU4My05ZmU3LTJjMDA0NzY4YmViNCJ9',
    'ga_client_id': '392313674.1759910975',
    'ga_session_id': '1759910974',
    'shopping_session_id': '0c329f65badd059e955de30248d3f4d46846585ab914b499725c71efb0a14828',
    'bltgSessionId': '425171cf-47fd-4fee-bc9c-357e76f1a074',
    'XSRF-TOKEN': '90e5e33c-ea23-4f93-9582-b6cc7b24fc79',
    'bolConsentChoices': 'source#OFC|version#6|int-tran#true|ext-tran#true|int-beh#true|ext-beh#true',
    '_abck': 'D913F887F03B81CBC74A347C8173669F~-1~YAAQDEPHFyjAgZeZAQAA/W1nxw5L1PxtqP/8dZM1Yo6BStGK7nOfk6mgi+AHVVWdkEsqW5DFL9GUHKFopSMevDc4qWNzd9nt5LwZvFJoA/TZYcf9jUHc0c26/EIQRUCK7V4/EIB9mNaXV0tqPpqWt9C0q7+BZHBlCb3UjTw/Hes8pWmh+SzFsycwHPTRFe9cISuv+bcr+pi2cu3KwwYLt1Zfwm+ysxdCNxMq7Z0nUXL/BY5RYdjQ47MGnddSabhN3bYW931WCgBZQP7yhfpVY83LXoEOxuYz3YGzyB74H+hZ4eFODfFMMTH7r+WNmsM95Pz1qtc4Xx/8h2tIBAx4DquH5SyqQRx+lEPjblpC1Bh5u6xh0EYCjq+a1roJxk0vpMmaUuUqPzf1nlF4zNiSSh5b7TyzZsmd5YPpNngnHgAqnRFutYGFzCZ1jJnb9c6+CQhhv526xVTTr5QC3h+PajNM487nmun131szc04m/bJf5QZD/5VH7D1bCg==~-1~-1~-1~-1~-1',
    'ak_bmsc': '8D46E2091E1959CCC540820113689202~000000000000000000000000000000~YAAQDEPHFynAgZeZAQAA/W1nxx2U3WJcK0ZETgBAgLXtOEFTikjcIrzmBKW44zZU1iLqZoHvKJK/VPwgwmEtSnfBgoD10lzF2uRF+25O4IP3t1Wiwn06krVpTu3VgOjJdpzg460cyDRJylwW9rn/fD0apUU/I62GZJ+K+P3Wcceev7HxjtJdwgGm/ZubfWodWg/xsyTrot1I2QC15cM48jZjisCucEGGxbey1GgSyu6WQ4LuZdchItzh/p3a6leiUqT9at7Y0JspCzkIxszelytUywvZYBuell5siTIouhgbfjU597KF0hN81U9MnPESAv7hP5yYfCHvzQ22ow7e7b2nt5vr8wiWlZCIlMgmTlaWnMEf51XW3/4PnRQe8Jyrmw==',
    'locale': 'NL',
    'language': 'nl-NL',
    'sbsd_o': '11EB0D1D5C29B595E728C89B362959EF8B9EE65CF69F32E7CB0A5EB1EA0B6913~si3h0MdCEe3X3eueL7tnBmMbB4MCGYdM30Dp/btl1rQBM8OBpamfJVRo5LGjSwfKIDyozrtESgZoMStKzFWSiA9ylvcmoaAbYdqQr8CU3B5tKwzqASfLJXzJeYmXbqGXEPvbX+TPjAkxmadgdZRzmRzb7FAryJ3kaI3MPf/BG5BvWmT4csytcIvS/oOXzS14UY6yb8EaETKSICHY2oUpILcFhVUZ0iqIH1Pgm8YI87tI=',
    'sbsd': 'sW9xwK0t4i/kzsFSaB7X1oqMczmC8Ssjk7mKDwNHpxXAZ4qQNd/fHb/yoDZBR36nHyLMLO8VsTT8S/jb5yJV9Ei94V9GZR6VYRmEdEC5jg0ZjI9gw45h4+hCZ/WzRF8vrWNViHgjWbrDrWfUAIQhNDmTWKfx1GRXQSR3xUn7x2+mv03U0U5YOMFjyKXCN++9B9wWLYCtI9u2ZbHeWOYM9jIioG8c9hcMBh/26cU0XnfGFn6+vntqJIAV1EbB7g63UFIT1M0kcPSUsU8YZnwCMfRlt7Y/2vEhUc4FWGIlUPNrn7aWyzhiD8DpZotdpZZg3js6d4WOQPGFRhW7+Y87s8Wgfnp+9sIo9wfTFwMeS7T2AfzWyfKNsoMn9QvN2DawrTO3WgxJ/dK2eom3H7Bwtoq4xiakEtqRvLMlTs8kkGp8=',
    'bm_sz': '04DD556299C0D0510B002A9B4888C5E1~YAAQTZUjF1bRq8WZAQAAIQp1xx1RO3T6OXef7K+BIGHOQp9yb6brmVBgg9OXUP4DEWhG5CKfBpspkcH5GkmR5rb46RmEV25azyMVtPbggBE2E35CR4OdNYrTUavnI2je5ogQQvvlK8dpN4RvTjBc/EYmVsXpdxZLyceFa3BP7E+cxEa/x1u3Kkv22lTmQQnwOvme2QDoiTXM9VUtgXeicRhLoWW25mkiYLFM/dh/AU/smEq5yjohmB4Of62sxveceiYMe1P49kpLHEN096PAWN3Pmy6jSCPLDaDHuvhRcluNLD9hzUuGdDuhly6k5iHb0HV5f+xJkl+OFIki6ALzAL/86DinSP2g2CBAi3VxEKxpyOhowWVnUSHliYLYskyBtsHmtLCzTGRWeYbToKotBMCmPN5fb0vvqnbHfV1tKUTzF2w=~3163442~4404792',
    'P': '.wspc-deployment-597bf947d6-vnkl5',
    'bm_lso': '11EB0D1D5C29B595E728C89B362959EF8B9EE65CF69F32E7CB0A5EB1EA0B6913~si3h0MdCEe3X3eueL7tnBmMbB4MCGYdM30Dp/btl1rQBM8OBpamfJVRo5LGjSwfKIDyozrtESgZoMStKzFWSiA9ylvcmoaAbYdqQr8CU3B5tKwzqASfLJXzJeYmXbqGXEPvbX+TPjAkxmadgdZRzmRzb7FAryJ3kaI3MPf/BG5BvWmT4csytcIvS/oOXzS14UY6yb8EaETKSICHY2oUpILcFhVUZ0iqIH1Pgm8YI87tI=^1759987963589',
    '_uetsid': '1d9af8c0a41e11f0892ae55a9cdd75a5',
    '_uetvid': '1d9b4200a41e11f0bf4f41d92a42bd94',
    '_ga_MY1G523SMZ': 'GS2.1.s1759987079$o3$g1$t1759987967$j9$l0$h0',
    '__eoi': 'ID=4b801c569e2797b8:T=1755587444:RT=1759987970:S=AA-AfjaIie8oyK6cGFqCsiVe8ydg',
    'rl_session': 'RS_ENC_v3_eyJhdXRvVHJhY2siOnRydWUsInRpbWVvdXQiOjE4MDAwMDAsImV4cGlyZXNBdCI6MTc1OTk4OTc3MzY5MSwiaWQiOjE3NTk5ODcwNzM2NDIsInNlc3Npb25TdGFydCI6ZmFsc2V9',
    'bm_sv': 'D8BCBB41D67F0A415A448C0F66C1DD70~YAAQTZUjF93Tq8WZAQAAA1F1xx0rigUtnLqiUmiYVH23J8te9Jnle2iwWh5J59s8QbigaOJemgA+9h1Iml8dhIqSoDRIdJXRC1Y7EBCHjtv0F+DreyB6deon4zB4uFYQ+uHEGmpmnhyUWDBLwqzAEjnWkaucbRhj1SLEQXIuRN6Bq4XpxPU64ncSD4Zz4hYOGvHMnUO3t9LLrT9Io3zOY9KH5h7INdgDmOjfdPBlvardHdToq1X22mVHSWj9WQ==~1',
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
while len(product)<=300:
    base_url=f"https://www.bol.com/nl/nl/l/draadloze-opladers/04349/?page={page}"
    response = requests.get(base_url, cookies=cookies, headers=headers,impersonate='chrome')
    print(response.status_code)
    print(base_url)
    sel=Selector(text=response.text)
    product_urls=sel.xpath("//a[@class='w-full']/@href").getall()
    # if not product_urls:
    #     break
   
    for url in product_urls:
        full_url=f'https://www.bol.com{url}'
        # product.append(full_url)
        print(full_url)
    page+=1

print(len(product))
#############################PARSER#########################
for base_url in product:
# base_url="https://www.bol.com/nl/nl/p/autohouder-telefoon-smartphone-telefoon-houder-auto-ventilatie-telefoonhouder-auto/9200000105111982/"
    response=requests.get(base_url,cookies=cookies,headers=headers)
    print(response.status_code)
sel=Selector(text=response.text)
product_name=sel.xpath("//span[@class='u-mr--xs']/text()").get()
brand=sel.xpath("//a[@data-role='BRAND']/text()").get()
rating=sel.xpath("//div[@class='text-neutral-text-high']/text()").get()
review=sel.xpath("//div[@data-test='rating-suffix']/text()").get()
breadcrumb=sel.xpath("//p[@class='breadcrumbs__link-label']/text()").getall()
selling_price=sel.xpath("//span[@class='promo-price']//text()").getall()
image_url=sel.xpath("//img[@data-test='product-main-image']/@src").get()
product_description=sel.xpath("//div[@class='product-description']//text()").getall()
ean=sel.xpath("//dt[contains(text(),'EAN')]/following-sibling::dd/text()").get()
mpn=sel.xpath("//dt[contains(text(),'MPN (Manufacturer Part Number)')]/following-sibling::dd/text()").get()
product_information={}
rows = sel.xpath("//h3[text()='Productinformatie']/following-sibling::dl/div")
for row in rows:
    title = row.xpath("normalize-space(.//dt[@class='specs__title']/text())").get()
    value = row.xpath("normalize-space(.//dd[@class='specs__value']//text())").get()
manufacturer_address=sel.xpath("//dt[contains(text(),'Fabrikant Adres')]/following-sibling::dd/text()").get()
documents=sel.xpath("//h3[text()='Documenten']/following-sibling::div/a/@href").getall()

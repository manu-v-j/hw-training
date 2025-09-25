import requests
from parsel import Selector

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'if-none-match': 'W/"ed57f-yVcTdJJJpvH/ZWwcbu63CQCgvLs"',
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
    # 'cookie': 'OptanonAlertBoxClosed=2025-08-20T04:44:26.216Z; usid_AT=cdd7b1d6-897d-4908-8ca8-e6b7be6ab0a6; cc-nx-g_AT=XUiuOKfimjlVB_0Nz8BunTKeoihVDYIpBocNzvgsNuM; dwanonymous_59af42139973e787a0e92cb1ace52202=bcmbBGkXwXwraRkXdFwqYYkXc1; dwsid=dLjvkrDsavpHYICKykjoug68zKuZPxl9gHYbYQg58EBWuBJHvV_o1PXqFNJbKZQoTUCcNBPk3jOmYFf7ZmnQiA==; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Sep+25+2025+16%3A11%3A01+GMT%2B0530+(India+Standard+Time)&version=202508.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5e464e5c-8c5b-475c-a066-d2009c0cf77c&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0007%3A0%2CC0003%3A0%2CC0004%3A0&intType=2&geolocation=%3B&AwaitingReconsent=false',
}

# response = requests.get(
#     'https://www.bipa.at/c/make-up?count=20&sort=Bestseller&refine_0=price%3D(0..300)',
#     headers=headers
# )

# sel=Selector(text=response.text)
# product_urls=sel.xpath("//a[@class='chakra-link css-d89yvx']/@href").getall()
# for url in product_urls:
#     full_url=f"https://www.bipa.at{url}"
#     print(full_url)


base_url="https://www.bipa.at/p/loreal-paris-setting-spray-infaillible-3-second-setting-mist/B3-436474"

response=requests.get(base_url,headers=headers)
sel=Selector(text=response.text)
product_name=sel.xpath("//h1[contains(@class,'chakra-heading')]/text()").get()
brand=sel.xpath("//a[contains(@class,'chakra-link css-14do5ft')]/text()").get()
selling_price=sel.xpath("//p[@data-testid='product-view-price']/text()").get()
product_description=sel.xpath("//ul[@class='css-tu0njr']/li/text()").getall()
instructionforuse=sel.xpath("//p[contains(@class,'css-hd1mf2')]/text()").get()
image_url=sel.xpath("//img[@class='chakra-image css-1jxic4p']/@src").getall()
breadcrumb=sel.xpath("//li[contains(@class,'chakra-breadcrumb__list-item')]/a/text()").getall()
ingredients=sel.xpath("//h3[text()='Inhaltsstoffe']/following-sibling::div/p/text()").get()
labelling=sel.xpath("//span[text()='Kennzeichnung']/following-sibling::text()").get()
storage_instructions=sel.xpath("//span[text()='Aufbewahrungshinweis']/following-sibling::text()").get()
country_of_origin=
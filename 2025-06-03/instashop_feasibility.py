import requests
from parsel import Selector
headers={
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'accept-encoding':'gzip, deflate, br, zstd',
'accept-language':'en-US,en;q=0.9',
'cache-control':'max-age=0',
'priority':'u=0,i',
'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'Linux',
'sec-fetch-dest':'document',
'sec-fetch-mode':'navigate',
'sec-fetch-site':'same-origin',
'sec-fetch-user':'?1',

}
cookies={
  "perseusRolloutSplit": "4",
  "dhhPerseusSessionId": "1748923561420.952001526806550700.nwyoc3kt7qj",
  "dhhPerseusGuestId": "1748923561421.750506234133841500.8ebfyxjcktl",
  "_gcl_au": "1.1.582924188.1748923581",
  "_ga": "GA1.1.1440326402.1748923582",
  "ab.storage.deviceId.bf6e1480-148f-4b67-80ff-27afa4040964": "{\"g\":\"e50a5444-88f0-5215-2940-12898d8b0e58\",\"c\":1748923582057,\"l\":1748923582057}",
  "_scid": "rIQgbeC-7IPj57pienEUEMCZ7Owg5DY8",
  "session_token": "U2FsdGVkX1%2Fkj7kKM0hl%2F%2FsQ5OOaOJS%2FfUf8VOtTxESkumHDqvvGkQtRd7TWgap2YMkziREffCAbwuyHRv9RLQ%3D%3D",
  "anonymous": "true",
  "installation_id": "AFiAfEQkRR",
  "_fbp": "fb.1.1748923583181.802065632851679777",
  "CookieConsent": "{stamp:'CkEGa0u1AsylkG0mnzt/4eMldCibrbU1SpU2yOgD+9PABsCraBfixA==',necessary:true,preferences:true,statistics:true,marketing:true,method:'explicit',ver:1,utc:1748924086826,region:'in'}",
  "_ScCbts": "[\"172;chrome.2:2:5\",\"289;chrome.2:2:5\"]",
  "ab.storage.sessionId.bf6e1480-148f-4b67-80ff-27afa4040964": "{\"g\":\"88c4c87a-8ab1-3559-a060-3b4467422a9b\",\"e\":1748926359201,\"c\":1748923582054,\"l\":1748924559201}",
  "_scid_r": "pwQgbeC-7IPj57pienEUEMCZ7Owg5DY8NWkhUQ",
  "_ga_98CQYB3PP0": "GS2.1.s1748923581$o1$g1$t1748924560$j57$l0$h0",
  "dhhPerseusHitId": "1748924584763.769727610330740200.rgak3f0evzn"
}
# url = 'https://instashop.com/en-ae/client/viva-supermarket-al-bateen'

# response=requests.get(url,headers=headers,cookies=cookies)
# print(response.text)

##############################CRAWLER##############################
# import cloudscraper
# from parsel import Selector

# scraper = cloudscraper.create_scraper() 

# url = 'https://instashop.com/en-ae/client/viva-supermarket-al-bateen'
# response = scraper.get(url)

# with open("data.html","w") as file:
#             file.write(response.text)



from curl_cffi import requests
from parsel import Selector
headers={
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'en-US,en;q=0.9',
    'connection':'keep-alive',
    'content-type':'application/json; charset=UTF-8',
    'host':'api.livenation.com',
    'origin':'https://www.livenation.com',
    'referer':'https://www.livenation.com/',
    'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile':'?1',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
    'x-amz-user-agent':'aws-amplify/6.13.1 api/1 framework/2',
    'x-api-key':'da2-jmvb5y2gjfcrrep3wzeumqwgaq'
}
# ##############################CRAWLER##############################

payload={
  "query": "query PROMOTION_EVENTS($artist_id: String, $dedup: Boolean, $end_date_time: String, $include_genres: String, $market_id: Int, $offset: Int!, $promotion_id: String!, $start_date_time: String, $venue_id: String) {\n  getEvents(\n    filter: {artist_id: $artist_id, dedup: $dedup, end_date_time: $end_date_time, exclude_status_codes: [\"cancelled\", \"postponed\"], image_identifier: \"ARTIST_PAGE_3_2\", include_genres: $include_genres, market_id: $market_id, promotion_id: $promotion_id, start_date_time: $start_date_time, venue_id: $venue_id}\n    limit: 36\n    offset: $offset\n    order: \"ascending\"\n    sort_by: \"start_date\"\n  ) {\n    artists {\n      discovery_id\n      genre\n      name\n      slug\n      tm_id\n    }\n    discovery_id\n    event_date\n    event_date_timestamp_utc\n    event_end_date\n    event_end_date_timestamp_utc\n    event_end_time\n    event_status_code\n    event_time\n    event_timezone\n    genre\n    images {\n      fallback\n      image_url\n    }\n    links {\n      link\n      platform\n    }\n    name\n    presales {\n      end_date_time\n      is_ln_promoted\n      name\n      start_date_time\n    }\n    sales_end_date_time\n    sales_start_date_time\n    similar_event_count\n    slug\n    source\n    tm_id\n    type\n    url\n    venue {\n      discovery_id\n      is_livenation_owned\n      location {\n        address\n        city\n        country\n        state\n      }\n      market_ids\n      name\n      slug\n      tm_id\n      venue_type\n    }\n  }\n}\n",
  "variables": {
    "market_id": 51,
    "promotion_id": "tickettosummer",
    "offset": 0
  }
}
total=[]
url="https://api.livenation.com/graphql"

response=requests.post(url,headers=headers,json=payload)
data=response.json()
event_list=data.get("data","").get("getEvents",[])
for event in event_list:
    url=event.get("url","")
    event_name=event.get("name","")
    event_date=event.get("event_date","")
    event_time=event.get("event_time","")
    venue_address=event.get("venue",{}).get("location",{})
       
    total.append(url)


###############################PARSER##############################
headers={
    'c-tmpt':'0:32d0282981000000:1750840747:90b9cea3:f5986c6c5533969ddea657c52fbc6061:22993c5a2ca0791ba66293fd00dada6836a457fc5ed6a3e012892567006ee45c',
    'referer':'https://www.ticketmaster.com/',
    'tmps-correlation-id':'8bc80e75-c0a0-4bdb-85da-f2ad6ae05412',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36'
}
url = "https://services.ticketmaster.com/api/ismds/event/1C00629C7364144B/facets"


params = {
    "by": "section seating attributes available accessibility offer placeGroups inventoryType offerType description",
    "show": "places",
    "embed": "description",
    "q": "available",
    "compress": "places",
    "resaleChannelId": "internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us",
    "apikey": "b462oi7fic6pehcdkzony5bxhe",
    "apisecret": "pquzpfrfz7zd2ylvtz3w5dtyse"
}
response=requests.get(url,headers=headers,params=params)
data=response.json()
available=[]
facet_list=data.get("facets",[])
for item in facet_list:
    count=item.get('count','')
    available.append(count)

filled_seats=[]
url="https://pubapi.ticketmaster.com/sdk/static/manifest/v1/1C00629C7364144B"
response=requests.get(url,headers=headers)
data=response.json()
section_list=data.get("manifestSections",[])
for item in section_list:
    seats=item.get("numSeats","")
    filled_seats.append(seats)
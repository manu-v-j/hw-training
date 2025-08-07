from curl_cffi import requests
import random
import json
from settings import MONGO_URL,MONGO_DB,COLLECTION,COLLECTION_DETAILS
from pymongo import MongoClient
client=MongoClient(MONGO_URL)
db=client[MONGO_DB]
collection=db[COLLECTION]
collection_details=db[COLLECTION_DETAILS]
# proxies = {
#     "http": "http://62.255.223.195:8080",
#     "https": "http://62.255.223.195:8080",
# }
cookies = {
    'JSESSIONID': '0000ME2-jHyUUrzPcKOv3ilxH0w:1h17gkrm5',
    'AWSALBCORS': 'rZuDcNesVVRWHCP4sN1/G6YnhdUXpBV2hI9Db1SEF9oVNaqUwoBPqd0cVsx3U/SQQ0INvu3dtVZt3onx3dkd3XyvjvV9RIyBupiVfKK0mzMhIud18aBv6HdIGFMr',
    'AWSALB': 'rZuDcNesVVRWHCP4sN1/G6YnhdUXpBV2hI9Db1SEF9oVNaqUwoBPqd0cVsx3U/SQQ0INvu3dtVZt3onx3dkd3XyvjvV9RIyBupiVfKK0mzMhIud18aBv6HdIGFMr',
    'akaas_gol_global': '1762344265~rv=38~id=29ee9622285b2d8061e297354c501309',
    '_abck': 'CE5ED87AC3AE4B71A0D80835EB612C25~0~YAAQGYR7XCtCImGYAQAA2g9rhA5qgHz9iaGqT5Ujw725XDMmfZ1DtUl96jwZmXF17L9BykMMcK6EeZr5qfeOZXqQ//wqj8/UOSmO597JUai2MpBloiiaq5gCmGUZ+6FAGZ1BQrWyM1qcWZWRZOEs7C9Llfxjo7DJHcbk63NLSTyPSEbwKcC14i9aco8bsig+Bz70jprTFDR2L5NArhlPYL47QMdjGExlFJUKmO1kp18iLqwgD1SZYc7G5a6qIj3/ipBrWQ/ujfh3WZ+/u+8R8Y4+j6W77+9ReO8KhxdDwURYxN6QnyzfgX1yuHPwtD1LSr+IZKZRnM2E7q07+vKrjFaAtcFdMj/y6g1mwxPzN/DDtnPRqwwI/W5Fb2CVTo+zbWXgNBZScP2tzHkhqectAn+dVlclMBz8Mr+XrAMarCjmY5LQ+OC/Ayr9Q8pw3lH/KF4WGehSl6JSDOL3A/lusbrh0PhMjYt5me+S1zXsIyDybCpwYObT2wSv4VVWhSTRSKtdWCEN2P+3C4C5yajCI5FosGUG0yGzF5zB1nYiBfZ/TXA6johleM3cem5AfBKUWfUKaF82vOoBeQq/jomtmvKU2ltzWUuryNxhH8a0A+/d5PCUOCR9rdNVVBv0pA7zvvkMeubEZX0gXaMtg0KtNpsnKtibp+90AaJkwDRY8/fYkqlARMhdygs9701Elp5/jB9kKFZ6JS/+lAF/HD9tgg2tv+s18FpTjNNlVQ0HfA5dnFgsvEXl/4ZMC3QzIA5DQSQsgQd4kIGUrA5uRZWRZPTM8iFUQ4Zo9evTvzJbMvYgMxfy8xElTVEy2Jy+H5ZuDLLSRY4xyDCioNqZJ0SfjlYIYwG801DS0qqCIYn5EZcSOpigfa1p8VzKcJOtWIH7ovweISNeQCJWsa2+Ny9OcVQ2DWc4bHr2/XdrL4U6tTmQUTfZP27wRz9CkoAHt3YTgPp+L3hQdHKOXIfExN1+RXkHqZSY5U7LHvEbtypaVnvu5MWEfDUr4T6G3akDdJsWWOkmJCyMr0pE7HSQ6ybyzW5T6spOTb9Pke5En0Q=~-1~-1~-1',
    'bm_sv': '60511916F389F3D0A2779BA74920AAFE~YAAQGYR7XC9CImGYAQAA2w9rhBx1t4IqZF7Ig06Ov4iA3SQfb07OI7cWfuxM9/t2UIaxnW97PDYhl5V8mxJBENYFY4mwt6CkBRuyB8zqdPVC9bSixENxEvTIPpPx+680NvvUxt+Src6NQczGAUWrrEIg/mycEgTGSUbaE6vXzeNxLe0i5t7Qkucis8bb6iIhWwtADnnuIxBZwwdJXYrwPu/PAWkh67Lz7fuu8dStXZxdvBzReIF9+xcLGNriyvTCBiaKc0Vn~1',
    'akaas_gol_random': '34',
    'akavpau_vpc_gol_default': '1754568641~id=78b2c23f1f5dce0d2aca1b72a45f8690',
    'ak_bmsc': '972CD538263C76EB005DEC2AA47BED7D~000000000000000000000000000000~YAAQCoR7XB4XhFyYAQAA6ThshBxeD13qetm9mTCqbZYvKTTC0gXbuP3YPjEkW7NZLEWTecqFfQFPtuOiDI5pdHwuHdJw+7ZTun7lt3FSQcxWV3+ZedYiJ12n58je/oTLvsGPK+aA8m5FBuWTUjgi8Co98PwZ18GkW77QI4OvA88Lbp9Eqin5RUusKWG+cRvRt5wE5zluEMGBFwReSVx4D9O10jgiNMhY/GqScL3zzKbAhXcbHqIojOT9CnuG/xSpPdT83KkVlNzrk+Y0vKYNKQpPPoBUF/bvE13rZIPxiJU8ZQ4ZjBe9fYYOb8N8YKvonURy4CFnFfLe+BPkJKDfzECoQ0X8KxoOm67Bm+Mdbtv6MivMu9RgVwZiLzuFZQYMeRWGSknvosmo1UOsaxsz',
    'bm_sz': 'EB1EFAF72782077EF1AEB27993779665~YAAQCoR7XB8XhFyYAQAA6ThshBxwtD7kmUZ5SLKt4NhFdZ87XdEVzmiN1NvGPilwfujbqbpEFe+bC1S54eezX9pBGWJM7kRD+ScHl1Lkllj/PByEdaLN1EyrhXCRlmmfXz7XOR9r5YPFtuLvrDSiy9U3WbM42HP2Q8rcmK3O03Ytbxgxe7AjRtbTFUoyrEqGCNKfzg2TRlX3LlDZvM/PCdY+j8pKL/nRBfDh07CJZHRb0o1SMTo0+6ac5+tmizWwG2Ub2nZCDm2QNiAhuimtsMJQB1GzH/VxNOGrfMUTljGjW7FNawvmgxDhj/Bqv/NQWJP+FHSbuI7mhdhzENWboC2XWth+ISu8KGMfQJykebB/4bmcsqoevxVnb74OZWSdYssu3NZRFBiZAQvkJJ8o7AvG5ajMSPDcGpuqRjELjQ==~3293491~3293762',
    'utag_main': 'v_id:01987efa2d0b00506ef793cc16a805065001d05d00bd0$_sn:9$_ss:0$_st:1754570142381$dc_visit:5$ses_id:1754568260761%3Bexp-session$_pn:2%3Bexp-session$previousPageName:web%3Agroceries%3Abrowse%3Afruit%20and%20vegetables%3Aflowers%20and%20plants%3Bexp-session$previousPageType:shelf%3Bexp-session$previousSiteSection:browse%3Bexp-session$previousPagePath:%2Fgol-ui%2Fgroceries%2Ffruit-and-vegetables%2Fflowers-and-plants%2Fc%3A1020005%3Bexp-session',
    'RT': '"z=1&dm=www.sainsburys.co.uk&si=8b55f566-c225-4027-9ddb-f22198a68699&ss=me1cn06a&sl=1&tt=2hh&bcn=%2F%2F0217991a.akstat.io%2F&ld=1ver"',
    'OptanonAlertBoxClosed': '2025-08-07T12:05:45.559Z',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Aug+07+2025+17%3A35%3A45+GMT%2B0530+(India+Standard+Time)&version=202501.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=283272da-bd95-4009-b92b-e71fcf60da12&interactionCount=5&isAnonUser=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A0%2C3%3A0%2C4%3A0&intType=2&geolocation=IN%3BKL&AwaitingReconsent=false',
    'last_button_track': 'false',
}

USER_AGENTS = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
]
impersonate_list = [
    'chrome',              
    'chrome99',
    'chrome100',
    'chrome101',
    'chrome104',
    'chrome105',
    'chrome106',
    'chrome107',
    'chrome108',
    'chrome109',
    'chrome110',
    'chrome99_android',
]
impersonate=random.choice(impersonate_list)
print(impersonate)
user_agent = random.choice(USER_AGENTS)

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'enabled-feature-flags': 'add_to_favourites,use_food_basket_service,use_food_basket_service_v3,ads_conditionals,findability_v5,show_static_cnc_messaging,fetch_future_slot_weeks,click_and_collect_promo_banner,cookie_law_link,citrus_banners,citrus_favourites_trio_banners,offers_trio_banners_single_call,special_logo,custom_product_messaging,promotional_link,promotional_link2,findability_search,findability_autosuggest,findability_orchestrator,fto_header_flag,recurring_slot_skip_opt_out,first_favourite_oauth_entry_point,seasonal_favourites,cnc_start_amend_order_modal,slot_confirmation_board,favourites_product_cta_alt,get_favourites_from_v2,krang_alternatives,offers_config,alternatives_modal,relevancy_rank,changes_to_trolley,nectar_destination_page,meal_deal_live,browse_pills_nav_type,zone_featured,use_cached_findability_results,event_zone_list,cms_carousel_zone_list,show_ynp_change_slot_banner,recipe_scrapbooks_enabled,event_carousel_skus,split_savings,trolley_nectar_card,favourites_magnolia,homepage,taggstar,meal_deal_cms_template_ids,pdp_accordions,pdp_meta_desc_template,grouped_meal_deals,hide_desc_mobile,pci_phase_2,enable_favourites_priority,meal_deal_builder_nectar_widget,new_favourites_filter,occasions_navigation,rokt,sales_window,resting_search,brands_background,brands_background_config,taggstar_config,all_ad_components_enabled,byg_ab_test_products_display_2,new_global_header,new_filter_pages,recipe_reviews_enabled,sponsored_drawer,frequently_bought_together,product_tile_experiment,pci_phase_3,show_ynp_opt_in_ui_elements,fetch_ynp_opt_ins,resting_search_v2,bop_enabled,favourites_boards,mobile_nav_2,should_not_scroll_into_view_fbt,show_popular_categories,lp_ab_test_display,lp_interstitial_grid_config,track_remove_scroll_experiment,track_group_by_top_category,track_boards_experiment,ynpoptin_national_launch,booking_confirmation_content_and_button,call_bcs,catchweight_dropdown,citrus_preview_new,citrus_search_trio_banners,citrus_xsell,compare_seasonal_favourites,constant_commerce_v2,ctt_ynp_products,desktop_interstitial_variant,disable_product_cache_validation,event_dates,favourites_pill_nav,favourites_whole_service,fbt_on_search,fbt_on_search_tracking,first_favourites_static,foodmaestro_modal,golui_payment_cards,hfss_restricted,interstitial_variant,kg_price_label,krang_recommendations,meal_planner,meganav,mobile_interstitial_variant,multi_styling,my_nectar_migration,nectar_card_associated,nectar_prices,new_favourites_service,new_filters,new_page_header,ni_brexit_banner,occasions,optimised_product_tile,promo_lister_page,recipes_ingredients_modal,review_syndication,sale_january,show_hd_xmas_slots_banner,similar_products,slot_v2,xmas_dummy_skus,ynp_np_zonalpage,your_nectar_prices',
    'origin': 'https://www.sainsburys.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://www.sainsburys.co.uk/gol-ui/groceries',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-ba911c9ae54ed6c07446b562209ba550-431b2dddfeb165c0-01',
    'tracestate': '2092320@nr=0-1-1782819-181742266-431b2dddfeb165c0----1754566174966',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'wcauthtoken': '',
}
print(user_agent)
session = requests.Session()
# session.http_version = 2
response = session.get(
    'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]=&filter[category]=188701&browse=true&hfss_restricted=false&categoryId=188701&page_number=1&sort_order=FAVOURITES_FIRST&favouritesPriority=true&include[PRODUCT_AD]=citrus&citrus_placement=category-only&salesWindow=1',
    cookies=cookies,
    headers=headers,impersonate='chrome110',
)
print(response.status_code)

# data=response.json()
# product_list=data.get('products',[])
# for product in product_list:
#     full_url=product.get('full_url',{})
#     # collection.insert_one({'link':full_url})
#     print(full_url)

# ###############################PARSER##################################
# for item in db[COLLECTION].find().limit(10):
#     url=item.get('link')
#     parts = url.split('/')
#     name=parts[-1]
    
#     url = f"https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[product_seo_url]=gb%2Fgroceries%2F{name}&include[ASSOCIATIONS]=true&include[PRODUCT_AD]=citrus"


#     response = session.get(url,headers=headers,cookies=cookies,impersonate='chrome')
#     data=response.json()
#     product_details=data.get('products',[])
#     for item in product_details:
#         product_name=item.get('name','')
#         selling_price=item.get('unit_price',{}).get('price','')
#         product_description=item.get('description',[])
#         review=item.get('reviews',{}).get('total','')
#         rating=item.get('reviews',{}).get('average_rating','')
#         image_url=item.get('assets',{}).get('plp_image','')
#         currency='GBP'
#         breadcrumb_list=item.get('breadcrumbs',[])
#         for data in breadcrumb_list:
#             breadcrumb=data.get('label','')
#         print(name)


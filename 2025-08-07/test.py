# import requests

# headers = {
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'content-type': 'application/json+protobuf',
#     'origin': 'https://shop.rewe.de',
#     'priority': 'u=1, i',
#     'referer': 'https://shop.rewe.de/',
#     'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'cross-site',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
#     'x-browser-channel': 'stable',
#     'x-browser-copyright': 'Copyright 2025 Google LLC. All rights reserved.',
#     'x-browser-validation': 'onHIqyUSYwlqe77GwAvZSAO7PjU=',
#     'x-browser-year': '2025',
#     'x-goog-api-key': 'AIzaSyATBXajvzQLTDHEQbcpq0Ihe0vWDHmO520',
# }

# data = '[[["rewe.de","Anmelden","PLZ 80331","Märkte &amp; Angebote","Lieferservice","ändern","Rezepte &amp; Ernährung","<a i=0>Liefertermin </a><a i=1>wählen</a>"," Favoriten\\n                                ","0,00 €","Sortiment","Deine Produkte","Angebote","Mengenrabatt","Tiefpreis","Bio","Regional","Neu","Shop Startseite","Fleisch &amp; Fisch","Fleisch","Fleischalternativen","Wurst &amp; Aufschnitt","Fisch &amp; Meeresfrüchte","<a i=0>653</a><a i=1> Produkte</a>","Alle Filter","REWE Bonus","2","9","125","76","Vegan","122","1","REWE Regional Hähnchen Innenbrustfilet 350g","W","350g (1 kg = 14,26 €)","4,99 €","Gesponsert","The Vegetarian Butcher Vegane Beflügel-Nuggets 180g","180g (1 kg = 17,72 €)","3,19 €","Regionale Fleisch- &amp; Wurstwaren","Entdecke Fleisch &amp; Wurst aus deiner Region","Toni M No Tuna Salad Brotaufstrich vegan 125g","125g (1 kg = 23,92 €)","2,99 €","REWE Bio Hähnchenbrustfilet 70g","70g (1 kg = 39,86 €)","Ab 3 Stück 5% sparen","2,79 €","The Vegetarian Butcher Veganes Hick-Hack-Hurra 180g","The Vegetarian Butcher Wie&#39;n Schnitzel vegan 180g","Toni M No Tuna Pflanzlicher Thunfisch vegan 125g","REWE Bio Rinderhackfleisch 400g","400g (1 kg = 22,48 €)","8,99 €","The Vegetarian Butcher Chick-Eria Filets vegan 180g","180g (1 kg = 16,61 €)","<a i=0>bis </a><a i=1>10.08.2025</a>","REWE Bio + vegan Tofu Natur 2x200g","2x200g (1 kg = 5,48 €)","2,19 €","REWE Beste Wahl Delikatess-Metzgerschinken 150g","150g (1 kg = 19,93 €)","REWE Bio Wiener Würstchen 200g","200g (1 kg = 16,45 €)","3,29 €","REWE Regional Hähnchen Geschnetzeltes 400g","400g (1 kg = 14,98 €)","5,99 €","REWE Regional Rinderhackfleisch 500g","500g (1 kg = 15,96 €)","7,98 €","REWE Bio Bacon-Würfel Schwein 80g","80g (1 kg = 19,88 €)","1,59 €","REWE Feine Welt Salami Ciatore 80g","80g (1 kg = 41,13 €)","REWE Regional Hähnchenbrustfilet 550g","550g (1 kg = 14,53 €)","7,99 €","Herta Finesse Hähnchenbrust ofengebacken 100g","100g (1 kg = 25,90 €)","2,59 €","REWE Bio Kochschinken 100g","100g (1 kg = 28,90 €)","2,89 €","Deutsche See Lachsfilet 250g","250g (1 kg = 25,96 €)","6,49 €","REWE Bio + vegan Räucher-Tofu 2x175g","2x175g (1 kg = 6,26 €)","Wiesenhof Geflügel-Mortadella 100g","100g (1 kg = 14,90 €)","1,49 €","REWE Bio Geflügel Wiener 200g","200g (1 kg = 19,95 €)","3,99 €","REWE Bio Bacon 100g","100g (1 kg = 19,90 €)","1,99 €","Herta Finesse Schinken hauchzart und feinwürzig 100g","REWE Bio Hähnchenbrustfilet ca. 320g","1 Stück ca. 320 g (1 kg = 34,90 €)","11,17 €","Einfach Bio Rinder-Hackfleisch 400g","400g (1 kg = 15,73 €)","6,29 €","Ponnath Prosciutto Cotto 150g","REWE Bio Salami 70g","70g (1 kg = 25 €)","1,75 €","REWE Bio Original Nürnberger Rostbratwürstchen 8 Stück 160g","160g (1 kg = 21,81 €)","3,49 €","REWE Bio Wurst Paprika Lyoner 100g","Zimmermann Münchner Weißwürste 5x60g","5x60g (1 kg = 11,30 €)","3,39 €","Wilhelm Brandenburg Wiener Würstchen 150g","150g (1 kg = 13,27 €)","Herta Finesse Putenbrust im Ofen gegrillt 100g","REWE Feine Welt Prosciutto Cotto 100g","100g (1 kg = 44,90 €)","4,49 €","Reinert Schinken Nuggetz 3x50g","REWE Regional Rinderhackfleisch 250g","250g (1 kg = 15,96 €)","Aoste Stickado Salami Sticks Classique 70g","70g (1 kg = 35,57 €)","2,49 €","<a i=0>Rügenwalder Mühle Veganer Schinken Spicker mit Grillgemüse 80g</a><a i=1>...</a>","Rügenwalder Mühle Veganer Schinken Spicker mit Grillgemüse 80g"],"de","en"],"te_lib"]'.encode()

# response = requests.post('https://translate-pa.googleapis.com/v1/translateHtml', headers=headers, data=data)
# print(response.text)

from curl_cffi import requests
import random
# proxies = {
#     "http": "http://45.38.107.97:6014",
#     "https": "http://45.38.107.97:6014"
# }
USER_AGENTS = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
]
user_agent=user_agent = random.choice(USER_AGENTS)
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'priority': 'u=1, i',
    'referer': 'https://www.sainsburys.co.uk/gol-ui/groceries/fruit-and-vegetables/flowers-and-plants/c:1020005',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-5955eda0d39ad8c632071f4d2f4a8cc0-3432dedc853019f1-01',
    'tracestate': '2092320@nr=0-1-1782819-181742266-3432dedc853019f1----1754538896900',
    'user-agent': user_agent,
    'wcauthtoken': '',
}
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

session = requests.Session()
homepage_url = "https://www.sainsburys.co.uk"

response = session.get(
    homepage_url,
    impersonate=impersonate,
)

url = 'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]=&filter[category]=188701&browse=true&hfss_restricted=false&categoryId=188701&page_number=1&sort_order=FAVOURITES_FIRST&favouritesPriority=true&include[PRODUCT_AD]=citrus&citrus_placement=category-only&salesWindow=1'

response = session.get(
    url,
    headers=headers,
    cookies=session.cookies.get_dict(),
    impersonate='chrome'
)
print(response.status_code)



# json_data = {
#     'template_id': 'homepage',
# }

# response = session.post(
#     'https://www.sainsburys.co.uk/groceries-api/gol-services/content/v2/withMagnoliaTemplate/ads',
#     cookies=session.cookies.get_dict(),
#     headers=headers,
#     json=json_data,
# )

# print(response.text)

# from curl_cffi import requests
# import random


# USER_AGENTS = [
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
# ]
# user_agent = random.choice(USER_AGENTS)
# session = requests.Session()

# session.headers.update( {
#     'accept': 'application/json',
#     'accept-language': 'en-US,en;q=0.9',
#     'content-type': 'application/json',
#     'enabled-feature-flags': 'add_to_favourites,use_food_basket_service,use_food_basket_service_v3,ads_conditionals,findability_v5,show_static_cnc_messaging,fetch_future_slot_weeks,click_and_collect_promo_banner,cookie_law_link,citrus_banners,citrus_favourites_trio_banners,offers_trio_banners_single_call,special_logo,custom_product_messaging,promotional_link,promotional_link2,findability_search,findability_autosuggest,fto_header_flag,recurring_slot_skip_opt_out,seasonal_favourites,cnc_start_amend_order_modal,slot_confirmation_board,favourites_product_cta_alt,get_favourites_from_v2,krang_alternatives,offers_config,alternatives_modal,relevancy_rank,changes_to_trolley,nectar_destination_page,meal_deal_live,browse_pills_nav_type,zone_featured,use_cached_findability_results,event_zone_list,cms_carousel_zone_list,show_ynp_change_slot_banner,recipe_scrapbooks_enabled,event_carousel_skus,split_savings,trolley_nectar_card,favourites_magnolia,homepage,taggstar,meal_deal_cms_template_ids,pdp_accordions,pdp_meta_desc_template,grouped_meal_deals,hide_desc_mobile,pci_phase_2,enable_favourites_priority,meal_deal_builder_nectar_widget,new_favourites_filter,occasions_navigation,rokt,sales_window,resting_search,brands_background,brands_background_config,taggstar_config,all_ad_components_enabled,byg_ab_test_products_display_2,new_global_header,new_filter_pages,recipe_reviews_enabled,sponsored_drawer,frequently_bought_together,product_tile_experiment,pci_phase_3,show_ynp_opt_in_ui_elements,fetch_ynp_opt_ins,resting_search_v2,bop_enabled,favourites_boards,mobile_nav_2,should_not_scroll_into_view_fbt,show_popular_categories,lp_ab_test_display,lp_interstitial_grid_config,track_remove_scroll_experiment,favourites_grouped_by_top_category,track_group_by_top_category,track_boards_experiment,ynpoptin_national_launch,booking_confirmation_content_and_button,call_bcs,catchweight_dropdown,citrus_preview_new,citrus_search_trio_banners,citrus_xsell,compare_seasonal_favourites,constant_commerce_v2,ctt_ynp_products,desktop_interstitial_variant,disable_product_cache_validation,event_dates,favourites_pill_nav,favourites_whole_service,fbt_on_search,fbt_on_search_tracking,first_favourites_static,foodmaestro_modal,golui_payment_cards,hfss_restricted,interstitial_variant,kg_price_label,krang_recommendations,meal_planner,meganav,mobile_interstitial_variant,multi_styling,my_nectar_migration,nectar_card_associated,nectar_prices,new_favourites_service,new_filters,new_page_header,ni_brexit_banner,occasions,optimised_product_tile,promo_lister_page,recipes_ingredients_modal,review_syndication,sale_january,show_hd_xmas_slots_banner,similar_products,slot_v2,sponsored_featured_tiles,xmas_dummy_skus,ynp_np_zonalpage,your_nectar_prices',
#     'priority': 'u=1, i',
#     'referer': 'https://www.sainsburys.co.uk/gol-ui/groceries/fruit-and-vegetables/flowers-and-plants/c:1020005',
#     'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'traceparent': '00-f456ca76376466c60c33d96fdfbcf020-a7446ac61edb2641-01',
#     'tracestate': '2092320@nr=0-1-1782819-181742266-a7446ac61edb2641----1754585623464',
#     'user-agent': user_agent,
#     'wcauthtoken': '',
# })
# session.get("https://www.sainsburys.co.uk")

# response = session.get(
#     'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]=&filter[category]=188701&browse=true&hfss_restricted=false&categoryId=188701&sort_order=FAVOURITES_FIRST&favouritesPriority=true&include[PRODUCT_AD]=citrus&citrus_placement=category-only&salesWindow=1',
#     impersonate='chrome' 
# )
# print(response.status_code)

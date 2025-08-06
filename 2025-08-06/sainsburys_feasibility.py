from curl_cffi import requests
import random
import json
cookies = {
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Aug+06+2025+17%3A46%3A30+GMT%2B0530+(India+Standard+Time)&version=202501.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1bf98b35-46ed-4314-94d6-4fbff1412aa7&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&intType=1&geolocation=NL%3BNH&AwaitingReconsent=false',
    'JSESSIONID': '0000sahznO9v3nEYJCVm-ov0XD-:1h0f7p25f',
    'AWSALBCORS': 'uzM3rgWKUzR9ldAL3AZPi9LmhWYeWDIFQ4w5nCL0Sm08M/jE3eBjfsCpyPxTnbR/rD2mrZPeVxG1cBvzmYp6A4T2OPRHqwmNADTe3ff5yurjWvThAtQUXVN6Xo72',
    'AWSALB': 'uzM3rgWKUzR9ldAL3AZPi9LmhWYeWDIFQ4w5nCL0Sm08M/jE3eBjfsCpyPxTnbR/rD2mrZPeVxG1cBvzmYp6A4T2OPRHqwmNADTe3ff5yurjWvThAtQUXVN6Xo72',
    '_abck': 'A750A3EE6CA6B3446707CA5F2DDBB9BC~0~YAAQXYgsMUUZ9WGYAQAAktBPfw5FS/9yDmNo2Kgtq42CTpr45jJXFj1cpPXGm2qD8xcHZNOg1+xlhInhluJ91Q3Mw2sBqqRGv/GT2Hmst8ZVIqKWHMP+XuXFtpjcsM0EYG/MHEu21y+y/1EakfCDFS9qp+WJEhOTjQkBBPjA5pE9Q+gExWWNdsua223C84k/CrgLdu7NbCl5QsGmr6j/ZBV9KkA42POxa6fKuqmPnrolL0pmUWuUAPxIg/wxLXGurWn5P1M+Bt520rzdPdG2r36AXEep6qGG7Y2EJozSHOxX2fo5Sv0L2vAQwjj0IuWf1n0jBZm3vG/1x13GDC8v3LBVgRTAlyjxUfuwzKJFE7YJGwofmmTAm7/NdkgTxM9pEF4Y90AqH/YS6l+E224mOrWM+9TtupgKuR55h560O8E1v5jeulSLYBOIbB0SKGG1CdCs/fO6bL1qRoyf2S/uQElHNDigSC3Tk1C9rCXArevehSPL6sQrw2cQjuDkY8vVa5kJNcqX3i/tUl9MJXgyG2blI6uPv0nx2KIHHXPX8nNfMZmYRo8E2XNcRlhlPDfjx6+mzYn9bJSyDC6atTis64nk9La26dFNRGHlLBlPB6AkHMA88jmm/VF0iGrY00hUVskmegP1dM5nQ373Shj/vKIScvp018Q7qkqBWYvnnTh0j7HmMOk+EWk/1JDcG3a/i8upJOMxXItMs/OAyDEXd+jVoGqVQUuvCUSzCiepXejrIBciL0fCAj3NRBxkIkyIYXa620aWRtMc4zqlAoDjB3p2FqMoeIvB6LrjOrAhm59LCgVS8BYyiITgZbpaM4vl4nednFR9jK+WF7po5zXFae44YcEDXDtItaATqFdnQ03FHtrIHfypOgwgCnVI3m9wOj8EzsA0fQg+391mNlft5+RcvFRRDAtYBvou8XVHZAgdjQVqOIHk898SuLY3zSmf3e5WmA==~-1~-1~-1',
    'bm_sz': '49800B3137F5EE71A1A944AD68404AB4~YAAQXYgsMUcZ9WGYAQAAktBPfxyGkFdLZAxfJ6vi5PaMTLA5uM7hbIENn9tYeMwAsQ3zkKSxqs4fuVYOrO/qf8V7PImhWpSUYcAAee4U6BgjM0Ex1i+mkFH7M4PdZARdwqZqz8szHOIK9N/fSQAc20ikzpOLJPx6eN5d7vYHkn3E2w/K/1skevgR76Ifn8rcyfdEh5+kmui3lxmVvPw4G6dV/XWW2aXsf/ifRt5q09pC5FGWZ/BSNn73jYQwKgwoNozNddQnQo12U3KOdKHyNqCV9Z9bB4LDk+w1egCwQYd2UL0BOUkrhF8nlA1DA+AcHU5hOUICsCFqe/nmivhqqm6GOY3mxRiLw/0UXBkef3L7LSIxO6tRUpU3auwlOU0Itud2Q/O9LTewA8x2g32qWrOS+VarEtiXZ3cwXRB9xF3B8S81rp1ABNANeNWHSv0Q5s2UB5c=~3683640~4403255',
    'akavpau_vpc_gol_default': '1754482894~id=33645e14f42a6e14b3c7818d1536fe52',
    'akaas_gol_global': '1762258594~rv=22~id=3c1299f005e8e4073252a1adad7badbf',
    'bm_sv': '186A990A4194E870B09D631FB7E54C15~YAAQXYgsMTIa9WGYAQAAyNJPfxyRfth2Aka1ljS98PUkhVhoe+Wg5IHBA8P0YJrsxi5RhgBSlHbDnSZCdf4/FWmKUUiA1uVo9oZwagVwo6f3qksSY5uZfuEc85DIV+9XjrSoBTMAwr0IPQrd2wNlPXesycc2Pvykwt8C/HpgybKzxl+TXQYQYdMms+oYslHGmZ4/JcQSAYosve2ErcWX/9b9Q0Y+hrlOw8/0a9nE4QjkKYPn7UKrLweoNsfehQSSstbwh7uh~1',
    '_scid_r': '4jxW6R3ZYyNyfgPJS6ptEerBEmmZEifQBpJ6UA',
    '_ga_QD2JF6T7MG': 'GS2.1.s1754482586$o2$g1$t1754482595$j51$l0$h0',
    'utag_main': 'v_id:01987f0b556700516786ec85fe9805065005305d00bd0$_sn:2$_ss:0$_st:1754484395071$dc_visit:2$ses_id:1754482588691%3Bexp-session$_pn:1%3Bexp-session$dc_event:3%3Bexp-session$previousPageName:web%3Agroceries%3Abrowse%3Afrozen%3Afish%20and%20seafood%3Aall%3Bexp-session$previousPageType:shelf%3Bexp-session$previousSiteSection:browse%3Bexp-session$previousPagePath:%2Fgol-ui%2Fgroceries%2Ffrozen%2Ffish-and-seafood%2Fall%2Fc%3A1019911%3Bexp-session$dc_region:eu-west-1%3Bexp-session',
    '_cls_v': '7555b434-8b74-41db-9cca-6cd2311f1163',
    '_cls_s': 'bc0b4fb3-2652-45f0-82a0-c8bf342dd302:0',
    'Bc': 'd:0*0.1_p:0*0.005_r:null*null',
    '_fbp': 'fb.2.1754482597730.612790571200564948',
    'rto': 'c0',
    '_gcl_au': '1.1.574346634.1754482598',
    '_uetsid': '344c560072bf11f0a8fccf061ae6038a',
    '_uetvid': '344c7b7072bf11f0905667b02e5690be',
    '_pin_unauth': 'dWlkPU5UYzFNV1ZqWVRVdE9UTXhOaTAwWVRFeUxXRXlaR1F0T0dZNFltSXdaRFV6WW1Ndw',
}
USER_AGENTS = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
]
user_agent = random.choice(USER_AGENTS)

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'enabled-feature-flags': 'add_to_favourites,use_food_basket_service,use_food_basket_service_v3,ads_conditionals,findability_v5,show_static_cnc_messaging,fetch_future_slot_weeks,click_and_collect_promo_banner,cookie_law_link,citrus_banners,citrus_favourites_trio_banners,offers_trio_banners_single_call,special_logo,custom_product_messaging,promotional_link,promotional_link2,findability_search,findability_autosuggest,findability_orchestrator,fto_header_flag,recurring_slot_skip_opt_out,first_favourite_oauth_entry_point,seasonal_favourites,cnc_start_amend_order_modal,slot_confirmation_board,favourites_product_cta_alt,get_favourites_from_v2,krang_alternatives,offers_config,alternatives_modal,relevancy_rank,changes_to_trolley,nectar_destination_page,meal_deal_live,browse_pills_nav_type,zone_featured,use_cached_findability_results,event_zone_list,cms_carousel_zone_list,show_ynp_change_slot_banner,recipe_scrapbooks_enabled,event_carousel_skus,split_savings,trolley_nectar_card,favourites_magnolia,homepage,taggstar,meal_deal_cms_template_ids,pdp_accordions,pdp_meta_desc_template,grouped_meal_deals,hide_desc_mobile,pci_phase_2,enable_favourites_priority,meal_deal_builder_nectar_widget,new_favourites_filter,occasions_navigation,rokt,sales_window,resting_search,brands_background,brands_background_config,taggstar_config,all_ad_components_enabled,byg_ab_test_products_display_2,new_global_header,new_filter_pages,recipe_reviews_enabled,sponsored_drawer,frequently_bought_together,product_tile_experiment,pci_phase_3,show_ynp_opt_in_ui_elements,fetch_ynp_opt_ins,resting_search_v2,bop_enabled,favourites_boards,mobile_nav_2,should_not_scroll_into_view_fbt,show_popular_categories,track_remove_scroll_experiment,track_group_by_top_category,ynpoptin_national_launch,booking_confirmation_content_and_button,call_bcs,catchweight_dropdown,citrus_preview_new,citrus_search_trio_banners,citrus_xsell,compare_seasonal_favourites,constant_commerce_v2,ctt_ynp_products,desktop_interstitial_variant,disable_product_cache_validation,event_dates,favourites_pill_nav,favourites_whole_service,fbt_on_search,fbt_on_search_tracking,first_favourites_static,foodmaestro_modal,golui_payment_cards,hfss_restricted,interstitial_variant,kg_price_label,krang_recommendations,meal_planner,meganav,mobile_interstitial_variant,multi_styling,my_nectar_migration,nectar_card_associated,nectar_prices,new_favourites_service,new_filters,new_page_header,ni_brexit_banner,occasions,optimised_product_tile,promo_lister_page,recipes_ingredients_modal,review_syndication,sale_january,show_hd_xmas_slots_banner,similar_products,slot_v2,xmas_dummy_skus,ynp_np_zonalpage,your_nectar_prices',
    'priority': 'u=1, i',
    'referer': 'https://www.sainsburys.co.uk/gol-ui/groceries/frozen/fish-and-seafood/all/c:1019911',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-f0ce5a422d36660a14843ff2827e5210-c8dcf179b6072f9b-01',
    'tracestate': '2092320@nr=0-1-1782819-181742266-c8dcf179b6072f9b----1754478110375',
    'user-agent': user_agent,
    'wcauthtoken': '',
    # 'cookie': 'ak_bmsc=EB698D07E5B9CBD59391BB0F85DA8195~000000000000000000000000000000~YAAQXYgsMfnm2GGYAQAAf1ELfxypwyRLFIiSwlJrp5TbcFciCA9O+8WkPpTAa0TbaQZa7qDnyOQjq3WzN5wGPHzi2opByhoXj7Jbym9OJvnxvGb1c2xsIkoBnSbyFbmPV7elL7G99Qdiys8k8esBHXzelXYTWe5NGN5MGBkrWoiphLGnTDiPVog6zx8nenB1fdOd72Xua5q/XY4izstuBTCtDoHAWFfUsUARn5b0XJTa33bowg/ElE0ZLwoIKk913zQTFGBvngV2E3qI5AwJ1xbcrELiYLjLVGT1LSgS800IkBZnwvv+8QIuAgCVRrNORALCsmxcykBsF5/nNA+vyUcFRnaGo6cYcT4PgaqLbfTQuoEYngESUCRMnCDGbd5Ov2ZXPBoRpdvQjFyiO6Z17OWdXLE/msuIT+vMAZfpkNwwkiIDZMMrXYY=; bm_sz=49800B3137F5EE71A1A944AD68404AB4~YAAQXYgsMfrm2GGYAQAAf1ELfxwdsPPHSRjNBvExkTR5unkk6emCxxhxmEVMRWEPTQ7gfdpMaoiVaBF7qa6Z0XE+KWPz6v3TwgiUNhJtQGvWHHj6QbCIF78i7D00dnxwj3azhi6jgKlebs/s9xAwJOMCsl+bWN4Usg/9ASyID6Z1KLf7N9U0U61q5Ot3oYdG2w/3yhso4/9kE2HpVGbosmXY00JH45Bw4wR5DpgV/mapY4YjJzcvB6ZPHbaUzlobpOb9CplFj4BKQ9c2bdh2Lk6MwxKufdbt4OD2vwUCj9Ei8aBNleaB0//0sJcLneXtX0ar+A5wGTyi9ceF1jyFm5EENzdDZbfcTIKGLfdqp4sctPPp4RXF2YuNnsiZKQGnI2w9EibXGICNvI2RVPsyyv4g3T4d/i/Qmo+7WVyNfuxJtUHYHkfIu/jDxP4dng==~3683640~4403255; utag_main=v_id:01987f0b556700516786ec85fe9805065005305d00bd0$_sn:1$_ss:1$_st:1754479905959$ses_id:1754478105959%3Bexp-session$_pn:1%3Bexp-session; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Aug+06+2025+16%3A31%3A47+GMT%2B0530+(India+Standard+Time)&version=202501.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=1bf98b35-46ed-4314-94d6-4fbff1412aa7&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.sainsburys.co.uk%2Fgol-ui%2Fgroceries%2Ffrozen%2Ffish-and-seafood%2Fall%2Fc%3A1019911&groups=1%3A1%2C2%3A0%2C3%3A0%2C4%3A0; _abck=A750A3EE6CA6B3446707CA5F2DDBB9BC~-1~YAAQXYgsMers2GGYAQAAu10Lfw5MJFG2Twlp6DcheVOPRfw7JM41Hp8Tby6ik8pCwy28NKKr2EhWd1TjAnB1hw92ptma/lzuhJeJyC0nsHrRYKhUVQCXwdBpqcxQOR+7/zPAMQnbXHvXzei3uWCYgFp1u0UtvufJGEf9GgvgoHEIX5evU9mw+bsW4mr3Cml+lqvgiu2tNX6Cr/liRbzGwKaGY5bOAZ7WoelcD8p1RkVmDm3WzNhYhKrBQErcP9e/cFPqvQ2am49+cYTvfSYWkN697kgxll9TG/ttimGC22h7IlMyo/ytnKUNXtOQt2vjXE3f8M4Kb1SzPhw6e75aw6MKDiDeDiaaieWmx8+i6GVEYHHGnCUCHAMBij13Umjy/zLuiAU3+qAZ91/ltEirLWg8RuyXkk+L55z7X0cD7i9dtnEnxCDGw1hjhURFxnX6OoEFGgg/Z60d9+Btmu5R9Eea93Y8kg6XYhy+h+p/buC2G/a8olr3VqauESdlCEnJI9/UqSm7q9tvPCE8KY2JAnsH8wkZrAsP1A6kOwQHfe3luGBuV3opmSaxaq+D5o3TnlUHoCZ3U3TWGKEmGDNJ7ras6jCALQ/KkGD2RWpZVLP2cqk=~-1~-1~-1; last_button_track=false; akavpau_vpc_gol_default=1754478409~id=d1cdcadf1418440543d7ab85db0c9927; AWSALB=7KbNTZM79X6wQAeskZzwBUyuq7T6zllNWv5rrsESPX2LWei8WsUoaOjXI3YJVRL1CVPJpecmb2TlkAAnSNsi2g4jQqa44d+5tALGe3TCbmcJPpx4yVpiSWLCHLsv; AWSALBCORS=7KbNTZM79X6wQAeskZzwBUyuq7T6zllNWv5rrsESPX2LWei8WsUoaOjXI3YJVRL1CVPJpecmb2TlkAAnSNsi2g4jQqa44d+5tALGe3TCbmcJPpx4yVpiSWLCHLsv; Apache=10.8.240.42.1754478109199686; JSESSIONID=0000qooodfbzD6XUwfDRYVsd2At:1h0f7p25f; akaas_gol_global=1762254109~rv=22~id=d85cc240181cdb5a9dcfd8407779e3fa; bm_sv=186A990A4194E870B09D631FB7E54C15~YAAQXYgsMbvv2GGYAQAAmWMLfxwi2JGWhsj4DfHxAyeevdhuzdDgrh90HkXSzoj4k6bly8RNDnkmZSzx9/AWasW7dwgdG86YR81jsFRQA5FWB+xbLhB8sbL7f/AUy20ynuDbWg6o4u55aY0w9x9R/jDf+vsLAL/r5sZ/Y4jy1ujZEiPaHNhDwpZFqL8Bb/WIW+y6YgcbRKBJ6by/1sh50owixRA0ArOPZ/WutmiVJzxcMrAx9aVM/CbYIVE5HCCoL9E5leY3~1',
}
print(user_agent)
session = requests.Session()  
response = session.get(
    'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[keyword]=&filter[category]=271267&browse=true&hfss_restricted=false&categoryId=271267&sort_order=FAVOURITES_FIRST&favouritesPriority=true&include[PRODUCT_AD]=citrus&citrus_placement=category-only&salesWindow=1',
    headers=headers,
    cookies=cookies,impersonate='chrome101',http_version=1 
)
# data = response.json()
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4) 
print(response.status_code)
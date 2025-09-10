from pymongo import MongoClient
from parsel import Selector
import json
import re
from datetime import datetime
extraction_date = datetime.now().strftime('%Y-%m-%d')

MONGO_URL = "mongodb://localhost:27017"
MONGO_DB = 'walmart'
COLLECTION = 'data'
COLLECTION_DETAILS='product_details'

client = MongoClient(MONGO_URL)
db = client[MONGO_DB]
collection = db[COLLECTION_DETAILS]

for item in db[COLLECTION].find():
    response = item.get('response', '')
    sel = Selector(text=response)

    competitor_name = 'walmart'
    store_name = ''
    store_addressline1 = ''
    store_addressline2 = ''
    store_suburb = ''
    store_state = ''
    store_postcode = ''
    store_addressid = ''
    extraction_date = extraction_date

    script_text = sel.xpath("//script[@type='application/ld+json' and @data-seo-id='schema-org-product']/text()").get()
    try:
        data = json.loads(script_text) if script_text else {}
    except json.JSONDecodeError:
        data = {}

    if isinstance(data, dict):
        product_name = data.get('name', '')
        brand = data.get('brand', {}).get('name', '')
        unique_id = data.get('sku', '')
        upc = data.get('gtin13', '')
        image_url_1 = data.get('image', '')
    elif isinstance(data, list) and len(data) > 0:
        product_name = data[0].get('name', '')
        brand = data[0].get('brand', {}).get('name', '')
        unique_id = data[0].get('sku', '')
        upc = data[0].get('gtin13', '')
        image_url_1 = data[0].get('image', '')
    else:
        product_name = brand = unique_id = upc = image_url_1 = ''

    brand_type = ''

    grammage_quantity = re.search(r'(\d+(\.\d+)?)\s*(oz|g|kg|ml|l)?', product_name)
    grammage_quantity = grammage_quantity.group(1) if grammage_quantity else ''
    grammage_unit = re.search(r'\b(fl oz|oz|ml|g|kg|lb|l)\b', product_name, re.IGNORECASE)
    grammage_unit = grammage_unit.group(0) if grammage_unit else ''
    drained_weight = ''

    script_text_one = sel.xpath("//script[@id='__NEXT_DATA__' and @type='application/json']/text()").get()
    try:
        data_one = json.loads(script_text_one) if script_text_one else {}
    except json.JSONDecodeError:
        data_one = {}

    modules = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('seoItemMetaData', {})
    breadcrumb_names = modules.get('breadCrumbs', [])
    breadcrumb_names = [b.get('name', '') for b in breadcrumb_names]
    breadcrumb=' > '.join(breadcrumb_names)

    producthierarchy_level1=breadcrumb_names[0] if len(breadcrumb_names) > 0 else ''
    producthierarchy_level2=breadcrumb_names[1] if len(breadcrumb_names) > 1 else ''
    producthierarchy_level3=breadcrumb_names[2] if len(breadcrumb_names) > 2 else ''
    producthierarchy_level4=breadcrumb_names[3] if len(breadcrumb_names) > 3 else ''
    producthierarchy_level5=breadcrumb_names[4] if len(breadcrumb_names) > 4 else ''
    producthierarchy_level6=breadcrumb_names[5] if len(breadcrumb_names) > 5 else ''
    producthierarchy_level7=breadcrumb_names[6] if len(breadcrumb_names) > 6 else ''

    if isinstance(data, dict):
        offers_list = data.get('offers', [])
    elif isinstance(data, list) and len(data) > 0:
        offers_list = data[0].get('offers', [])
    else:
        offers_list = []

    if offers_list:
        regular_price = offers_list[0].get('price', '')
        selling_price = regular_price
        currency = offers_list[0].get('priceCurrency', '')
        pdp_url = offers_list[0].get('url', '')
    else:
        regular_price = selling_price = currency = pdp_url = ''

    price_was = ''
    promotion_price = ''
    promotion_valid_from = ''
    promotion_valid_upto = ''
    promotion_type = ''
    percentage_discount = ''
    promotion_description = ''
    package_sizeof_sellingprice = ''
    per_unit_sizedescription = ''
    price_valid_from = ''
    price_per_unit = sel.xpath("//span[@data-seo-id='hero-unit-price']/text()").get() or ''
    multi_buy_item_count = ''
    multi_buy_items_price_total = ''
    variants = ''

    if isinstance(data, dict):
        product_description = data.get('description', '')
    elif isinstance(data, list) and len(data) > 0:
        product_description = data[0].get('description', '')
    else:
        product_description = ''

    instructions_list = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('idml', {}).get('directions', [])
    instructions = ' '.join([instr.get('value','').replace('\n',' ').strip() for instr in instructions_list])
    storage_instructions=''
    preparationinstructions=''
    instructionforuse=''
    country_of_origin=''

    specifications_list = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('idml', {}).get('specifications', [])
    specifications = specifications_list[1] if len(specifications_list) > 1 else {}
    allergens = specifications.get('value','')
    age_of_the_product=''
    age_recommendations=''
    flavour=''
    nutritions=''

    def safe_get(d, keys, default=None):
        for key in keys:
            if isinstance(d, dict):
                d = d.get(key, default)
            else:
                return default
        return d

    key_nutrients = safe_get(
        data_one,
        ['props', 'pageProps', 'initialData', 'data', 'idml', 'nutritionFacts', 'keyNutrients', 'values'],
        []
    )

    vitamin_minerals = safe_get(
        data_one,
        ['props', 'pageProps', 'initialData', 'data', 'idml', 'nutritionFacts', 'vitaminMinerals', 'childNutrients'],
        []
    )

    nutritional_information = {}

    def process_nutrient(nutrient_list):
        for nutrient in nutrient_list:
            if not isinstance(nutrient, dict):
                continue
            main = nutrient.get('mainNutrient', {})
            main_name = main.get('name')
            main_amount = main.get('amount')
            main_dvp = main.get('dvp')
            if main_name and main_dvp:
                key = f"{main_name} {main_amount}" if main_amount else main_name
                nutritional_information[key] = main_dvp
            child_nutrients = nutrient.get('childNutrients') or []
            for child in child_nutrients:
                child_name = child.get('name')
                child_amount = child.get('amount')
                child_dvp = child.get('dvp')
                if child_name and child_dvp:
                    key = f"{child_name} {child_amount}" if child_amount else child_name
                    nutritional_information[key] = child_dvp
                if child.get('childNutrients'):
                    process_nutrient([child])

    process_nutrient(key_nutrients)

    for vitamin in vitamin_minerals:
        name = vitamin.get('name')
        amount = vitamin.get('amount')
        dvp = vitamin.get('dvp')
        if name and dvp:
            key = f"{name} {amount}" if amount else name
            nutritional_information[key] = dvp

    warning_list = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('idml', {}).get('warnings', [])
    warning = ''
    if warning_list:
        warning_value = warning_list[0].get('value')
        if warning_value and warning_value != "None":
            warning = warning_value

    vitamins=''
    labelling=''
    grade=''
    region=''
    packaging=''
    receipies=''
    processed_food=''
    barcode=''
    frozen=''
    chilled=''
    organictype=''
    cooking_part=''
    handmade=''
    max_heating_temperature=''
    special_information=''
    label_information=''
    dimensions=''
    special_nutrition_purpose=''
    feeding_recommendation=''
    warranty = ''   
    color=''
    model_number=''
    material=''
    usp=''
    dosage_recommendation=''
    tasting_note=''
    food_preservation=''
    size=''
    file_name_1=''
    file_name_2=''
    image_url_2=''
    file_name_3=''
    image_url_3=''
    file_name_4=''
    image_url_4=''
    file_name_5=''
    image_url_5=''
    file_name_6=''
    image_url_6=''
    competitor_product_key = ''
    fit_guide = ''
    occasion = ''
    material_composition = ''
    style = ''
    care_instructions = ''
    heel_type = ''
    heel_height = ''
    features = ''
    dietary_lifestyle = ''
    manufacturer_address = ''
    importer_address = ''
    distributor_address = ''
    vinification_details = ''
    recycling_information = ''
    return_address = ''
    alchol_by_volume = ''
    beer_deg = ''
    netcontent = ''
    netweight = ''
    site_shown_uom = ''
    random_weight_flag = ''
    instock = ''
    promo_limit = ''
    product_unique_key = ''
    multibuy_items_pricesingle = ''
    perfect_match = ''
    servings_per_pack = ''
    warning = ''
    suitable_for = ''
    standard_drinks = ''
    environmental = ''
    grape_variety = ''
    retail_limit = ''


    ingredients_dict = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('idml', {}).get('ingredients', {})
    ingredients = ''
    if isinstance(ingredients_dict, dict):
        inner_ingredients = ingredients_dict.get('ingredients', {})
        if isinstance(inner_ingredients, dict):
            ingredients = inner_ingredients.get('value','')

    rating = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('product', {}).get('averageRating', '')
    review = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}).get('data', {}).get('product', {}).get('numberOfReviews', '')

    item = {
        "unique_id": unique_id,
        "competitor_name": competitor_name,
        "store_name": store_name,
        "store_addressline1": store_addressline1,
        "store_addressline2": store_addressline2,
        "store_suburb": store_suburb,
        "store_state": store_state,
        "store_postcode": store_postcode,
        "store_addressid": store_addressid,
        "extraction_date": extraction_date,
        "product_name": product_name,
        "brand": brand,
        "brand_type": brand_type,
        "grammage_quantity": grammage_quantity,
        "grammage_unit": grammage_unit,
        "drained_weight": drained_weight,
        "producthierarchy_level1": producthierarchy_level1,
        "producthierarchy_level2": producthierarchy_level2,
        "producthierarchy_level3": producthierarchy_level3,
        "producthierarchy_level4": producthierarchy_level4,
        "producthierarchy_level5": producthierarchy_level5,
        "producthierarchy_level6": producthierarchy_level6,
        "producthierarchy_level7": producthierarchy_level7,
        "regular_price": regular_price,
        "selling_price": selling_price,
        "price_was": price_was,
        "promotion_price": promotion_price,
        "promotion_valid_from": promotion_valid_from,
        "promotion_valid_upto": promotion_valid_upto,
        "promotion_type": promotion_type,
        "percentage_discount": percentage_discount,
        "promotion_description": promotion_description,
        "package_sizeof_sellingprice": package_sizeof_sellingprice,
        "per_unit_sizedescription": per_unit_sizedescription,
        "price_valid_from": price_valid_from,
        "price_per_unit": price_per_unit,
        "multi_buy_item_count": multi_buy_item_count,
        "multi_buy_items_price_total": multi_buy_items_price_total,
        "currency": currency,
        "breadcrumb": breadcrumb,
        "pdp_url": pdp_url,
        "variants": variants,
        "product_description": product_description,
        "instructions": instructions,
        "storage_instructions": storage_instructions,
        "preparationinstructions": preparationinstructions,
        "instructionforuse": instructionforuse,
        "country_of_origin": country_of_origin,
        "allergens": allergens,
        "age_of_the_product": age_of_the_product,
        "age_recommendations": age_recommendations,
        "flavour": flavour,
        "nutritions": nutritions,
        "nutritional_information": nutritional_information,
        "vitamins": vitamins,
        "labelling": labelling,
        "grade": grade,
        "region": region,
        "packaging": packaging,
        "receipies": receipies,
        "processed_food": processed_food,
        "barcode": barcode,
        "frozen": frozen,
        "chilled": chilled,
        "organictype": organictype,
        "cooking_part": cooking_part,
        "handmade": handmade,
        "max_heating_temperature": max_heating_temperature,
        "special_information": special_information,
        "label_information": label_information,
        "dimensions": dimensions,
        "special_nutrition_purpose": special_nutrition_purpose,
        "feeding_recommendation": feeding_recommendation,
        "warranty": warranty,
        "color": color,
        "model_number": model_number,
        "material": material,
        "usp": usp,
        "dosage_recommendation": dosage_recommendation,
        "tasting_note": tasting_note,
        "food_preservation": food_preservation,
        "size": size,
        "rating": rating,
        "review": review,
        "file_name_1": file_name_1,
        "image_url_1": image_url_1,
        "file_name_2": file_name_2,
        "image_url_2": image_url_2,
        "file_name_3": file_name_3,
        "image_url_3": image_url_3,
        "file_name_4": file_name_4,
        "image_url_4": image_url_4,
        "file_name_5": file_name_5,
        "image_url_5": image_url_5,
        "file_name_6": file_name_6,
        "image_url_6": image_url_6,
        "competitor_product_key": competitor_product_key,
        "fit_guide": fit_guide,
        "occasion": occasion,
        "material_composition": material_composition,
        "style": style,
        "care_instructions": care_instructions,
        "heel_type": heel_type,
        "heel_height": heel_height,
        "upc": upc,
        "features": features,
        "dietary_lifestyle": dietary_lifestyle,
        "manufacturer_address": manufacturer_address,
        "importer_address": importer_address,
        "distributor_address": distributor_address,
        "vinification_details": vinification_details,
        "recycling_information": recycling_information,
        "return_address": return_address,
        "alchol_by_volume": alchol_by_volume,
        "beer_deg": beer_deg,
        "netcontent": netcontent,
        "netweight": netweight,
        "site_shown_uom": site_shown_uom,
        "ingredients": ingredients,
        "random_weight_flag": random_weight_flag,
        "instock": instock,
        "promo_limit": promo_limit,
        "product_unique_key": product_unique_key,
        "multibuy_items_pricesingle": multibuy_items_pricesingle,
        "perfect_match": perfect_match,
        "servings_per_pack": servings_per_pack,
        "warning": warning,
        "suitable_for": suitable_for,
        "standard_drinks": standard_drinks,
        "environmental": environmental,
        "grape_variety": grape_variety,
        "retail_limit": retail_limit
    }


    print(nutritional_information)
    collection.insert_one(item)

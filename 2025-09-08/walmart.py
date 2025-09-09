from pymongo import MongoClient
from parsel import Selector
import json
import re
import csv
import os

MONGO_URL = "mongodb://localhost:27017"
MONGO_DB = 'walmart'
COLLECTION = 'data'
CSV_FILE = 'walmart_20250909.csv'

client = MongoClient(MONGO_URL)
db = client[MONGO_DB]

file_exists = os.path.isfile(CSV_FILE)
write_header = not file_exists or os.path.getsize(CSV_FILE) == 0

with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    headers = [
    'competitor_name', 'store_name', 'store_addressline1', 'store_addressline2',
    'store_suburb', 'store_state', 'store_postcode', 'store_addressid',
    'extraction_date', 'product_name', 'brand', 'brand_type', 'unique_id',
    'grammage_quantity', 'grammage_unit', 'drained_weight', 'producthierarchy_level1',
    'producthierarchy_level2', 'producthierarchy_level3', 'producthierarchy_level4',
    'producthierarchy_level5', 'producthierarchy_level6', 'producthierarchy_level7',
    'regular_price', 'selling_price', 'currency', 'pdp_url', 'price_was',
    'promotion_price', 'promotion_valid_from', 'promotion_valid_upto', 'promotion_type',
    'percentage_discount', 'promotion_description', 'package_sizeof_sellingprice',
    'per_unit_sizedescription', 'price_valid_from', 'price_per_unit', 'multi_buy_item_count',
    'multi_buy_items_price_total', 'breadcrumb', 'variants', 'product_description',
    'instructions', 'storage_instructions', 'preparationinstructions', 'instructionforuse',
    'country_of_origin', 'allergens', 'specifications', 'age_of_the_product',
    'age_recommendations', 'flavour', 'nutritions', 'nutritional_information',
    'vitamins', 'labelling', 'grade', 'region', 'packaging', 'receipies', 'processed_food',
    'barcode', 'frozen', 'chilled', 'organictype', 'cooking_part', 'handmade',
    'max_heating_temperature', 'special_information', 'label_information', 'dimensions',
    'special_nutrition_purpose', 'feeding_recommendation', 'warranty', 'color', 'model_number',
    'material', 'usp', 'dosage_recommendation', 'tasting_note', 'food_preservation', 'size',
    'rating', 'review', 'file_name_1', 'image_url_1', 'file_name_2', 'image_url_2',
    'file_name_3', 'image_url_3', 'file_name_4', 'image_url_4', 'file_name_5', 'image_url_5',
    'file_name_6', 'image_url_6', 'competitor_product_key', 'fit_guide', 'occasion',
    'material_composition', 'style', 'care_instructions', 'heel_type', 'heel_height',
    'upc', 'features', 'dietary_lifestyle', 'manufacturer_address', 'importer_address',
    'distributor_address', 'vinification_details', 'recycling_information', 'return_address',
    'alchol_by_volume', 'beer_deg', 'netcontent', 'netweight', 'site_shown_uom',
    'ingredients', 'random_weight_flag', 'instock', 'promo_limit', 'product_unique_key',
    'multibuy_items_pricesingle', 'perfect_match', 'servings_per_pack', 'warning', 'suitable_for',
    'standard_drinks', 'environmental', 'grape_variety', 'retail_limit'
]
    if write_header:
        writer.writerow(headers)

    # Iterate through documents from MongoDB
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
        extraction_date = ''
        
        script_text = sel.xpath("//script[@type='application/ld+json' and @data-seo-id='schema-org-product']/text()").get()
        data = json.loads(script_text)
        
        if isinstance(data, dict):
            product_name = data.get('name', '')
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            product_name = data[0].get('name', '')
        else:
            product_name = ''        
        if isinstance(data, dict):
            brand = data.get('brand', {}).get('name', '')
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            brand = data[0].get('brand', {}).get('name', '')
        else:
            brand = ''        
        brand_type = ''
        if isinstance(data, dict):
            unique_id = data.get('sku', '')
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            unique_id = data[0].get('sku', '')
        else:
            unique_id = ''
        
        grammage_quantity = re.search(r'\d+(\.\d+)?', product_name)
        if grammage_quantity:
            grammage_quantity = grammage_quantity.group(0)
        
        grammage_unit = re.search(r'\b(oz|ml|g|kg|lb|l)\b', product_name, re.IGNORECASE)
        if grammage_unit:
            grammage_unit = grammage_unit.group(0)
        
        drained_weight = ''
        
        script_text = sel.xpath("//script[@id='__NEXT_DATA__' and @type='application/json']/text()").get()
        data_one = json.loads(script_text)
        
        modules = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}) \
            .get('data', {}).get('seoItemMetaData', {})
        
        breadcrumb = modules.get('breadCrumbs', [])
        producthierarchy_level1 = breadcrumb[0].get('name', '') if len(breadcrumb) > 0 else ''
        producthierarchy_level2 = breadcrumb[1].get('name', '') if len(breadcrumb) > 1 else ''
        producthierarchy_level3 = breadcrumb[2].get('name', '') if len(breadcrumb) > 2 else ''
        producthierarchy_level4 = breadcrumb[3].get('name', '') if len(breadcrumb) > 3 else ''
        producthierarchy_level5 = breadcrumb[4].get('name', '') if len(breadcrumb) > 4 else ''
        producthierarchy_level6 = breadcrumb[5].get('name', '') if len(breadcrumb) > 5 else ''
        producthierarchy_level7 = breadcrumb[6].get('name', '') if len(breadcrumb) > 6 else ''
            
        if isinstance(data, dict):
            offers_list = data.get('offers', [])
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            offers_list = data[0].get('offers', [])
        else:
            offers_list = []        
        if offers_list:
            regular_price = offers_list[0].get('price')
            selling_price = regular_price
            currency = offers_list[0].get('priceCurrency')
            pdp_url = offers_list[0].get('url')
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
        price_per_unit = sel.xpath("//span[@data-seo-id='hero-unit-price']/text()").get()
        multi_buy_item_count = ''
        multi_buy_items_price_total = ''
        
        breadcrumb_names = [item.get('name','') for item in breadcrumb]
        breadcrumb_str = ' > '.join(breadcrumb_names)
        
        variants = ''
        if isinstance(data, dict):
            product_description = data.get('description', '')
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            product_description = data[0].get('description', '')
        else:
            product_description = ''
        
        instructions = []
        instructions_list = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}) \
            .get('data', {}).get('idml',{}).get('directions', [])
        
        for instr in instructions_list:
            name = instr.get('value', '').replace('\n', ' ').strip()
            instructions.append(name)
        
        instructions = ' '.join(instructions)
        
        storage_instructions = ''
        preparationinstructions = ''
        instructionforuse = ''
        country_of_origin = ''
        
        specifications_list = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}) \
            .get('data', {}).get('idml', {}).get('specifications', [])
        
        specifications = specifications_list[1] if len(specifications_list) > 1 else {}
        allergens = specifications.get('value', '')
        
        age_of_the_product = ''
        age_recommendations = ''
        flavour = ''
        nutritions = ''
        nutritional_information=''
        vitamins = ''
        labelling = ''
        grade = ''
        region = ''
        packaging = ''
        receipies = ''
        processed_food = ''
        barcode = ''
        frozen = ''
        chilled = ''
        organictype = ''
        cooking_part = ''
        handmade = ''
        max_heating_temperature = ''
        special_information = ''
        label_information = ''
        dimensions = ''
        special_nutrition_purpose = ''
        feeding_recommendation = ''
        warranty = ''
        color = ''
        model_number = ''
        material = ''
        usp = ''
        dosage_recommendation = ''
        tasting_note = ''
        food_preservation = ''
        size = ''
        
        rating = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}) \
            .get('data', {}).get('product', {}).get('averageRating', '')
        
        review = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}) \
            .get('data', {}).get('product', {}).get('numberOfReviews', '')
        
        file_name_1 = ''
        if isinstance(data, dict):
            image_url_1 = data.get('image', '')
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            image_url_1 = data[0].get('image', '')
        else:
            image_url_1 = ''
        file_name_2 = ''
        image_url_2 = ''
        file_name_3 = ''
        image_url_3 = ''
        file_name_4 = ''
        image_url_4 = ''
        file_name_5 = ''
        image_url_5 = ''
        file_name_6 = ''
        image_url_6 = ''
        
        competitor_product_key = ''
        fit_guide = ''
        occasion = ''
        material_composition = ''
        style = ''
        care_instructions = ''
        heel_type = ''
        heel_height = ''
        
        if isinstance(data, dict):
            upc = data.get('gtin13', '')
        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            upc = data[0].get('gtin13', '')
        else:
            upc = ''
        
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
        ingredients_dict = data_one.get('props', {}) \
            .get('pageProps', {}) \
            .get('initialData', {}) \
            .get('data', {}) \
            .get('idml', {}) \
            .get('ingredients')

        ingredients = ''
        if isinstance(ingredients_dict, dict):
            inner_ingredients = ingredients_dict.get('ingredients')
            if isinstance(inner_ingredients, dict):
                ingredients = inner_ingredients.get('value', '')



        
        random_weight_flag = ''
        instock = ''
        promo_limit = ''
        product_unique_key = ''
        multibuy_items_pricesingle = ''
        perfect_match = ''
        servings_per_pack = ''
        
        warning_list = data_one.get('props', {}).get('pageProps', {}).get('initialData', {}) \
            .get('data', {}).get('idml', {}).get('warnings', [])
        
        warning = warning_list[0].get('value') if warning_list and warning_list[0].get('value') != "None" else ''
        
        suitable_for = ''
        standard_drinks = ''
        environmental = ''
        grape_variety = ''
        retail_limit = ''
        
        # Create the row of data
        row = [
            competitor_name, store_name, store_addressline1, store_addressline2,
            store_suburb, store_state, store_postcode, store_addressid,
            extraction_date, product_name, brand, brand_type, unique_id,
            grammage_quantity, grammage_unit, drained_weight, producthierarchy_level1,
            producthierarchy_level2, producthierarchy_level3, producthierarchy_level4,
            producthierarchy_level5, producthierarchy_level6, producthierarchy_level7,
            regular_price, selling_price, currency, pdp_url, price_was,
            promotion_price, promotion_valid_from, promotion_valid_upto, promotion_type,
            percentage_discount, promotion_description, package_sizeof_sellingprice,
            per_unit_sizedescription, price_valid_from, price_per_unit, multi_buy_item_count,
            multi_buy_items_price_total, breadcrumb_str, variants, product_description,
            instructions, storage_instructions, preparationinstructions, instructionforuse,
            country_of_origin, allergens, json.dumps(specifications), age_of_the_product,
            age_recommendations, flavour, nutritions, nutritional_information,
            vitamins, labelling, grade, region, packaging, receipies, processed_food,
            barcode, frozen, chilled, organictype, cooking_part, handmade,
            max_heating_temperature, special_information, label_information, dimensions,
            special_nutrition_purpose, feeding_recommendation, warranty, color, model_number,
            material, usp, dosage_recommendation, tasting_note, food_preservation, size,
            rating, review, file_name_1, image_url_1, file_name_2, image_url_2,
            file_name_3, image_url_3, file_name_4, image_url_4, file_name_5, image_url_5,
            file_name_6, image_url_6, competitor_product_key, fit_guide, occasion,
            material_composition, style, care_instructions, heel_type, heel_height,
            upc, features, dietary_lifestyle, manufacturer_address, importer_address,
            distributor_address, vinification_details, recycling_information, return_address,
            alchol_by_volume, beer_deg, netcontent, netweight, site_shown_uom,
            ingredients, random_weight_flag, instock, promo_limit, product_unique_key,
            multibuy_items_pricesingle, perfect_match, servings_per_pack, warning, suitable_for,
            standard_drinks, environmental, grape_variety, retail_limit
        ]

        writer.writerow(row)


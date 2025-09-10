from pymongo import MongoClient
import csv,re

MONGO_URL = "mongodb://localhost:27017"
MONGO_DB = 'walmart'
COLLECTION_DETAILS = 'product_details'

class Export:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]

    def start(self):
        csv_file = 'walmart_20250910.csv'
        
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = None
            
            for item in self.db[COLLECTION_DETAILS].find():
                unique_id = item.get('unique_id')
                competitor_name = item.get('competitor_name')
                store_name = item.get('store_name')
                store_addressline1 = item.get('store_addressline1')
                store_addressline2 = item.get('store_addressline2')
                store_suburb = item.get('store_suburb')
                store_state = item.get('store_state')
                store_postcode = item.get('store_postcode')
                store_addressid = item.get('store_addressid')
                extraction_date = item.get('extraction_date')
                product_name = item.get('product_name')
                brand = item.get('brand')
                brand_type = item.get('brand_type')
                grammage_quantity = item.get('grammage_quantity')
                grammage_unit = item.get('grammage_unit')
                drained_weight = item.get('drained_weight')
                producthierarchy_level1 = item.get('producthierarchy_level1')
                producthierarchy_level2 = item.get('producthierarchy_level2')
                producthierarchy_level3 = item.get('producthierarchy_level3')
                producthierarchy_level4 = item.get('producthierarchy_level4')
                producthierarchy_level5 = item.get('producthierarchy_level5')
                producthierarchy_level6 = item.get('producthierarchy_level6')
                producthierarchy_level7 = item.get('producthierarchy_level7')
                regular_price = item.get('regular_price')
                selling_price = item.get('selling_price')
                price_was = item.get('price_was')
                promotion_price = item.get('promotion_price')
                promotion_valid_from = item.get('promotion_valid_from')
                promotion_valid_upto = item.get('promotion_valid_upto')
                promotion_type = item.get('promotion_type')
                percentage_discount = item.get('percentage_discount')
                promotion_description = item.get('promotion_description')
                package_sizeof_sellingprice = item.get('package_sizeof_sellingprice')
                per_unit_sizedescription = item.get('per_unit_sizedescription')
                price_valid_from = item.get('price_valid_from')
                price_per_unit = item.get('price_per_unit')
                multi_buy_item_count = item.get('multi_buy_item_count')
                multi_buy_items_price_total = item.get('multi_buy_items_price_total')
                currency = item.get('currency')
                breadcrumb = item.get('breadcrumb')
                pdp_url = item.get('pdp_url')
                variants = item.get('variants')
                product_description = item.get('product_description')
                instructions = item.get('instructions')
                storage_instructions = item.get('storage_instructions')
                preparationinstructions = item.get('preparationinstructions')
                instructionforuse = item.get('instructionforuse')
                country_of_origin = item.get('country_of_origin')
                allergens = item.get('allergens')
                age_of_the_product = item.get('age_of_the_product')
                age_recommendations = item.get('age_recommendations')
                flavour = item.get('flavour')
                nutritions = item.get('nutritions')
                nutritional_information = item.get('nutritional_information')
                vitamins = item.get('vitamins')
                labelling = item.get('labelling')
                grade = item.get('grade')
                region = item.get('region')
                packaging = item.get('packaging')
                receipies = item.get('receipies')
                processed_food = item.get('processed_food')
                barcode = item.get('barcode')
                frozen = item.get('frozen')
                chilled = item.get('chilled')
                organictype = item.get('organictype')
                cooking_part = item.get('cooking_part')
                handmade = item.get('handmade')
                max_heating_temperature = item.get('max_heating_temperature')
                special_information = item.get('special_information')
                label_information = item.get('label_information')
                dimensions = item.get('dimensions')
                special_nutrition_purpose = item.get('special_nutrition_purpose')
                feeding_recommendation = item.get('feeding_recommendation')
                warranty = item.get('warranty')
                color = item.get('color')
                model_number = item.get('model_number')
                material = item.get('material')
                usp = item.get('usp')
                dosage_recommendation = item.get('dosage_recommendation')
                tasting_note = item.get('tasting_note')
                food_preservation = item.get('food_preservation')
                size = item.get('size')
                rating = item.get('rating')
                review = item.get('review')
                file_name_1 = item.get('file_name_1')
                image_url_1 = item.get('image_url_1')
                file_name_2 = item.get('file_name_2')
                image_url_2 = item.get('image_url_2')
                file_name_3 = item.get('file_name_3')
                image_url_3 = item.get('image_url_3')
                file_name_4 = item.get('file_name_4')
                image_url_4 = item.get('image_url_4')
                file_name_5 = item.get('file_name_5')
                image_url_5 = item.get('image_url_5')
                file_name_6 = item.get('file_name_6')
                image_url_6 = item.get('image_url_6')
                competitor_product_key = item.get('competitor_product_key')
                fit_guide = item.get('fit_guide')
                occasion = item.get('occasion')
                material_composition = item.get('material_composition')
                style = item.get('style')
                care_instructions = item.get('care_instructions')
                heel_type = item.get('heel_type')
                heel_height = item.get('heel_height')
                upc = item.get('upc')
                features = item.get('features')
                dietary_lifestyle = item.get('dietary_lifestyle')
                manufacturer_address = item.get('manufacturer_address')
                importer_address = item.get('importer_address')
                distributor_address = item.get('distributor_address')
                vinification_details = item.get('vinification_details')
                recycling_information = item.get('recycling_information')
                return_address = item.get('return_address')
                alchol_by_volume = item.get('alchol_by_volume')
                beer_deg = item.get('beer_deg')
                netcontent = item.get('netcontent')
                netweight = item.get('netweight')
                site_shown_uom = item.get('site_shown_uom')
                ingredients = item.get('ingredients')
                random_weight_flag = item.get('random_weight_flag')
                instock = item.get('instock')
                promo_limit = item.get('promo_limit')
                product_unique_key = item.get('product_unique_key')
                multibuy_items_pricesingle = item.get('multibuy_items_pricesingle')
                perfect_match = item.get('perfect_match')
                servings_per_pack = item.get('servings_per_pack')
                warning = item.get('warning')
                suitable_for = item.get('suitable_for')
                standard_drinks = item.get('standard_drinks')
                environmental = item.get('environmental')
                grape_variety = item.get('grape_variety')
                retail_limit = item.get('retail_limit')

                product_description = re.sub(r'<.*?>', '', product_description).replace('\n', '')
                product_description = re.sub(r'\s+', ' ', product_description).strip()
                instructions=re.sub(r'\s+', ' ', instructions).strip()
                ingredients=re.sub(r'\s+', ' ', ingredients).strip()
                
                row = {
                    'unique_id': unique_id,
                    'competitor_name': competitor_name,
                    'store_name': store_name,
                    'store_addressline1': store_addressline1,
                    'store_addressline2': store_addressline2,
                    'store_suburb': store_suburb,
                    'store_state': store_state,
                    'store_postcode': store_postcode,
                    'store_addressid': store_addressid,
                    'extraction_date': extraction_date,
                    'product_name': product_name,
                    'brand': brand,
                    'brand_type': brand_type,
                    'grammage_quantity': grammage_quantity,
                    'grammage_unit': grammage_unit,
                    'drained_weight': drained_weight,
                    'producthierarchy_level1': producthierarchy_level1,
                    'producthierarchy_level2': producthierarchy_level2,
                    'producthierarchy_level3': producthierarchy_level3,
                    'producthierarchy_level4': producthierarchy_level4,
                    'producthierarchy_level5': producthierarchy_level5,
                    'producthierarchy_level6': producthierarchy_level6,
                    'producthierarchy_level7': producthierarchy_level7,
                    'regular_price': regular_price,
                    'selling_price': selling_price,
                    'price_was': price_was,
                    'promotion_price': promotion_price,
                    'promotion_valid_from': promotion_valid_from,
                    'promotion_valid_upto': promotion_valid_upto,
                    'promotion_type': promotion_type,
                    'percentage_discount': percentage_discount,
                    'promotion_description': promotion_description,
                    'package_sizeof_sellingprice': package_sizeof_sellingprice,
                    'per_unit_sizedescription': per_unit_sizedescription,
                    'price_valid_from': price_valid_from,
                    'price_per_unit': price_per_unit,
                    'multi_buy_item_count': multi_buy_item_count,
                    'multi_buy_items_price_total': multi_buy_items_price_total,
                    'currency': currency,
                    'breadcrumb': breadcrumb,
                    'pdp_url': pdp_url,
                    'variants': variants,
                    'product_description': product_description,
                    'instructions': instructions,
                    'storage_instructions': storage_instructions,
                    'preparationinstructions': preparationinstructions,
                    'instructionforuse': instructionforuse,
                    'country_of_origin': country_of_origin,
                    'allergens': allergens,
                    'age_of_the_product': age_of_the_product,
                    'age_recommendations': age_recommendations,
                    'flavour': flavour,
                    'nutritions': nutritions,
                    'nutritional_information': nutritional_information,
                    'vitamins': vitamins,
                    'labelling': labelling,
                    'grade': grade,
                    'region': region,
                    'packaging': packaging,
                    'receipies': receipies,
                    'processed_food': processed_food,
                    'barcode': barcode,
                    'frozen': frozen,
                    'chilled': chilled,
                    'organictype': organictype,
                    'cooking_part': cooking_part,
                    'handmade': handmade,
                    'max_heating_temperature': max_heating_temperature,
                    'special_information': special_information,
                    'label_information': label_information,
                    'dimensions': dimensions,
                    'special_nutrition_purpose': special_nutrition_purpose,
                    'feeding_recommendation': feeding_recommendation,
                    'warranty': warranty,
                    'color': color,
                    'model_number': model_number,
                    'material': material,
                    'usp': usp,
                    'dosage_recommendation': dosage_recommendation,
                    'tasting_note': tasting_note,
                    'food_preservation': food_preservation,
                    'size': size,
                    'rating': rating,
                    'review': review,
                    'file_name_1': file_name_1,
                    'image_url_1': image_url_1,
                    'file_name_2': file_name_2,
                    'image_url_2': image_url_2,
                    'file_name_3': file_name_3,
                    'image_url_3': image_url_3,
                    'file_name_4': file_name_4,
                    'image_url_4': image_url_4,
                    'file_name_5': file_name_5,
                    'image_url_5': image_url_5,
                    'file_name_6': file_name_6,
                    'image_url_6': image_url_6,
                    'competitor_product_key': competitor_product_key,
                    'fit_guide': fit_guide,
                    'occasion': occasion,
                    'material_composition': material_composition,
                    'style': style,
                    'care_instructions': care_instructions,
                    'heel_type': heel_type,
                    'heel_height': heel_height,
                    'upc': upc,
                    'features': features,
                    'dietary_lifestyle': dietary_lifestyle,
                    'manufacturer_address': manufacturer_address,
                    'importer_address': importer_address,
                    'distributor_address': distributor_address,
                    'vinification_details': vinification_details,
                    'recycling_information': recycling_information,
                    'return_address': return_address,
                    'alchol_by_volume': alchol_by_volume,
                    'beer_deg': beer_deg,
                    'netcontent': netcontent,
                    'netweight': netweight,
                    'site_shown_uom': site_shown_uom,
                    'ingredients': ingredients,
                    'random_weight_flag': random_weight_flag,
                    'instock': instock,
                    'promo_limit': promo_limit,
                    'product_unique_key': product_unique_key,
                    'multibuy_items_pricesingle': multibuy_items_pricesingle,
                    'perfect_match': perfect_match,
                    'servings_per_pack': servings_per_pack,
                    'warning': warning,
                    'suitable_for': suitable_for,
                    'standard_drinks': standard_drinks,
                    'environmental': environmental,
                    'grape_variety': grape_variety,
                    'retail_limit': retail_limit
                }

                if writer is None:
                    writer = csv.DictWriter(file, fieldnames=row.keys())
                    writer.writeheader()
                
                writer.writerow(row)

        print(f"Data has been exported to {csv_file}")

if __name__ == "__main__":
    exporter = Export()
    exporter.start()

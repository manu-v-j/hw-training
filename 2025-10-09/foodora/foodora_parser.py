import requests
import re
import logging
from pymongo import MongoClient
from mongoengine.errors import NotUniqueError
from settings import headers,MONGO_URL,MONGO_DB,CATEGORY_ID
from foodora_item import Product_Item
logging.basicConfig(level=logging.INFO)

class Parser:

    def __init__(self):
        self.client=MongoClient(MONGO_URL)
        self.db=self.client[MONGO_DB]

    def start(self):
        for item in self.db[CATEGORY_ID].find():
            id=item.get('link')
            print(id)
            page=0
            while True:
                json_data = {
                    'query': '\n    \n    fragment ProductFields on Product {\n        attributes(keys: $attributes) {\n            key\n            value\n        }\n        activeCampaigns {\n            benefitQuantity\n            cartItemUsageLimit\n            description\n            discountType\n            discountValue\n            endTime\n            id\n            isAutoAddable\n            isBenefit\n            isTrigger\n            name\n            teaserFormat\n            totalTriggerThresholdFloat\n            triggerQuantity\n            type\n        }\n        badges\n        description\n        favourite\n        globalCatalogID\n        isAvailable\n        name\n        nmrAdID\n        originalPrice\n        packagingCharge\n        parentID\n        price\n        productBadges {\n            text\n            type\n        }\n        productID\n        stockAmount\n        stockPrediction\n        tags\n        type\n        urls\n        vendorID\n        weightableAttributes {\n            weightedOriginalPrice\n            weightedPrice\n            weightValue {\n                unit\n                value\n            }\n        }\n    }\n\n    \n    fragment PageInfoFieldsWithTotalCount on PageInfo {\n        isLast\n        pageNumber\n        totalCount\n    }\n\n\n    query getProducts(\n        $attributes: [String!]\n        $featureFlags: [FunWithFlag!]\n        $filters: [ProductFilterInput!]\n        $globalEntityId: String!\n        $isDarkstore: Boolean!\n        $locale: String!\n        $page: Int\n        $limit: Int\n        $userCode: String\n        $vendorCode: String!\n    ) {\n        products(\n            input: {\n                customerID: $userCode\n                filters: $filters\n                funWithFlags: $featureFlags\n                globalEntityID: $globalEntityId\n                isDarkstore: $isDarkstore\n                locale: $locale\n                page: $page\n                limit: $limit\n                platform: "web"\n                vendorID: $vendorCode\n            }\n        ) {\n            items {\n                ...ProductFields\n            }\n            pageInfo {\n                ...PageInfoFieldsWithTotalCount\n            }\n        }\n    }\n',
                    'variables': {
                        'attributes': [
                            'baseContentValue',
                            'baseUnit',
                            'freshnessGuaranteeInDays',
                            'maximumSalesQuantity',
                            'minPriceLastMonth',
                            'pricePerBaseUnit',
                            'sku',
                            'nutri_grade',
                            'sugar_level',
                        ],
                        'featureFlags': [
                            {
                                'key': 'pd-qc-weight-stepper',
                                'value': 'Variation1',
                            },
                        ],
                        'filters': [
                            {
                                'type': 'Category',
                                'id': id,
                            },
                        ],
                        'globalEntityId': 'MJM_AT',
                        'isDarkstore': False,
                        'locale': 'de_AT',
                        'page': page,
                        'vendorCode': 'jrii',
                    },
                }
                response = requests.post('https://mj.fd-api.com/api/v5/graphql', headers=headers, json=json_data)

                if response.status_code==200:
                    has_item=self.parse_item(response)
                    if not has_item:
                        break

                page+=1

    def parse_item(self,response):
        data=response.json()
        product_list=data.get('data',{}).get('products',{}).get('items',[])
        if not product_list:
            return False
        for item in product_list:
            product_name=item.get('name','')
            selling_price=item.get('originalPrice','')
            product_unique_key=item.get('productID','')
            product_description=item.get('description','')
            image_url=item.get('urls',[])
            attribute_list=item.get('attributes',[])
            price = ''
            unit = ''
            for attr in attribute_list:
                key = attr.get('key')
                value = attr.get('value', '')

                if key == 'pricePerBaseUnit':
                    if value:
                        try:
                            price = float(value)
                            price = f"{price:.2f}"  
                        except ValueError:
                            price = ''
                elif key == 'baseUnit':
                    unit = value

            if price and unit:
                price_per_unit = f"{price}€/{unit}"
            else:
                price_per_unit = ''

            #CLEAN
            grammage_quantity=''
            grammage_unit=''
            match = re.search(
                r'(?:(\d+)\s*[xX]\s*)?(\d+(?:[\.,]\d+)?)\s*(g|kg|ml|l|L|pcs|Pack)',
                product_name
            )

            if match:
                if match.group(1):  
                    grammage_quantity = f"{match.group(1)}x{match.group(2)}"
                else:               
                    grammage_quantity = match.group(2)
                grammage_unit = match.group(3)

            image_url=''.join(image_url)

            item={}
            item['product_name']=product_name
            item['selling_price']=selling_price
            item['regular_price']=selling_price
            item['currency']='EURO'
            item['grammage_quantity']=grammage_quantity
            item['grammage_unit']=grammage_unit
            item['product_unique_key']=product_unique_key
            item['product_description']=product_description
            item['price_per_unit']=price_per_unit
            item['image_url']=image_url

            product_item=Product_Item(**item)
            try:
                product_item.save()
            except NotUniqueError:
                print(f"Duplicate product_unique_key found")

            logging.info(item)

        return True


if __name__=='__main__':
    parser=Parser()
    parser.start()
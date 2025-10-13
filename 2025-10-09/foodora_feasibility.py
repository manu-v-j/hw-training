import requests

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'web',
    'apollographql-client-version': 'GROCERIES-MENU-MICROFRONTEND.25.41.0007',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.foodora.at',
    'perseus-client-id': '1759988484706.372479628381561427.vcfj48vujf',
    'perseus-session-id': '1759988484706.057910429491009975.627denqmdu',
    'platform': 'web',
    'priority': 'u=1, i',
    'referer': 'https://www.foodora.at/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-pd-language-id': '2',
    'x-requested-with': 'XMLHttpRequest',
}

category_list=['ccf1c672-92a4-45a6-aeec-b5c78a306d6e']
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
                        'id': 'ccf1c672-92a4-45a6-aeec-b5c78a306d6e',
                    },
                ],
                'globalEntityId': 'MJM_AT',
                'isDarkstore': False,
                'locale': 'de_AT',
                'page': 1,
                'vendorCode': 'jrii',
            },
        }

    response = requests.post('https://mj.fd-api.com/api/v5/graphql', headers=headers, json=json_data)
    data=response.json()
    product_list=data.get('data',{}).get('products',{}).get('items',[])
    if not product_list:
        break
    for item in product_list:
        product_name=item.get('name','')
        selling_price=item.get('originalPrice','')
        product_unique_key=item.get('productID','')
        product_description=item.get('description','')
        image_url=item.get('urls',[])
        attribute_list=item.get('attributes',[])
        for attr in attribute_list:
            if attr.get('key')=='pricePerBaseUnit':
                price_per_unit=attr.get('value','')
        print(selling_price)

    page+=1



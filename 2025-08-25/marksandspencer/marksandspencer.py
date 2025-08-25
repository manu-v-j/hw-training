import pandas as pd
import re,csv

df = pd.read_csv(
    '/home/toshiba/Hashwave/2025-08-25/marksandspencer/marksandspencer-com-2025-08-25-2.csv')

df=df.drop(columns=['web-scraper-order','web-scraper-start-url','pagination-selector','data-page-selector','Fit-0'])
df=df.rename(columns={
    'data-page-selector-href':'pdp_url',
    'Product-Brand-name-0':'brand',
    'Product-Offer-UnitPriceSpecification-price-0':'selling_price',
    'Product-description-0':'product_description',
    'Product-name-0':'product_name',
    'Product Code-0':'unique_id',
    'Colour-0':'color',
})


df['selling_price']=(df['selling_price'].astype(str).str.replace('£','',regex=False).astype(float).map(lambda x: f"{x:.2f}"))
df['unique_id']=df['unique_id'].astype(str).str.replace('Product code: ','',regex=False)
# df['breadcrumb'] = df['breadcrumb'].astype(str).apply(
#     lambda x: ' > '.join(re.findall(r"[A-Z][a-zA-Z']*", x))
# )

df['currency']='£'

df=df[['unique_id','product_name','brand','product_description','selling_price','currency','pdp_url','color']]
df.to_csv('marksandspencer_20250825.csv',  index=False, encoding='utf-8')

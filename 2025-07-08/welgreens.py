import pandas as pd
import re
import json

df = pd.read_csv('/home/user/Hashwave/2025-07-08/walgreens.csv')
df['image_url-src'] = df['image_url-src'].str.replace(r'^//', 'https://', regex=True)
df['breadcrumbs']=df['breadcrumbs'].str.replace('""','"')
df['breadcrumbs'] = df['breadcrumbs'].map(lambda x: ' > '.join(d['breadcrumbs'] for d in json.loads(x)) if pd.notnull(x) else x)
df['warning']=df['warning'].str.replace('""','"')

df['warning'] = df['warning'].map(lambda x: ' > '.join(d['warning'] for d in json.loads(x)) if pd.notnull(x) else x)

def parse_spec(val):
    try:
        val = json.loads(val.replace('""', '"').replace("'", '"'))
        spec = val[0].get('product_specification', '')
        return re.sub(r'(?<=[a-z])(?=[A-Z])', '\n', spec) 
    except:
        return val

df['product_specification'] = df['product_specification'].apply(parse_spec)
def clean_selling_price(val):
    if pd.isnull(val):
        return val
    match = re.search(r'\$\d+(?:\.\d{2})?', val)
    return match.group(0) if match else val

df['selling_price'] = df['selling_price'].apply(clean_selling_price)
df['regular_price']=df['selling_price'] 
print(df['warning'])

df.to_csv('cleaned_walgreens.csv', index=False)

import pandas as pd
import re

df = pd.read_csv('/home/user/Hashwave/2025-07-23/2xlhome .csv')
df.columns = df.columns.str.strip().str.replace('-', '_').str.replace(' ', '_')

df['selling_price'] = df['regular_price'].str.extract(r'Special\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['selling_price'] = df['selling_price'].str.replace(',', '', regex=True).astype(float).apply(lambda x: f"{x:.2f}")

df['regular_price_clean'] = df['regular_price'].str.extract(r'Regular\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['regular_price_clean'] = df['regular_price_clean'].str.replace(',', '', regex=True).astype(float).apply(lambda x: f"{x:.2f}")

df['breadcrumbs'] = df['breadcrumbs'].fillna('').apply(lambda x: x if '>' in x else ' > '.join(x.split(' ', 1)))

df.rename(columns={
    'premotion_description': 'promotion_description',
    'product_liink_href': 'url',  
    'image_src': 'image'
}, inplace=True)
df['promotion_description'] = df['promotion_description'].str.replace(r"\((.*?)\)", r"\1", regex=True)
df.drop(columns=['regular_price', 'web_scraper_order', 'web_scraper_start_url', 'product_liink'], errors='ignore', inplace=True)

df_final = df[['url', 'product_name', 'selling_price', 'regular_price_clean', 'breadcrumbs',
               'promotion_description', 'image', 'product_description']].copy()

df_final.rename(columns={'regular_price_clean': 'regular_price'}, inplace=True)

df_final = df_final.head(50)

output_file = '/home/user/Hashwave/2025-07-23/2xlhome_clean.csv'
df_final.to_csv(output_file, index=False)


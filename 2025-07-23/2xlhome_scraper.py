import pandas as pd
import re

df = pd.read_csv('/home/user/Hashwave/2025-07-23/2xlhome.csv')
df.columns = df.columns.str.strip().str.replace('-', '_').str.replace(' ', '_')

df['selling_price'] = df['regular_price'].str.extract(r'Special\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['selling_price'] = df['selling_price'].str.replace(',', '', regex=True).astype(float).apply(lambda x: f"{x:.2f}")

df['regular_price_clean'] = df['regular_price'].str.extract(r'Regular\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['regular_price_clean'] = df['regular_price_clean'].str.replace(',', '', regex=True).astype(float).apply(lambda x: f"{x:.2f}")

df['breadcrumbs'] = df['breadcrumbs'].fillna('').apply(lambda x: x if '>' in x else ' > '.join(x.split(' ', 1)))
df['product_description'] = df['product_description'].fillna('').apply(lambda x: re.sub(r'\s+', ' ', x))
df['product_description'] = df['product_description'].apply(lambda x: re.sub(r'(Height \(cm\):|Width \(cm\):|Colour:|Color:|Material:|Length \(cm\):|Care\s*:)', r', \1', x).strip(', '))


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


#scraper sitemap
# {"_id":"2xlhome","startUrl":["https://2xlhome.com/ae-en/kids","https://2xlhome.com/ae-en/kids/kids-bathroom","https://2xlhome.com/ae-en/kids/kids-soft-furnishing"],
#  "selectors":[{"id":"product_liink","parentSelectors":["_root"],"type":"SelectorLink","selector":".slick-dotted .slick-current a","multiple":true,"linkType":"linkFromHref"},
#               {"id":"product_name","parentSelectors":["product_liink"],"type":"SelectorText","selector":"span[itemprop='name']","multiple":false,"regex":""},
#               {"id":"regular_price","parentSelectors":["product_liink"],"type":"SelectorText","selector":"div.product-info-price","multiple":false,"regex":""},
#               {"id":"breadcrumbs","parentSelectors":["product_liink"],"type":"SelectorText","selector":"div.breadcrumbs","multiple":false,"regex":""},
#               {"id":"image","parentSelectors":["product_liink"],"type":"SelectorImage","selector":".mt-thumb-switcher img[itemprop='image']","multiple":false},
#               {"id":"product_description","parentSelectors":["product_liink"],"type":"SelectorText","selector":".detail-acc .collapsibleContent > div","multiple":true,"regex":""},
#               {"id":"premotion_description","parentSelectors":["product_liink"],"type":"SelectorText","selector":".discount-wrapper span.active","multiple":false,"regex":""}]}
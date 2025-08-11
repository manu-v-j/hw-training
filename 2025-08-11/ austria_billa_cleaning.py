import pandas as pd
import re
df = pd.read_csv("/home/toshiba/Hashwave/2025-08-11/DataHut_AT_Billa_PriceExtractions_20250806.csv")
df["regular_price"] = df["regular_price"].replace("", pd.NA) 
df["regular_price"] = df["regular_price"].fillna(df["selling_price"])

df['regular_price'] = df['regular_price'].astype(float).apply(lambda x: f"{x:.2f}")
df['selling_price'] = df['selling_price'].astype(float).apply(lambda x: f"{x:.2f}")

print(df[['regular_price', 'selling_price']].tail())

print(df[['regular_price', 'selling_price']].dtypes)
df['price_per_unit'] = df['price_per_unit'].str.replace(',', '', regex=False)
df["breadcrumb"] = df["breadcrumb"].replace("", pd.NA)
empty_breadcrumb_count = df["breadcrumb"].isna().sum()

keywords_one = [
    "Teebeutel Packung",
    "Teebeutel",
    "Beutel",
    "Btl",
    "Teebeutel Karton",
    "Teebeutel Paket",
    "Packung Beutel"
]
df.loc[df['site_shown_uom'].isin(keywords_one), 'grammage_unit'] = 'btl'
keywords_two = ["Portion Packung", "ANW"]
df.loc[df['site_shown_uom'].isin(keywords_one), 'grammage_unit'] = 'stuck'
keywords_three = ["wg", "Waschgänge"]
df.loc[df['site_shown_uom'].isin(keywords_three), 'grammage_unit'] = 'stuck'
df['competitor_name']=df['competitor_name'].replace('billaa','billa',regex=False)
df['currency']=df['currency'].replace('eur','EUR',regex=False)

df.to_csv("/home/toshiba/Hashwave/2025-08-11/DataHut_AT_Billa_PriceExtractions_20250811.csv", index=False)

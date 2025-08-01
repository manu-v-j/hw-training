import pandas as pd
import re

df = pd.read_csv('/home/user/Hashwave/2025-08-01/robertsbrothers_site.csv')
df = df.drop(columns=['web-scraper-order', 'web-scraper-start-url', 'agent_link','website'])
df = df.rename(columns={'agent_link-href': 'profile_url','website-href':'website'})
df['name'] = df['name'].str.split('\n').str[0].str.strip()
df['description'] = df['description'].str.replace('\n', ' ', regex=False).str.strip()
df['description'] = (df['description'].str.replace('\n', ' ', regex=False).str.replace(r'\s+', ' ', regex=True).str.strip()                               
)
df['address'] = df['address'].str.replace('\n', ' ', regex=False).str.strip()
df['country']='US'
df_final = df[['title', 'address', 'profile_url', 'description', 'name',
               'website', 'agent_phone_numbers', 'country']].copy()

print(df_final['title'])
df=df_final.to_json("ewm.json", orient="records", lines=True)

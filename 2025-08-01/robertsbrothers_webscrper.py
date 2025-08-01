import pandas as pd
import re
import json

df = pd.read_csv('/home/user/Hashwave/2025-08-01/robertsbrothers_site.csv')
df = df.drop(columns=['web-scraper-order','website'])
df = df.rename(columns={'web-scraper-start-url': 'profile_url','website-href':'website'})
df['name'] = df['name'].str.split('\n').str[0].str.strip()
df['description'] = df['description'].str.replace('\n', ' ', regex=False).str.strip()
df['description'] = (df['description'].str.replace('\n', ' ', regex=False).str.replace(r'\s+', ' ', regex=True).str.strip()                               
)
df['address'] = df['address'].str.replace('\n', ' ', regex=False).str.strip()
df['country']='US'
df_final = df[['title', 'address', 'profile_url', 'description', 'name',
               'website', 'agent_phone_numbers', 'country']].copy()

data = df_final.to_json("robertsbrothers.json", orient="records", lines=True)

result = []
with open(data, 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

# Print as a list of dicts
print(result)
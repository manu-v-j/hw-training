import pandas as pd
import re
import json

df = pd.read_csv('/home/user/Hashwave/2025-07-23/2xlhome.csv')
df.columns = df.columns.str.strip().str.replace('-', '_').str.replace(' ', '_')
import re
# Extract discount percent

# Extract Special Price
df['special_price'] = df['regular_price'].str.extract(r'Special\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['special_price'] = df['special_price'].str.replace(',', '', regex=True).astype(float)

df['original_price']=df['special_price']
# Extract Original Price
df['original_price'] = df['regular_price'].str.extract(r'Regular\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['original_price'] = df['original_price'].str.replace(',', '', regex=True).astype(float)
df['regular_price']=df['original_price']
# Print cleaned info

df.drop(columns=['regular_price'], inplace=True)

output_file = '/home/user/Hashwave/2025-07-23/2xlhome_clean.csv'
df.to_csv(output_file, index=False)
print(f"\n✅ Cleaned data saved to: {output_file}")


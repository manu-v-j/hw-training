import pandas as pd
import re
import json

df = pd.read_csv('/home/user/Hashwave/2025-07-23/2xlhome.csv')
df.columns = df.columns.str.strip().str.replace('-', '_').str.replace(' ', '_')
import re
# Extract discount percent

df['selling_price'] = df['regular_price'].str.extract(r'Special\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['selling_price'] = df['selling_price'].str.replace(',', '', regex=True).astype(float)

# Extract Original Price (regular price)
df['regular_price_clean'] = df['regular_price'].str.extract(r'Regular\s*Price\s*AED\s*([\d,]+)', flags=re.IGNORECASE)
df['regular_price_clean'] = df['regular_price_clean'].str.replace(',', '', regex=True).astype(float)

# Extract promotion description
df['promotion_description'] = df['premotion_description']

# Add URL and image columns
df['url'] = df['product_liink_href']
df['image'] = df['image_src']

# Drop unnecessary columns
df.drop(columns=['regular_price', 'web_scraper_order', 'web_scraper_start_url', 'product_liink', 'premotion_description'], inplace=True)

# Reorder columns
df_final = df[['url', 'product_name', 'selling_price', 'regular_price_clean', 'breadcrumbs',
               'promotion_description', 'image', 'product_description']]

# Rename columns for clarity
df_final.rename(columns={'regular_price_clean': 'regular_price'}, inplace=True)

# Save final cleaned CSV
output_file = '/home/user/Hashwave/2025-07-23/2xlhome_clean.csv'
df_final.to_csv(output_file, index=False)

print(f"\n✅ Cleaned data saved to: {output_file}")
print(df_final.head())
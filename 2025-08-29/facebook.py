import pandas as pd
file_one="/home/toshiba/Hashwave/2025-08-29/morrisons.csv"
file_two="/home/toshiba/Hashwave/2025-08-29/sainsbury.csv"

df1=pd.read_csv(file_one)
df2=pd.read_csv(file_two)

df=pd.concat([df1,df2],ignore_index=True)
df['Post Date/Time'] = pd.to_datetime(df['Post Date/Time'], utc=True)
df['Post Text/Caption']=(df['Post Text/Caption'].astype(str).str.replace(r'\s+', ' ', regex=True).str.strip())
df.to_csv("facebook_20250829.csv",index=False)
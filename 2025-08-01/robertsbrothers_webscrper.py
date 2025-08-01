import pandas as pd
import re

df = pd.read_csv('/home/user/Hashwave/2025-08-01/robertsbrothers.csv')
df=df.to_json("ewm.json", orient="records", lines=True)
print(df)
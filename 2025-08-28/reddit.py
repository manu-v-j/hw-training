import pandas as pd

file1 = "/home/toshiba/Hashwave/2025-08-28/reddit_tesco.csv"
file2 = "/home/toshiba/Hashwave/2025-08-28/reddit_morrisons.csv"
file3 = "/home/toshiba/Hashwave/2025-08-28/reddit_sainsburys.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

df_combined = pd.concat([df1, df2, df3], ignore_index=True)

df_combined.to_csv("/home/toshiba/Hashwave/2025-08-28/reddit_20250828.csv", index=False)

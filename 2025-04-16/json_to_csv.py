import csv
import json

json_file_path="/home/user/Hashwave/2025-04-16/products.json"
csv_file_path="/home/user/Hashwave/2025-04-16/products_converted.csv"

with open(json_file_path,'r') as json_file:
    data=json.load(json_file)

header=list(data[0].keys())

with open(csv_file_path,'w') as csv_file:
    writer=csv.DictWriter(csv_file,header)
    writer.writeheader()
    writer.writerows(data)

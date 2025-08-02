import csv
import json

csv_file_path='/home/user/Hashwave/2025-04-16/products.csv'
json_file_path='/home/user/Hashwave/2025-04-16/products.json'

with open (csv_file_path,'r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    data=list(csv_reader)

with open(json_file_path,'w') as json_file:
    json.dump(data,json_file)
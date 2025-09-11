import os
from datetime import date


folder_name = str(date.today())
os.makedirs(folder_name, exist_ok=True)
log_file_path = os.path.join(folder_name,"training.log")


with open(log_file_path,"w") as file:
    file.write("")
    
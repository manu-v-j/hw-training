import os
from datetime import date, datetime

base_dir = "/home/toshiba/Hashwave"
folder_name = str(date.today())
folder_path = os.path.join(base_dir, folder_name)

os.makedirs(folder_path, exist_ok=True)

log_file_path = os.path.join(folder_path, "training.log")

with open(log_file_path, "w") as file:
    file.write(f"Folder created on {datetime.now()}\n")

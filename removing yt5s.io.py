import os
import shutil

os.chdir("/Users/zeeshanwaheed/Downloads")

for file in os.listdir():
    if not file.startswith("yt5s.io"):
        continue
    splitting = file.split("- ")
    splitting.remove(splitting[0])
    new_name = f"{splitting[0]}"
    os.rename(file, new_name)


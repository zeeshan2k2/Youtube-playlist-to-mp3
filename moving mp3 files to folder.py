import os
from pathlib import Path
import shutil
import time

n = input(str("what do you want to name your file : "))

os.chdir("/Users/zeeshanwaheed/Downloads")

Path(n)

if not os.path.exists(n):
    os.mkdir(n)

for file in os.listdir():
    if not file.startswith("yt5s.io"):
        continue
    shutil.move(file, n)


os.chdir(n)
for file in os.listdir():
    if not file.startswith("yt5s.io"):
        continue
    splitting = file.split("yt5s.io - ")
    splitting.remove(splitting[0])
    new_name = f'{splitting[0]}'
    os.rename(file, new_name)

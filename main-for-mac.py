from pytube import Playlist
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from datetime import datetime, timedelta
import os
import shutil
from pathlib import Path

# note that the playlist link you enter here must be public or else the program will give an error
print("The playlist link you copy must be public or else it will give an error")
playlist_link = input("Enter the link of the playlist: ")

# taking filename as an input
file_name = input(str("what would you like to name your file : "))

# getting links of all videos in the playlist
video_links = Playlist(playlist_link).video_urls

length = len(video_links)
print()
print("There are", length, "videos in this playlist.")
print()

# this is to note time
start_time = time.monotonic()


# a function that'll add adblocker to chrome driver and then download all the mp3s one by one
def dowmp3():
    chrome_options = ChromeOptions()
    chrome_options.add_extension("adguard.crx")

    print("Please wait the download will begin shortly...")
    print()

    browser = webdriver.Chrome("./chromedriver", options=chrome_options)

    time.sleep(14)

    n = 0

    for i in video_links:
        browser.get("https://yt5s.io/en20/youtube-to-mp3")

        button0 = browser.find_element_by_xpath('//input[@id="s_input"]')
        time.sleep(0.2)       # this is really important takes into account how many secs it will take to load the page

        button0.send_keys(i)

        button = browser.find_element_by_xpath('//button[@class="btn-red"]')
        button.click()

        time.sleep(2.5)     # this is really important takes into account how many secs it will take to load the button

        button1 = browser.find_element_by_xpath('//button[@id="btn-action"]')
        button1.click()

        time.sleep(2.5)     # this is really important takes into account how many secs it will take to load the button

        button2 = browser.find_element_by_link_text("Download")
        button2.click()

        n = n + 1
        # this works as a progress bar updates with how many have been downloaded from the playlist
        print(n, "out of", length, "done")

    print("Please wait it will be downloaded shortly...")

    time.sleep(10)    # this is the more than time taken to finish the last download to prevent it from error


dowmp3()
print()
print("downloaded mp3 version of youtube playlist successfully")
print()

end_time = time.monotonic()

# this will move all mp3 files to a folder and then rename the file(removing the yt5s.io) from all mp3 file names
os.chdir("/Users/zeeshanwaheed/Downloads")
Path(file_name)

if not os.path.exists(file_name):
    os.mkdir(file_name)

for file in os.listdir():
    if not file.startswith("yt5s.io"):
        continue
    shutil.move(file, file_name)

os.chdir(file_name)
for file in os.listdir():
    if not file.startswith("yt5s.io"):
        continue
    splitting = file.split("yt5s.io - ")
    splitting.remove(splitting[0])
    new_name = f'{splitting[0]}'
    os.rename(file, new_name)

# tells us how much time it took to download and rename the files.
print()
print("It took ", timedelta(seconds=end_time - start_time), "to download", length, "songs")

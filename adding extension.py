from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser
import time

chrome_options = ChromeOptions()
chrome_options.add_extension("adguard.crx")

browser = webdriver.Chrome("./chromedriver", options=chrome_options)

time.sleep(10.8)


def dowmp3(n):
    browser.get("https://yt5s.io/en20/youtube-to-mp3")

    button0 = browser.find_element_by_xpath('//input[@id="s_input"]')
    # time.sleep(5)
    button0.send_keys(n)

    button = browser.find_element_by_xpath('//button[@class="btn-red"]')
    button.click()

    time.sleep(1)

    button1 = browser.find_element_by_xpath('//button[@id="btn-action"]')
    button1.click()

    time.sleep(1.5)

    button2 = browser.find_element_by_link_text("Download")
    button2.click()

dowmp3("https://youtu.be/8aRCmMlCcY0")
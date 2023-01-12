from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import time
import webbrowser


browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get("https://yt5s.io/en20/youtube-to-mp3")

# time.sleep(2)

button0 = browser.find_element_by_xpath('//input[@id="s_input"]')
button0.send_keys("https://youtu.be/8aRCmMlCcY0")

button = browser.find_element_by_xpath('//button[@class="btn-red"]')
button.click()

time.sleep(5)

button1 = browser.find_element_by_xpath('//button[@id="btn-action"]')
button1.click()

time.sleep(5)

button2 = browser.find_element_by_link_text("Download")
button2.click()




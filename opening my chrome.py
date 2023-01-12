import webbrowser
from selenium import webdriver


path = "/Applications/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.w3schools.com/")




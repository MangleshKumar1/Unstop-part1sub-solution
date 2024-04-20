#  linkedin_scraper
import pandas as pd
import time
import random
import requests
from time import sleep
from bs4 import BeautifulSoup
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
opts = Options()
import csv

driver = webdriver.Chrome(options=opts, executable_path= "chromedriver")

# function to ensure all key data fields have a value
def validate_field(field):
# if field is present pass if field:
if field:
pass
# if field is not present print text else:
else:
field = 'No results'
return field


# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
#locate email form by_class_name
username = driver.find_element(By.ID, "session_key")
# send keys(0) to simulate keystrokes
username.send_keys ("*****@gmail.com")
# sleep for 0.5 seconds
sleep(0.5)
# locate password form by_class_name
password = driver.find_element(By.ID,'session_password')
# send keys() to simulate key strokes
password.send_keys('*******')
sleep(0.5)
# locate submit button by xpath
sign_in_button = driver.find_element(By.XPATH,'//* [@type="submit"]')
# . click() to mimic button click
sign_in_button.click()
sleep(10)


# Task 2: Search for the profile we want to crawl

# Task 2.1: Locate the search bar element
search_field = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
# Task 2.2: Input the search query to the search bar
# search_query = input('What profile do you want to scrape? ')
search_field.send_keys('Python Developers')
# Task 2.3: Search
search_field.send_keys(Keys.RETURN)
# locate Peoples button by xpath
people = driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
# . click() to mimic button click
people.click()
sleep(2)


# Task 3: Scrape the URLs of the profiles
profiles = driver.find_elements(By.CLASS_NAME, 'app-aware-link')
all_profile_URL = []
for profile in profiles:
profile_ID = profile.get_attribute('href')
profile_URL = "https://www.linkedin.com" + profile_ID
if profile_URL not in all_profile_URL:
all_profile_URL.append(profile_URL)

print('- Finish Task 3: Scrape the URLs')
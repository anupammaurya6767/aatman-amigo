#login_insta.py 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def login(driver, username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    # Log in
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(4)

    # Accept cookies
    driver.find_element_by_xpath('//button[text()="Accept"]').click()
    time.sleep(2)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def insta_send_message(username, message):
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(2)
    driver.find_element_by_xpath("//a[contains(@href,'/direct/t/')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//textarea[@placeholder='Message...']").send_keys(message)
    driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()

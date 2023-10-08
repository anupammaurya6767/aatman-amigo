#login_insta.py 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# options = Options()
# options.add_argument("--headless=new")

# driver = webdriver.Chrome(options=options)

def login(driver, username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(10)

    # Log in
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(10)

    # Accept cookies
    # driver.find_element(By.XPATH, '//button[text()="Accept"]').click()
    # time.sleep(2)
    
    # saving login info
    driver.find_element(By.CLASS_NAME, "_acan").click()
    time.sleep(10)
    
    # notifications
    driver.find_element(By.CLASS_NAME, '_a9_1').click()
    time.sleep(3)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def send_message(driver, recipient, message):
    try:
        driver.get(f"https://www.instagram.com/{recipient}/")
        time.sleep(10)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]').click()
        time.sleep(7)
        textarea_element = driver.find_element(By.CSS_SELECTOR, '[aria-label="Message"]').send_keys(message)
        submit_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")
        submit_button.click()
        return "Message sent successfully."
    except Exception as e:
        return f"Error sending message: {str(e)}"

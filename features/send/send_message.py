from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

 def send_message(driver, recipient, message):
        try:
            driver.get(f"https://www.instagram.com/{recipient}/")
            time.sleep(2)
            driver.find_element_by_xpath("//a[contains(@href,'/direct/t/')]").click()
            time.sleep(2)
            textarea_element = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
            textarea_element.send_keys(message)
            submit_button = driver.find_element_by_xpath("//button[contains(@type,'submit')]")
            submit_button.click()
            return "Message sent successfully."
        except Exception as e:
            return f"Error sending message: {str(e)}"

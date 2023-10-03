from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

 def send_sticker(driver, recipient, sticker_url):
        try:
            driver.get(f'https://www.instagram.com/direct/t/{recipient}/')
            time.sleep(2)
            driver.execute_script(f'window.open("{sticker_url}", "_blank");')
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
            submit_button.click()
            driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            return "Sticker sent successfully."
        except Exception as e:
            return f"Error sending sticker: {str(e)}"

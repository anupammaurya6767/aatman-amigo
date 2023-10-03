from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def send_video(driver, recipient, video_path):
        try:
            driver.get(f'https://www.instagram.com/direct/t/{recipient}/')
            time.sleep(2)
            video_input = driver.find_element_by_xpath('//input[@accept="video/mp4,video/x-m4v,video/*"]')
            video_input.send_keys(video_path)
            time.sleep(2)
            submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
            submit_button.click()
            return "Video sent successfully."
        except Exception as e:
            return f"Error sending video: {str(e)}"

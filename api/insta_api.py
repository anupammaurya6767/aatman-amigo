from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from features.login.login_insta import login
from features.send.send_message import send_message
from utils.constants import DRIVER_PATH


class AatmanAmigo:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    def login(self, username, password):
        
        login(self.driver, username, password)
    
    def send_message(self, recipient, message):
        send_message(self.driver, recipient, message)


    def close(self):
        self.driver.quit()

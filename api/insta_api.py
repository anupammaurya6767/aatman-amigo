from selenium import webdriver
from features.login.login_whatsapp import login_insta
from features.send.send_message import send_message
from features.send.send_video import send_video
from features.send.send_image import send_image
from features.send.send_sticker import send_sticker
from features.receive.receive_message import receive_message

class InstaAPI:
    def __init__(self, driver_path, username, password):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.username = username
        self.password = password

    def login(self):
        login_insta(self.driver, self.username, self.password)

    def send_message(self, recipient, message):
        send_message(self.driver, recipient, message)

    def send_video(self, recipient, video_path):
        send_video(self.driver, recipient, video_path)

    def send_image(self, recipient, image_path):
        send_image(self.driver, recipient, image_path)

    def send_sticker(self, recipient, sticker_url):
        send_sticker(self.driver, recipient, sticker_url)

    def receive_messages(self):
        return receive_message(self.driver)

    def close(self):
        self.driver.quit()

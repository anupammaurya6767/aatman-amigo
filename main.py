from api.insta_api import AatmanAmigo
from utils.constants import username, password
import configparser
import time

# Initialize the AatmanAmigo API
insta_api = AatmanAmigo()

try:
    config = configparser.ConfigParser()
    # Read the existing configuration file, if it exists.
    # Prompt the user for the values of the configuration parameters.
    print("Credentials are not saved anywhere, dw ;)")
    username = input('Enter your Instagram username: ')
    password = input('Enter your Instagram password: ')
    # Login to Instagram
    insta_api.login(username=username, password=password)

    # Send a message
    recipient = input("Enter the recipient's username: ")
    message = input("Enter the message to send: ")
    insta_api.send_message(recipient, message)

    # ===>IMAGE FeATURE NOT WORKING
    # # Send an image
    # recipient = input("Enter the recipient's username: ")
    # image_path = input("Enter the path to the image to send\n(U may drag and drop the image): ")
    # insta_api.send_image(recipient, image_path)


except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the API
    time.sleep(2)
    insta_api.close()
    # print("Hogya Scene")

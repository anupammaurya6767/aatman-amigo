from api.insta_api import AatmanAmigo
from utils.constants import username, password

# Initialize the AatmanAmigo API
insta_api = AatmanAmigo()

try:
    # Login to Instagram
    insta_api.login(username=username, password=password)

    # Send a message
    recipient = "your recipient"
    message = "Hello, Instagram!"
    insta_api.send_message(recipient, message)

    # Send an image
    recipient = "tanjiro_0_3"
    image_path = "/Users/aditya/Downloads/d.png"
    insta_api.send_image(recipient, image_path)


except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the API
    insta_api.close()

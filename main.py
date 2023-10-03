from api.insta_api import AatmanAmigo

# Your Instagram credentials
username = "your_username"
password = "your_password"

# Initialize the AatmanAmigo API
insta_api = AatmanAmigo(driver_path="path/to/chromedriver.exe", username=username, password=password)

try:
    # Login to Instagram
    insta_api.login()

    # Send a message
    recipient = "recipient_username"
    message = "Hello, Instagram!"
    insta_api.send_message(recipient, message)

    # Send an image
    recipient = "recipient_username"
    image_path = "path/to/image.jpg"
    insta_api.send_image(recipient, image_path)

    # Send a sticker
    recipient = "recipient_username"
    sticker_url = "https://example.com/your-sticker.png"
    insta_api.send_sticker(recipient, sticker_url)

    # Send a video
    recipient = "recipient_username"
    video_path = "path/to/video.mp4"
    insta_api.send_video(recipient, video_path)

    # Receive and print messages
    insta_api.get_messages(username, password)

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the API
    insta_api.close()

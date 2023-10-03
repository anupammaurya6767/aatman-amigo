# receive_message.py
import requests
import json

def get_messages(username, password):
    url = "https://i.instagram.com/api/v1/direct_v2/inbox/"

    headers = {
        "user-agent": "Instagram 126.0.0.25.122 Android (24/7.0; 640dpi; 144.0 L; samsung; SM-G935F; herolte; samsungexynos8890) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36",
        "accept-language": "en-US",
        "accept-encoding": "gzip, deflate, br",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": f"sessionid={username}",
    }

    data = {
        "password": password,
        "username": username,
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        inbox = json_response["inbox"]
        threads = inbox["threads"]

        for thread in threads:
            items = thread["items"]

            for item in items:
                if "text" in item:
                    print(f"{thread['users'][0]['username']}: {item['text']}")

# get_messages("your_username", "your_password")

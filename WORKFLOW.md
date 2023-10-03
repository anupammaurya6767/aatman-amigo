# Aatman Amigo
Insta_api<br />
├── 📁 api/<br/>
│ ├── 📄 insta_api.py # Main API script<br/>
│ └── 📄 init.py<br/>
│
├── 📁 drivers/<br/>
│ ├── ⚙️ chromedriver.exe # Chrome WebDriver executable (or appropriate for your browser)<br/>
│ └── ⚙️ geckodriver.exe # Gecko WebDriver executable for Firefox (if using Firefox)<br/>
│
├── 📁 utils/<br/>
│ ├── 📄 constants.py # Constants and configuration settings<br/>
│ ├── 📄 helpers.py # Helper functions for interacting with WhatsApp Web<br/>
│ └── 📄 init.py<br/>
│
├── 📁 features/<br/>
│ ├── 📁 login/<br/>
│ │ ├── 📄 login_insta.py # Module for logging into Insta Web<br/>
│ │ └── 📄 init.py<br/>
│ │
│ ├── 📁 send/<br/>
│ │ ├── 📄 send_message.py # Module for sending text messages<br/>
│ │ ├── 📄 send_image.py # Module for sending images<br/>
│ │ ├── 📄 send_video.py # Module for sending videos<br/>
│ │ └── 📄 init.py<br/>
│ │
│ ├── 📁 receive/<br/>
│ │ ├── 📄 receive_message.py # Module for receiving and processing messages<br/>
│ │ └── 📄 init.py<br/>
│ │
│ └── ... (other feature modules)<br/>
│
├── 📄 requirements.txt # List of required Python packages<br/>
│
└──  📄 main.py # Main script to run the Insta API<br/>



This structured project organization should help you manage different aspects of your Instagram API more effectively. Each module inside the `features` directory can handle specific functionalities like sending messages, images, videos, receiving messages, and logging in. You can develop and maintain these modules separately, making your codebase more organized and maintainable.

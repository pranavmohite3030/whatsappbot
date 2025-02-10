from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# List of contacts (saved in WhatsApp)
contacts = ["7058258664"]

# List of messages
messages = [
    "Hello! How are you doing today?",
    "Hey! Just checking in. Hope you’re doing great!",
    "Good day! Wishing you a wonderful time ahead!",
    "Hey there! Hope everything is going well!"
]

# Initialize WhatsApp Web in Chrome
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Pranav\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
)  # Change this to your Chrome profile path
options.add_argument("--profile-directory=Default")  # Use your default profile

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
input("Scan the QR code in WhatsApp Web, then press Enter...")  # Wait for manual login

def send_message(contact, message):
    """Send a message to a WhatsApp contact."""
    search_box = driver.find_element("xpath", '//div[@contenteditable="true"][@title="Search input textbox"]')
    search_box.clear()
    search_box.send_keys(contact)
    time.sleep(2)

    try:
        # Click on the contact
        contact_element = driver.find_element("xpath", f'//span[@title="{contact}"]')
        contact_element.click()
        time.sleep(2)

        # Type and send the message
        message_box = driver.find_element("xpath", '//div[@contenteditable="true"][@title="Type a message"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        print(f"Message sent to {contact}")
    except Exception as e:
        print(f"Failed to send message to {contact}: {e}")

# Send messages in the background
for contact in contacts:
    message = random.choice(messages)
    send_message(contact, message)
    time.sleep(random.randint(3, 7))  # Random delay

print("All messages sent successfully!")
driver.quit()

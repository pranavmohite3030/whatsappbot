import pyautogui
import time
import random
import subprocess

# List of contacts (Numbers should be saved in WhatsApp)
contacts = ["7058258664","8830975020"]           

# List of messages to send
messages = [
    "Hello! How are you doing today?",
    "Hey! Just checking in. Hope you’re doing great!",
    "Good day! Wishing you a wonderful time ahead!",
    "Hey there! Hope everything is going well!"
]

# Open WhatsApp Desktop
subprocess.run("start whatsapp:", shell=True)
time.sleep(5)  # Give WhatsApp time to open

def search_and_select_contact(contact):
    # Open search bar
    pyautogui.hotkey("ctrl", "f")  
    time.sleep(1)

    # Clear search bar
    pyautogui.hotkey("ctrl", "a")  
    pyautogui.press("backspace")  
    time.sleep(1)

    # Type contact number or name
    pyautogui.write(contact, interval=0.1)  
    time.sleep(2)  # Wait for WhatsApp to load the contact

    # Move the arrow down to highlight the contact (if it's visible in the search results)
    pyautogui.press("down")
    time.sleep(1)

    # Press Enter to select the contact and open the chat
    pyautogui.press("enter")  
    time.sleep(3)  # Wait for chat to open

def send_message(message):
    # Type the message in the message box
    pyautogui.write(message, interval=0.1)
    time.sleep(1)

    # Press Enter to send the message
    pyautogui.press("enter")  

# Sending messages one by one
for contact in contacts:
    try:
        print(f"Searching for {contact}...")

        # Search and select contact
        search_and_select_contact(contact)

        # Choose a random message to send
        message = random.choice(messages)
        send_message(message)

        print(f"Message sent to {contact}")

        # Add random delay before sending the next message
        delay = random.randint(3, 7)
        print(f"Waiting {delay} seconds before sending the next message...")
        time.sleep(delay)

    except Exception as e:
        print(f"Error sending message to {contact}: {e}")

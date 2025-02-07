# KeyLogger
This is a basic keylogger that captures and logs keystrokes to a file

# KeyLogger – Ethical Cybersecurity Research
## Disclaimer

### WARNING: This project is for educational and ethical cybersecurity research purposes only. Unauthorized use of keyloggers is illegal and may violate privacy laws. Ensure you have explicit permission before using this software. The author is not responsible for any misuse.

# About
This is a basic keylogger that captures and logs keystrokes to a file. It also includes:

- Encryption: Logs are encrypted using the Fernet encryption method.
- Email Logging (Optional): The script can send logs via email at specified intervals (disabled by default).
  
This tool is meant for learning how keyloggers work and understanding how to defend against them in a cybersecurity environment.

# Features:
- Logs keystrokes and stores them in a file
- Encrypts logs for security
- Supports email-based log reporting (optional)
- Runs in a separate thread

# How to use:
- Clone the repository
- Install dependencies:
  ```bash
  pip install pynput yagmail cryptography
  ```
- Configure email settings (Optional)
  ```bash
  EMAIL_ADDRESS = "your-email@gmail.com"
  EMAIL_PASSWORD = "your-password"
  EMAIL_RECEIVER = "receiver-email@gmail.com"
  EMAIL_SEND = False  # Change to True to enable email sending
  ```
- Run the Script:
  ```bash
  python KeyLogger.py
  ```

# Ethical Use Cases 
- Understanding how keyloggers work for penetration testing
- Learning how to detect and mitigate cybersecurity threats
- Personal projects in a controlled environment

# Do Not Use This For
- Spying on people without consent
- Stealing passwords or sensitive data
- Unauthorized monitoring of systems you do not own

# Legal Compliance
Using keyloggers without consent may violate laws such as:
- Computer Fraud and Abuse Act (CFAA) – USA
- General Data Protection Regulation (GDPR) – EU
- IT Act 2000 – India
  
Always get explicit permission before using this tool in any environment.

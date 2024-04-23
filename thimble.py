import tkinter as tk
from tkinter import messagebox
from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login(username, password):
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        driver.get("https://1xbet.com/")
        time.sleep(5)
        
        login_button = driver.find_element(By.XPATH, "//a[contains(text(),'Log in')]")
        login_button.click()
        time.sleep(3)
        
        username_input = driver.find_element(By.NAME, "login")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        if "https://1xbet.com/en/live/" in driver.current_url:
            print("Login successful!")
        else:
            print("Login failed. Please check your credentials.")
        
        driver.quit()
    except Exception as e:
        print("An error occurred during login:", e)

def on_login_click():
    username = username_entry.get()
    password = password_entry.get()
    Thread(target=login, args=(username, password)).start()

root = tk.Tk()
root.title("1xbet Login")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=on_login_click)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)
# 

root.mainloop()

import tkinter as tk
from tkinter import messagebox
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def login(username, password):
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        driver.get("https://1xbet.com/")
        driver.implicitly_wait(10)
        
        login_button = driver.find_element(By.XPATH, "//a[contains(text(),'Log in')]")
        login_button.click()
        
        time.sleep(2)
        
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        
        password_input.submit()
        
        driver.implicitly_wait(10)
        
        if "https://1xbet.com/en/live/" in driver.current_url:
            messagebox.showinfo("Login Successful", "Login successful!")
        else:
            messagebox.showerror("Login Failed", "Login failed. Please check your credentials.")
        
        driver.quit()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during login: {e}")

def on_login_click():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        login_button.config(state=tk.DISABLED)
        Thread(target=login, args=(username, password)).start()
    else:
        messagebox.showerror("Error", "Please enter both username and password.")

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

root.mainloop()

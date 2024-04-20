import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function to login to 1xbet
def login(driver):
    # Enter your credentials here (replace 'username' and 'password' with actual values)
    username = '0796562713'
    password = 'Marian2003'
    
    try:
        # Open the login page
        driver.get("https://1xbet.com/")
        time.sleep(5)  # Wait for the page to load
        
        # Click on the login button
        login_button = driver.find_element(By.XPATH, "//a[contains(text(),'Log in')]")
        login_button.click()
        time.sleep(3)  # Wait for the login page to load
        
        # Enter username and password
        username_input = driver.find_element(By.NAME, "login")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        
        # Wait for login to complete
        time.sleep(5)
        
        print("Login successful!")
        return True
    
    except Exception as e:
        print("An error occurred during login:", e)
        return False

# Function to play the thimble game
def play_game(driver):
    try:
        # Open the thimble game
        driver.get("https://1xbet.com/")
        time.sleep(5)  # Wait for the page to load
        
        # Click on the thimble game
        thimble_button = driver.find_element(By.XPATH, "//div[contains(text(),'Thimble')]")
        thimble_button.click()
        time.sleep(3)  # Wait for the game to load
        
        # Logic to play the game
        # (For demonstration, we won't interact with the game)
        print("Thimble game opened in a new tab.")
        print("You can manually interact with the game.")
        
    except Exception as e:
        print("An error occurred during playing the game:", e)

# Main function to display menu and handle user input
def main():
    print("Welcome to Thimble Game Automation Script")
    
    # Open the browser
    driver = webdriver.Chrome()
    
    # Flag to track if the user is logged in
    logged_in = False
    
    while True:
        print("\nOptions:")
        print("1. Log in to 1xbet")
        print("2. Play Thimble Game")
        print("3. Exit")
        
        option = input("Enter your choice (1, 2, or 3): ")
        
        if option == "1":
            if not logged_in:
                logged_in = login(driver)
            else:
                print("You are already logged in.")
        elif option == "2":
            if logged_in:
                play_game(driver)
            else:
                print("You need to log in first.")
        elif option == "3":
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")
    
    # Close the browser
    driver.quit()

# Call the main function
if __name__ == "__main__":
    main()

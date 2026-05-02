from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#function that fetches the details of the webpage
def webpage_details():
    #Initializing chrome driver
    driver = webdriver.Chrome()
    try:
        #opens webpage
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(2)

        #logins using find_element method by using ID
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        #Gets title of the webpage
        title = driver.title
        print("Title: ",title)

        # Gets the current url of the webpage
        current_url = driver.current_url
        print("Current URL: ",current_url)

        #Gets the content of the page
        page_content = driver.page_source

        #Saves to a text file
        with open("webpage_task.txt","w", encoding="utf-8") as file:
            file.write(page_content)

        print("Content saved successfully!")

    finally:
        driver.quit()

#invoking the function
webpage_details()

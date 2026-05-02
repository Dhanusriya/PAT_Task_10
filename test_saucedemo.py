from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# function that tests the valid login scenario - positive testcase
def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    assert "inventory" in driver.current_url
    assert "Swag Labs" in driver.title

    driver.quit()

# function that tests the invalid login scenario - negative testcase
def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error = driver.find_element(By.XPATH, "//h3").text
    assert "Epic sadface" in error

    driver.quit()
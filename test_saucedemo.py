import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


#  FIXTURE
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()


# ---------- TEST CASE 1: TITLE (POSITIVE) ----------
def test_title_positive(driver):
    assert "Swag Labs" in driver.title


# ---------- TEST CASE 2: TITLE (NEGATIVE) ----------
def test_title_negative(driver):
    assert "Flipkart" not in driver.title


# ---------- TEST CASE 3: HOMEPAGE URL (POSITIVE) ----------
def test_homepage_url_positive(driver):
    assert driver.current_url == "https://www.saucedemo.com/"


# ---------- TEST CASE 4: HOMEPAGE URL (NEGATIVE) ----------
def test_homepage_url_negative(driver):
    assert driver.current_url != "https://www.google.com/"


# ---------- TEST CASE 5: DASHBOARD URL (POSITIVE) ----------
def test_dashboard_url_positive(driver):
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    assert "inventory" in driver.current_url


# ---------- TEST CASE 6: DASHBOARD URL (NEGATIVE) ----------
def test_dashboard_url_negative(driver):
    # Login with correct creds
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Wrong expectation
    assert "dashboard" not in driver.current_url
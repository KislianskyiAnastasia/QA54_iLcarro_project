import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from login_helper import test_go_to_login

URL = "https://icarro-v1.netlify.app/search?page=0&size=10"
EXPECTED_URL= "https://icarro-v1.netlify.app/login"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()

def test_login_wrong_password(driver):
    test_go_to_login(driver)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Zxczxczxc1!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_massage = driver.find_element(By.CSS_SELECTOR, ".error").text
    assert error_massage
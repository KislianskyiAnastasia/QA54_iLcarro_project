import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_helper import test_go_to_login

URL = "https://icarro-v1.netlify.app/search?page=0&size=10"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()

def test_login_fail(driver):
    test_go_to_login(driver)

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Nastya_star@mail.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Zxczxczxc1")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    error_massage = driver.find_element(By.CSS_SELECTOR, " div[class='modal-content'] p").text
    assert error_massage


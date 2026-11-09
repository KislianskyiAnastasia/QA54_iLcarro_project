import os
import time
from selenium.webdriver.common.by import By
from login_helper import test_go_to_login


def test_login_fail(driver):
    test_go_to_login(driver)

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Nastya_f@mail.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Zxczxczxc")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    error_massage = driver.find_element(By.CSS_SELECTOR, " div[class='modal-content'] p").text
    assert error_massage

def test_login_wrong_email(driver):
    test_go_to_login(driver)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Asdsa.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(os.getenv("ILCARRO_PASSWORD"))
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_massage = driver.find_element(By.CSS_SELECTOR, ".error").text
    assert error_massage

def test_login_wrong_password(driver):
    test_go_to_login(driver)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(os.getenv("ILCARRO_EMAIL"))
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error_massage = driver.find_element(By.CSS_SELECTOR, ".error").text
    assert error_massage


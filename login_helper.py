import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://icarro-v1.netlify.app/search?page=0&size=10"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()
def test_go_to_login(driver):
    button = driver.find_element(By.CSS_SELECTOR,"div[class='header '] a:nth-child(6)")
    assert button.is_displayed()
    button.click()

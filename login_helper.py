from selenium.webdriver.common.by import By


def test_go_to_login(driver):
    button = driver.find_element(By.CSS_SELECTOR,"div[class='header '] a:nth-child(6)")
    assert button.is_displayed()
    button.click()

import os

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.login_page import LoginPage


def test_login_success(driver: WebDriver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.fill_email_field(os.getenv("ILCARRO_EMAIL"))
    login_page.fill_password_field(os.getenv("ILCARRO_PASSWORD"))
    login_page.click_login_button()

    assert login_page.is_login_success() == "You are logged in success"
    login_page.is_ok_login_success()


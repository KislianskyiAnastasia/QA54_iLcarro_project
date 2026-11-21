import os

from pages.login_page import LoginPage
from pages.add_car_page import AddCarPage


def test_add_car_success(driver):
    login_page = LoginPage(driver)
    add_car_page = AddCarPage(driver)

    # Login
    login_page.open_login_page()
    login_page.fill_email_field("nastya_star@gmail.com")
    login_page.fill_password_field("Zxczxczxc1!")
    login_page.click_login_button()

    assert login_page.is_login_success() == "You are logged in success"
    login_page.is_ok_login_success()

    # Add car
    add_car_page.open_add_car_page()

    add_car_page.fill_city("Haifa")
    add_car_page.fill_make("Toyota")
    add_car_page.fill_model("Corolla")
    add_car_page.fill_year("2022")
    add_car_page.select_fuel("Petrol")
    add_car_page.select_gear("Automatic")
    add_car_page.select_wd("FWD")
    add_car_page.fill_doors("4")
    add_car_page.fill_seats("5")
    add_car_page.fill_car_class("Comfort")
    add_car_page.fill_reg_number("87gs435")
    add_car_page.fill_price("150")

    add_car_page.click_submit()

    assert driver.find_element(
        *add_car_page.MAKE_INPUT
    ).get_attribute("value") == ""
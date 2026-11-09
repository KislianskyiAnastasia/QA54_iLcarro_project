import random
import uuid

from models.user import User
from pages.registration_page import RegistrationPage


def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    # random_suffix = random.randint(1,1000000)
    random_suffix = uuid.uuid4()
    user = User(
        first_name="Anastasia",
        last_name="Kisliy",
        email=f"Kisl{random_suffix}@gmail.com",
        password="Asdasdsd1234!"
    )
    print(random_suffix)

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)

    assert registration_page.conformation1() == "Registered"
    assert registration_page.conformation2() == "You are logged in success"
    registration_page.close_window()






def test_invalid_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="",
        last_name="Kisliy",
        email=f"Kisl@gmail.com",
        password="Asd!asd1234!"
    )

    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_displayed()


import time

from selenium.webdriver.common.by import By


class AddCarPage:
    LET_CAR_WORK_LINK = (By.XPATH,"//a[text()='Let car work']")
    CITY_INPUT = (By.CSS_SELECTOR,"input[id='city']")
    MAKE_INPUT = (By.CSS_SELECTOR,"input[name='manufacture']")
    MODEL_INPUT = (By.CSS_SELECTOR,"input[name='model']")
    YEAR_INPUT = (By.CSS_SELECTOR,"input[name='year']")
    FUEL_SELECT = (By.CSS_SELECTOR,"select[name='fuel']")
    GEAR_SELECT = (By.CSS_SELECTOR,"select[name='gear']")
    WD_SELECT = (By.CSS_SELECTOR,"select[name='wheelsDrive']")
    DOORS_INPUT = (By.CSS_SELECTOR,"input[name='doors']")
    SEATS_INPUT = (By.CSS_SELECTOR,"input[name='seats']")
    CAR_CLASS_INPUT = (By.CSS_SELECTOR,"input[name='carClass']")
    CAR_REG_NUMBER_INPUT = (By.CSS_SELECTOR,"input[name='serialNumber']")
    PRICE_INPUT = (By.CSS_SELECTOR,"input[name='pricePerDay']")
    BUTTON_SUBMIT = (By.XPATH,"//button[text()='Submit']")


    def __init__(self, driver):
        self.driver = driver

    def open_add_car_page(self):
        self.driver.find_element(*self.LET_CAR_WORK_LINK).click()
        time.sleep(3)

    def fill_city(self,city):
        self.driver.find_element(*self.CITY_INPUT).click()
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)

    def fill_make(self,make):
        self.driver.find_element(*self.MAKE_INPUT).click()
        self.driver.find_element(*self.MAKE_INPUT).send_keys(make)

    def fill_model(self,model):
        self.driver.find_element(*self.MODEL_INPUT).click()
        self.driver.find_element(*self.MODEL_INPUT).send_keys(model)

    def fill_year(self,year):
        self.driver.find_element(*self.YEAR_INPUT).click()
        self.driver.find_element(*self.YEAR_INPUT).send_keys(year)

    def select_fuel(self, fuel):
        self.driver.find_element(*self.FUEL_SELECT).send_keys(fuel)

    def select_gear(self, gear):
        self.driver.find_element(*self.GEAR_SELECT).send_keys(gear)

    def select_wd(self, wd):
        self.driver.find_element(*self.WD_SELECT).send_keys(wd)

    def fill_doors(self,doors):
        self.driver.find_element(*self.DOORS_INPUT).click()
        self.driver.find_element(*self.DOORS_INPUT).send_keys(doors)

    def fill_seats(self,seats):
        self.driver.find_element(*self.SEATS_INPUT).click()
        self.driver.find_element(*self.SEATS_INPUT).send_keys(seats)

    def fill_car_class(self,car_class):
        self.driver.find_element(*self.CAR_CLASS_INPUT).click()
        self.driver.find_element(*self.CAR_CLASS_INPUT).send_keys(car_class)

    def fill_reg_number(self,reg_number):
        self.driver.find_element(*self.CAR_REG_NUMBER_INPUT).click()
        self.driver.find_element(*self.CAR_REG_NUMBER_INPUT).send_keys(reg_number)

    def fill_price(self,price):
        self.driver.find_element(*self.PRICE_INPUT).click()
        self.driver.find_element(*self.PRICE_INPUT).send_keys(price)

    def click_submit(self):
        self.driver.find_element(*self.BUTTON_SUBMIT).click()
        time.sleep(3)




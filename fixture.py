import random
import pytest
from locator import Locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://stellarburgers.education-services.ru/"

def generate_email():
    email = f"andreev_alexey_42_{random.randint(100, 999)}@yandex.ru"
    return email

@pytest.fixture
def open_main_page():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()

@pytest.fixture
def registered_user():
    email = generate_email()
    password = '123456'
    name = 'Newuser1'

    driver = webdriver.Chrome()
    driver.get(URL)

    driver.find_element(*Locators.ENTER_IN_BUTTON).click()
    driver.find_element(*Locators.REG_BUTTON).click()
    driver.find_element(*Locators.USERNAME_FIELD).send_keys(name)
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ENTER_BUTTON_ENTER))

    driver.quit()

    return {
        'email': email,
        'password': password,
        'name': name
    }
from locator import Locators
from fixture import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Test_Constructer_In:

    # проверка перехода по клику на «Конструктор» из Личного кабинета
    def test_click_on_constructer(self, open_main_page, registered_user):
        driver = open_main_page

        driver.find_element(*Locators.ENTER_IN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_ENTER).send_keys(registered_user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_ENTER).send_keys(registered_user['password'])
        driver.find_element(*Locators.ENTER_BUTTON_ENTER).click()

        driver.find_element(*Locators.BUTTON_MY_CABINET).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECK_OUT_BUTTON))

    # проверка перехода по клику на логотип Stellar Burgers из Личного кабинета
    def test_click_on_logo(self, open_main_page, registered_user):
        driver = open_main_page

        driver.find_element(*Locators.ENTER_IN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_ENTER).send_keys(registered_user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_ENTER).send_keys(registered_user['password'])
        driver.find_element(*Locators.ENTER_BUTTON_ENTER).click()

        driver.find_element(*Locators.BUTTON_MY_CABINET).click()
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()

        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECK_OUT_BUTTON))

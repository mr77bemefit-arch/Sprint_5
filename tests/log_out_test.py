from locator import Locators
from fixture import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLog_Out:
    #Проверка выхода по кнопке «Выйти» в личном кабинете:
    #вход по кнопке «Войти в аккаунт» на главной:
    def test_click_on_my_lk(self, open_main_page, registered_user):
        driver = open_main_page
        driver.find_element(*Locators.ENTER_IN_BUTTON).click()
        #вводим данные зарегестрированного пользователя в поля "Email" и "Пароль" и кликаем кнопку "Войти"
        driver.find_element(*Locators.EMAIL_FIELD_ENTER).send_keys(registered_user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_ENTER).send_keys(registered_user['password'])
        driver.find_element(*Locators.ENTER_BUTTON_ENTER).click()
        #клик на кнопку "Личный кабинет"
        driver.find_element(*Locators.BUTTON_MY_CABINET).click()
        #ожидание страницы с кнопкой  "Выйти"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LOG_OUT_BUTTON)))
        #клик на кнопку "Выйти"
        driver.find_element(*Locators.LOG_OUT_BUTTON).click()
        #проверяем успешный выход из аккаунта(на странице присутствует кнопка "Войти")
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ENTER_BUTTON)))






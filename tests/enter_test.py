from locator import Locators
from fixture import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Test_Enter:
    #проверка входа по кнопке «Войти в аккаунт» на главной:
    def test_click_on_enter_button(self, open_main_page, registered_user):
        driver = open_main_page
        driver.find_element(*Locators.ENTER_IN_BUTTON).click()
        #вводим данные зарегестрированного пользователя в поля "Email" и "Пароль" и кликаем кнопку "Войти"
        driver.find_element(*Locators.EMAIL_FIELD_ENTER).send_keys(registered_user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_ENTER).send_keys(registered_user['password'])
        driver.find_element(*Locators.ENTER_BUTTON_ENTER).click()
        #проверяем успешный вход(на странице присутствует кнопка "Оформить заказ")
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CHECK_OUT_BUTTON)))


    #проверка входа через кнопку «Личный кабинет»:
    def test_click_on_my_lk(self, open_main_page, registered_user):
        driver = open_main_page
        #клик на кнопку "Личный кабинет"
        driver.find_element(*Locators.BUTTON_MY_CABINET).click()
        #вводим данные зарегестрированного пользователя в поля "Email" и "Пароль" и кликаем кнопку "Войти"
        driver.find_element(*Locators.EMAIL_FIELD_ENTER).send_keys(registered_user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_ENTER).send_keys(registered_user['password'])
        driver.find_element(*Locators.ENTER_BUTTON_ENTER).click()
        #проверяем успешный вход(на странице присутствует кнопка "Оформить заказ")
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CHECK_OUT_BUTTON)))


        #проверка входа через кнопку в форме регистрации:
    def test_click_on_registration(self, open_main_page, registered_user):
        driver = open_main_page
        #клик на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.ENTER_IN_BUTTON).click()
        #клик на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.REG_BUTTON).click()
        #клик на кнопку "Войти" на странице регистрации
        driver.find_element(*Locators.ENTER_BUTTON_REG_PAGE).click()
        #вводим данные зарегестрированного пользователя в поля "Email" и "Пароль" и кликаем кнопку "Войти"
        driver.find_element(*Locators.EMAIL_FIELD_ENTER).send_keys(registered_user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_ENTER).send_keys(registered_user['password'])
        driver.find_element(*Locators.ENTER_BUTTON_ENTER).click()
        #проверяем успешный вход(на странице присутствует кнопка "Оформить заказ")
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CHECK_OUT_BUTTON)))


        #проерка входа через кнопку в форме восстановления пароля:
    def test_click_on_re_check_password(self, open_main_page, registered_user):
        driver = open_main_page
        #клик на кнопку "Войти в аккаунт"
        driver.find_element(*Locators.ENTER_IN_BUTTON).click()
        #клик на кнопку "Восстановить пароль"
        driver.find_element(*Locators.RE_CHECK_PASSWORD).click()
        #клик на кнопку "Войти"
        driver.find_element(*Locators.ENTER_BUTTON_RE_CHECK_PASSWORD).click()
        #вводим данные зарегестрированного пользователя в поля "Email" и "Пароль" и кликаем кнопку "Войти"
        driver.find_element(*Locators.EMAIL_FIELD_ENTER).send_keys(registered_user['email'])
        driver.find_element(*Locators.PASSWORD_FIELD_ENTER).send_keys(registered_user['password'])
        driver.find_element(*Locators.ENTER_BUTTON_ENTER).click()
        #проверяем успешный вход(на странице присутствует кнопка "Оформить заказ")
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.CHECK_OUT_BUTTON)))




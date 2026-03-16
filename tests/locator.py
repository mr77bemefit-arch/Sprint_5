from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


URL = "https://stellarburgers.education-services.ru/"

#кнопка "Войти в аккаунт"
ENTER_IN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
#ссылка "Зарегистрироваться"
REG_BUTTON = (By.CLASS_NAME, 'Auth_link__1fOlj')
#поле "Имя"
USERNAME_FIELD = (By.XPATH, ".//label[text()='Имя']/parent::div/input")
#поле "Email"
EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/parent::div/input")
#поле "Пароль"
PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/parent::div/input")
##кнопка "Зарегистрироваться"
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
#кнопка "Войти"
ENTER_BUTTON =(By.XPATH, ".//button[text()='Войти']")
#текст сообщения "Некорректный пароль"
TEXT_MISSTAKE = (By.XPATH, ".//p[text()='Некорректный пароль']")
#поле "Email" в форме входа
EMAIL_FIELD_ENTER = (By.XPATH, ".//label[text()='Email']/parent::div/input")
#поле "Пароль" в форме входа
PASSWORD_FIELD_ENTER = (By.XPATH, ".//label[text()='Пароль']/parent::div/input")
#кнопка "Войти" на странице входа
ENTER_BUTTON_ENTER =(By.XPATH, ".//button[text()='Войти']")
#кнопка "Оформить заказ"
CHECK_OUT_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
#кнопка "Личный кабинет"
BUTTON_MY_CABINET = (By.XPATH, ".//p[text()='Личный Кабинет']")
#кнопка "Войти" на странице с формой регистрации
ENTER_BUTTON_REG_PAGE = (By.XPATH, ".//a[text()='Войти']")
#кнопка "Восстановить пароль"
RE_CHECK_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")
#кнопка"Войти" на странице восстановления пароля
ENTER_BUTTON_RE_CHECK_PASSWORD = (By.XPATH, ".//a[text()='Войти']")
#текст "Профиль" в Личном кабинете
TEXT_MY_POFILE = (By.XPATH, ".//a[text()='Профиль']")
#кнопка "Конструктор" в Личном кабинете
BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
#логотип Stellar Burgers в Личном кабинете
LOGO_STELLAR_BURGERS = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')
#кнопка "Выйти" в Личном кабинете
LOG_OUT_BUTTON = (By.XPATH, ".//ul/li/button[text()='Выход']")
#раздел "Булки"
CHAPTER_ROLLS = (By.XPATH, ".//span[text()='Булки']")
#раздел "Соусы"
CHAPTER_SAUCES = (By.XPATH, ".//span[text()='Соусы']")
#раздел "Начинки"
CHAPTER_FILLINGS = (By.XPATH, ".//span[text()='Начинки']")
#вкладка "Булки"
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
#вкладка "Соусы"
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
#вкладка "Начинки"
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
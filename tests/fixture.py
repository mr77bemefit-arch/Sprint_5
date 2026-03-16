import random
import pytest
from selenium import webdriver

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


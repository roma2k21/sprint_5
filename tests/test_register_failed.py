import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.test_locators import TestLocators
from conftest import driver


class TestRegisterFailed:

    def test_create_user(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        name = 'RomanTTT' + str({random.randint(100,999)})
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(name)
        email = name + '@ya.ru'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = str(random.randint(10000,99999))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PLACEHOLDER_VISION))
        placeholder = driver.find_element(*TestLocators.PLACEHOLDER_VISION)
        assert placeholder.is_displayed()

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.test_locators import TestLocators
from conftest import driver


class TestTransferPersonalAccount:

    def test_transfer_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        driver.find_element(*TestLocators.LK_LOGIN_PAGE).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.ACCAOUNT_TEXT))
        text = driver.find_element(*TestLocators.ACCAOUNT_TEXT)
        assert text.is_displayed(), f"Не получилось открыть страницу личного кабинета"


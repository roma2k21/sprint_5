from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.test_locators import TestLocators
from conftest import driver


class TestSectionsSauce:

    def test_transfer_to_section_sauce(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        driver.find_element(*TestLocators.BUTTON_SAUCE).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_SAUCE))
        text = driver.find_element(*TestLocators.TITLE_SAUCE)
        assert text.is_displayed(), f"Не получилось открыть раздел Соусы"


class TestSectionsBread:

    def test_transfer_to_section_bread(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        driver.find_element(*TestLocators.BUTTON_SAUCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_SAUCE))
        driver.find_element(*TestLocators.BUTTON_BREAD).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_BREAD))
        text = driver.find_element(*TestLocators.TITLE_BREAD)
        assert text.is_displayed(), f"Не получилось открыть раздел Булки"


class TestSectionsFillings:

    def test_transfer_to_section_fillings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        driver.find_element(*TestLocators.BUTTON_FILLINGS).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_FILLINGS))
        text = driver.find_element(*TestLocators.TITLE_FILLINGS)
        assert text.is_displayed(), f"Не получилось открыть раздел Начинки"

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.test_locators import TestLocators
from conftest import driver


class TestMainEntrance:

    def test_main_entrance(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        title = driver.find_element(*TestLocators.TITLE_VISION)
        assert title.is_displayed(), f"Не авторизовались"


class TestLKEntrance:

    def test_lk_entrance(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.LK_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TITLIE_VISION_ENTRANCR))
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        title = driver.find_element(*TestLocators.TITLE_VISION)
        assert title.is_displayed(), f"Не авторизовались"


class TestFormRegister:

    def test_check_form_register(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TITLIE_VISION_ENTRANCR))
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        title = driver.find_element(*TestLocators.TITLE_VISION)
        assert title.is_displayed(), f"Не авторизовались"


class TestFormRepairPassword:

    def test_check_form_register(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*TestLocators.BUTTON_ENTRANCE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TITLIE_VISION_ENTRANCR))
        email = 'roman21@gmail.com'
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(email)
        password = '123456789'
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_VISION))
        title = driver.find_element(*TestLocators.TITLE_VISION)
        assert title.is_displayed(), f"Не авторизовались"

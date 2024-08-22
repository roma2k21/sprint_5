from selenium.webdriver.common.by import By


class TestLocators:
    INPUT_NAME = By.XPATH, './/*[text()="Имя"]/following-sibling::input'
    INPUT_EMAIL = By.XPATH, './/*[text()="Email"]/following-sibling::input'
    INPUT_PASSWORD = By.XPATH, './/*[text()="Пароль"]/following-sibling::input'
    BUTTON_REGISTRATION = By.XPATH, '//*[contains(@class, "button_button_size_medium")]'
    BUTTON_IN = By.XPATH, '//*[contains(text(), "Войти")]'
    PLACEHOLDER_VISION = By.XPATH, '//*[contains(text(), "Некорректный пароль")]'
    TITLE_VISION = By.XPATH, './/*[contains(text(), "Соберите бургер")]'
    LK_LOGIN_PAGE = By.XPATH, './/*[contains(text(), "Личный Кабинет")]'
    TITLIE_VISION_ENTRANCR = By.XPATH, './/*[contains(text(), "Вход")]'
    BUTTON_ENTRANCE = By.XPATH, './/*[contains(@class, "Auth_link")]'
    ACCAOUNT_TEXT = By.XPATH, './/*[contains(@class, "Account_text")]'
    BUTTON_CONSTRUCTOR = By.XPATH, ('.//div[contains(@class, "AppHeader_header__logo")]')
    BUTTON_EXIT = By.XPATH, './/*[contains(@class, "Account_button") and contains(text(), "Выход")]'
    BUTTON_SAUCE = By.XPATH, './/span[@class="text text_type_main-default" and contains(text(), "Соусы")]'
    TITLE_SAUCE = By.XPATH, './/h2[contains(@class, "text_type_main-medium") and contains(text(), "Соусы")]'
    BUTTON_BREAD = By.XPATH, './/span[@class="text text_type_main-default" and contains(text(), "Булки")]'
    TITLE_BREAD = By.XPATH, './/h2[contains(@class, "text_type_main-medium") and contains(text(), "Булки")]'
    BUTTON_FILLINGS = By.XPATH, './/span[@class="text text_type_main-default" and contains(text(), "Начинки")]'
    TITLE_FILLINGS = By.XPATH, './/h2[contains(@class, "text_type_main-medium") and contains(text(), "Начинки")]'

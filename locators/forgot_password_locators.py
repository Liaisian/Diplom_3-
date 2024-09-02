from selenium.webdriver.common.by import By


class ForgotPasswordLocators:

    FORGOT_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    ACTIVE_PASSWORD_INPUT = (By.CSS_SELECTOR, ".input__container .input_status_active")
    EYE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")


from endpoints import Endpoints
from conftest import driver
from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage
from user_email_password import UserEmailPassword


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(Endpoints.URL_LOGIN)

    def go_to_forgot_password_page(self):
        self.click_to_element(ForgotPasswordLocators.FORGOT_BUTTON)

    def reset_confirmation(self):
        self.click_to_element(ForgotPasswordLocators.EMAIL_INPUT)
        self.add_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, UserEmailPassword.EMAIL)
        self.click_to_element(ForgotPasswordLocators.RECOVER_BUTTON)
        self.url_to_be(Endpoints.URL_RESET_PASSWORD)

    def authorization(self):
        self.open_url(Endpoints.URL_LOGIN)
        self.click_to_element(ForgotPasswordLocators.EMAIL_INPUT)
        self.add_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, UserEmailPassword.EMAIL)
        self.add_text_to_element(ForgotPasswordLocators.PASSWORD_INPUT, UserEmailPassword.PASSWORD)
        self.click_to_element(ForgotPasswordLocators.ENTER_BUTTON)

    def toggle_password_visibility(self):
        self.add_text_to_element(ForgotPasswordLocators.PASSWORD_INPUT, UserEmailPassword.PASSWORD)
        self.click_to_element(ForgotPasswordLocators.EYE_BUTTON)
        self.find_element_with_wait(ForgotPasswordLocators.ACTIVE_PASSWORD_INPUT)


    def is_password_field_active(self):
        password_input = self.find_element_with_wait(ForgotPasswordLocators.ACTIVE_PASSWORD_INPUT)
        return password_input.is_displayed()
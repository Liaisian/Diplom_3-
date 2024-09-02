import time

import allure
from pages.forgot_password_page import ForgotPasswordPage

class TestForgotPassword:
    @allure.title("Проверка восстановления пароля")
    def test_page_forgot_password(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_login_page()
        time.sleep(10)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.reset_confirmation()
        forgot_password_page.toggle_password_visibility()
        assert forgot_password_page.is_password_field_active()

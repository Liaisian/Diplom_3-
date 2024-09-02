import time

import allure

from endpoints import Endpoints
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage


class TestAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        account = AccountPage(driver)
        account.go_to_login_page()
        account.get_current_url()
        expected_url = Endpoints.URL_LOGIN
        current_url = account.get_current_url()

        assert expected_url == current_url

    @allure.title('Переход в раздел «История заказов»')
    def test_switch_to_order_history(self, driver):
        account = AccountPage(driver)
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.authorization()
        account.go_to_login_page()
        account.go_to_order_history()
        account.get_current_url()
        account.url_to_be(Endpoints.URL_ORDER_HISTORY)
        assert account.get_current_url() == Endpoints.URL_ORDER_HISTORY

    @allure.title("Выход из аккаунта")
    def logout(self, driver):
        account = AccountPage(driver)
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.authorization()
        account.go_to_login_page()
        account.exit_from_account()
        account.get_current_url()
        account.url_to_be(Endpoints.URL_LOGIN)
        assert account.get_current_url() == Endpoints.URL_LOGIN








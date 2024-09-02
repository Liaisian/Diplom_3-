from conftest import driver
from locators.account_locators import AccountLocators

from pages.base_page import BasePage



class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.find_element_with_wait(AccountLocators.ACCOUNT_HEADER_BUTTON)
        self.click_to_element(AccountLocators.ACCOUNT_HEADER_BUTTON)

    def go_to_order_history(self):
        self.click_to_element(AccountLocators.ACCOUNT_LIST_ITEM)

    def exit_from_account(self):
        self.click_to_element(AccountLocators.EXIT_BUTTON)

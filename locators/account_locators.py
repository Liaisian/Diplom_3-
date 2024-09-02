from selenium.webdriver.common.by import By


class AccountLocators:

    ACCOUNT_HEADER_BUTTON = (By.CSS_SELECTOR, 'a[href="/account"]')
    ACCOUNT_LIST_ITEM = (By.CSS_SELECTOR, 'a[href="/account/order-history"]')
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")

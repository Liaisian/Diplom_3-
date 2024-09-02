from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FIRST_ORDER = (By.XPATH, ".//p[@class='text text_type_digits-default'][1]")
    MODAL_ORDER = (By.XPATH,'//section[contains(@class,"Modal_modal_opened")]//div[contains(@class,"Modal_modal__container")]')
    ALL_ORDERS_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox')]/"
                                    "p[contains(@class,'text_type_digits-default')]")
    ALL_ORDERS_FEED = (By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]//p[@class='text"
                                 " text_type_digits-default']")
    ORDER_ID =(By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
    LOADING_CHECK_BOX = (By.XPATH, ".//img[@alt='tick animation']")
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_PROCESS = (By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')]/li[@class='text text_type_digits-default mb-2']")
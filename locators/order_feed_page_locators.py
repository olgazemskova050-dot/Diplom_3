from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )
    IN_PROGRESS_ORDER_NUMBER = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"
    )
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    def get_today_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))

    def get_in_progress_order_number(self):
        return self.get_text(OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBER)
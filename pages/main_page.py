from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_constructor(self):
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.js_click(MainPageLocators.INGREDIENT_ITEM)

    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    def is_ingredient_modal_invisible(self):
        return self.is_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    def close_modal(self):
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def get_ingredient_counter(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)
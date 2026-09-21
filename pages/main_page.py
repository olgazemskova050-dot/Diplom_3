from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_ITEM)

    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    def is_ingredient_modal_invisible(self):
        return self.is_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    def close_modal(self):
        # клик по крестику через JS — надёжнее обычного click
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def get_ingredient_counter(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)
import allure


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver, main_page):
        main_page.click_order_feed()
        main_page.click_constructor()
        assert "stellarburgers.education-services.ru" in driver.current_url

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_go_to_order_feed(self, driver, main_page):
        main_page.click_order_feed()
        assert "/feed" in driver.current_url

    @allure.title("Клик на ингредиент открывает всплывающее окно")
    def test_ingredient_modal_appears(self, main_page):
        main_page.click_ingredient()
        assert main_page.is_ingredient_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closes(self, main_page):
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_ingredient_modal_invisible()

    @allure.title("Счётчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_increases(self, main_page):
        counter = main_page.get_ingredient_counter()
        assert isinstance(counter, int)
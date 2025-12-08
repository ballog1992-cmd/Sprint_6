import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить форму заказа")
    def input_form_field(self, name, family, adress, telephone):

        self.send_keys_to_input(LoginPageLocators.NAME, name)
        self.send_keys_to_input(LoginPageLocators.FAMILY, family)
        self.send_keys_to_input(LoginPageLocators.ADRESS, adress)
        self.send_keys_to_input(LoginPageLocators.TELEPHONE, telephone)

    @allure.step("Выбираем станцию метро")
    def select_random_metro_station(self):

        self.click_on_element(LoginPageLocators.METRO)
        station = self.wait_for_element(LoginPageLocators.OPTIONS_CONTAINER)
        station.click()
        

    @allure.step("Подтверждаем заказ")
    def button_succesful_in_order(self):

        self.click_on_element(LoginPageLocators.BUTTON_SUCCESESS_LOGIN)

    @allure.step("Заполнить форму аренды")
    def input_form_rental(self, date, text):

        self.send_keys_to_input(LoginPageLocators.DATE, date)
        self.send_keys_to_input(LoginPageLocators.COMMENT_FIELD_COURIER, text)
        self.click_on_element(LoginPageLocators.DATE_CALENDAR)
    @allure.step("Выбор срока аренды")
    def random_rent(self):
        self.click_on_element(LoginPageLocators.LIST_RENTAL_PERIODS)
        first_option = self.wait_for_element(LoginPageLocators.DROP_DOWN_LIST_PERIODS)
        first_option.click()

    @allure.step("Выбор цвета самоката")
    def scooter_color(self):
        self.click_on_element(LoginPageLocators.SCOOTER_COLOR_CHECKBOX)
    
    @allure.step("Клик по кнопке подверждения аренды")
    def succeses_button_rent(self):
       self.click_on_element(LoginPageLocators.BUTTON_SUCCESESS_RENT_DESIGN)
    @allure.step("Клик по кнопке подверждения заказа")
    def succeses_button_order_rent(self):
       self.click_on_element(LoginPageLocators.BUTTON_SUCCESESS_ORDER_DESIGN)
    
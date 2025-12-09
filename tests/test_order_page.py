import allure
import pytest
from pages.order_page import OrderPage
from helper import generate_registration_data
from locators.login_page_locators import LoginPageLocators
from data import ORDER_TEST_DATA


@allure.feature("Оформление заказа и его подтверждение")
class TestPlacingAndConfirmingOrder:

    @allure.feature("Заполнение формы заказа")
    def test_fill_order_form_with_random_metro(self, order_page_driver):
        driver = order_page_driver
        order_page = OrderPage(driver)

        name, family, address, phone, date, text = generate_registration_data()
        order_page.input_form_field(name, family, address, phone)
        order_page.select_random_metro_station()

        order_page.button_succesful_in_order()

        order_page.input_form_rental(date, text)
        order_page.random_rent()
        order_page.scooter_color()

        order_page.succeses_button_rent()
        order_page.succeses_button_order_rent()

        assert order_page.wait_for_element(LoginPageLocators.ORDER_INFORMATION_POPUP)

    @allure.feature("Заполнение формы заказа с ручными наборами данных")
    @pytest.mark.parametrize(
        "name, family, address, phone, date, text", ORDER_TEST_DATA
    )
    def test_fill_order_form_with_different_data(
        self, order_page_driver, name, family, address, phone, date, text
    ):
        driver = order_page_driver
        order_page = OrderPage(driver)

        name, family, address, phone, date, text = generate_registration_data()
        order_page.input_form_field(name, family, address, phone)
        order_page.select_random_metro_station()

        order_page.button_succesful_in_order()

        order_page.input_form_rental(date, text)
        order_page.random_rent()
        order_page.scooter_color()

        order_page.succeses_button_rent()
        order_page.succeses_button_order_rent()

        assert order_page.wait_for_element(LoginPageLocators.ORDER_INFORMATION_POPUP)
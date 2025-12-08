import allure
from pages.base_page import BasePage
from curl import *
from locators.button_main_page_locators import ButtonAndLinksLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@allure.feature("Кнопки и ссылки на главной странице")
class TestButtonAndLinksMainPage:

    @allure.title("Проверка кнопки перехода на страницу заказа в шапке страницы")
    def test_button_order_in_header(self, driver):

        button_order = BasePage(driver)
        button_order.click_on_element(ButtonAndLinksLocators.BUTTON_LOGIN_HEADER)
        current_url = driver.current_url
        assert order_page in current_url

    @allure.title("Проверка кнопки перехода на страницу заказа на дорожной карте")
    def test_button_order_in_roadmap(self, driver):

        button_order = BasePage(driver)

        button_order.scroll_to_element(ButtonAndLinksLocators.BUTTON_LOGIN_ROADMAP)
        button_order.wait_for_element(ButtonAndLinksLocators.BUTTON_LOGIN_ROADMAP)
        button_order.click_on_element(ButtonAndLinksLocators.BUTTON_LOGIN_ROADMAP)
        current_url = driver.current_url
        assert order_page in current_url

    @allure.title("Проверка перехода по клику на логотип сайта на главную страницу")
    def test_click_of_link_the_main_page(self, order_page_driver):

        link_main_page = BasePage(order_page_driver)

        link_main_page.click_on_element(ButtonAndLinksLocators.LINK_MAIN_PAGE)
        current_url = order_page_driver.current_url
        assert main_page in current_url

    @allure.title(
        "Проверка перехода по клику на ссылку яндекса на главную страницу дзена"
    )
    def test_click_of_link_the_dzen_site(self, driver):

        link_dzen_site = BasePage(driver)

        link_dzen_site.click_on_element(ButtonAndLinksLocators.LINK_DZEN_PAGE)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.url_contains(dzen_site))
        current_url = driver.current_url
        assert dzen_site in current_url

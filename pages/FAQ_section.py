import allure
from pages.base_page import BasePage
from locators.FAQ_section_locators import FAQSectionLocatorsItem
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FAQSection(BasePage):

    @allure.step("Скролл на раздел FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_element(FAQSectionLocatorsItem.QUESTIONS_SECTION)

    @allure.step("Получить текст вопроса №{number}")
    def get_question_text(self, number):
        question_locator = FAQSectionLocatorsItem.question_headings(number)
        return self.get_text_on_element(question_locator)

    @allure.step("Кликнуть по вопросу №{number}")
    def click_question(self, number):
        question_locator = FAQSectionLocatorsItem.question_headings(number)
        self.click_on_element(question_locator)

    @allure.step("Получить текст ответа на вопрос №{number}")
    def get_answer_text(self, number):
        answer_locator = FAQSectionLocatorsItem.answers_to_questions(number)
        return self.get_text_on_element(answer_locator)

    @allure.step("Ожидание появления аккордиона с вопросами")
    def waiting_accordion_appear_with_questions(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
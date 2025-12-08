import allure
from pages.base_page import BasePage
from locators.FAQ_section_locators import FAQ_Section_Locators

class FAQSection(BasePage):

    @allure.step("Скролл на раздел FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_element(FAQ_Section_Locators.QUESTIONS_SECTION)  

    @allure.step("Получить текст вопроса №{number}")
    def get_question_text(self, number):
        question_locator = FAQ_Section_Locators.question_headings(number)
        return self.get_text_on_element(question_locator)
    
    @allure.step("Кликнуть по вопросу №{number}")
    def click_question(self, number):
        question_locator = FAQ_Section_Locators.question_headings(number)
        self.click_on_element(question_locator)
    
    @allure.step("Получить текст ответа на вопрос №{number}")
    def get_answer_text(self, number):
        answer_locator = FAQ_Section_Locators.answers_to_questions(number)
        return self.get_text_on_element(answer_locator)

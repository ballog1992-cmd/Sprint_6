import pytest
import allure
from pages.FAQ_section import FAQSection
from data import TextOfQuestionsInFAQSection, TextOfAnswersInFAQSection
import time

@allure.feature("Раздел FAQ - Вопросы о главном")
class TestFAQSection:

    @allure.title("Проверка текста всех вопросов в разделе FAQ")
    @pytest.mark.parametrize(
        "number, expected_text",
        TextOfQuestionsInFAQSection.text_and_number_question_headings,
    )
    def test_question_headings_text(self, driver, number, expected_text):
        faq_page = FAQSection(driver)
        faq_page.scroll_to_faq_section()
        time.sleep(1)
        actual_text = faq_page.get_question_text(number)
        assert actual_text == expected_text

    @allure.title("Проверка текста всех ответов на вопросе в разделе FAQ")
    @pytest.mark.parametrize(
        "number, expected_text",
        TextOfAnswersInFAQSection.text_and_number_question_headings,
    )
    def test_answers_text(self, driver, number, expected_text):
        faq_page = FAQSection(driver)
        faq_page.scroll_to_faq_section()
        time.sleep(1)
        faq_page.click_question(number)
        actual_text = faq_page.get_answer_text(number)
        assert actual_text == expected_text

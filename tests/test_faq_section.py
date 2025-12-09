import pytest
import allure
from pages.FAQ_section import FAQSection
from data import TextOfQuestionsInFAQSection, TextOfAnswersInFAQSection
from locators.FAQ_section_locators import FAQSectionLocatorsItem


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
        faq_page.waiting_accordion_appear_with_questions(
            FAQSectionLocatorsItem.FAQ_ACCORDION
        )
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
        faq_page.waiting_accordion_appear_with_questions(
            FAQSectionLocatorsItem.FAQ_ACCORDION
        )
        faq_page.click_question(number)
        actual_text = faq_page.get_answer_text(number)
        assert actual_text == expected_text
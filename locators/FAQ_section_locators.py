from selenium.webdriver.common.by import By


class FAQSectionLocatorsItem:

    # Секция "Вопросы о главном"
    QUESTIONS_SECTION = (By.XPATH, "//div[@class='Home_FourPart__1uthg']")
    # FAQ заголовки вопросов
    # Блок аккордиона с вопросами
    FAQ_ACCORDION = (By.XPATH, "//div[@class='accordion']")

    @staticmethod
    def question_headings(number):
        return (By.ID, f"accordion__heading-{number - 1}")

    # FAQ панель ответов на вопросы

    @staticmethod
    def answers_to_questions(number):
        return (By.XPATH, f"//div[@id='accordion__panel-{number - 1}']//p")
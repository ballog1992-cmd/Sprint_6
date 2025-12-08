from selenium.webdriver.common.by import By


class FAQ_Section_Locators:

    # Секция "Вопросы о главном"
    QUESTIONS_SECTION = (By.XPATH, "//div[@class='Home_FourPart__1uthg']")
    # FAQ заголовки вопросов

    @staticmethod
    def question_headings(number):
        return (By.ID, f"accordion__heading-{number - 1}")

    # FAQ панель ответов на вопросы

    @staticmethod
    def answers_to_questions(number):
        return (By.XPATH, f"//div[@id='accordion__panel-{number - 1}']//p")

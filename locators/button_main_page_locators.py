from selenium.webdriver.common.by import By


class ButtonAndLinksLocators:

    # Кнопки и ссылки главной страницы
    # Кнопка оформления заказа
    BUTTON_LOGIN_HEADER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[@class='Button_Button__ra12g']")
    # Кнопка оформления на дорожной карте
    BUTTON_LOGIN_ROADMAP = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm button")
    # Кнопка проверки статуса заказа
    BUTTON_STATUS_ORDER = (By.XPATH, "//button[@class='Header_Link__1TAG7']")
    

    # Ссылка на главную страницу
    LINK_MAIN_PAGE = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR' and @href='/']")
    # Ссылка на главную страницу DZEN 
    LINK_DZEN_PAGE = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru']")

    


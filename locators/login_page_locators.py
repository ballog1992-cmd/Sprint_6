from selenium.webdriver.common.by import By


class LoginPageLocators:

    # Поле ввода 'Имя'
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    # Поле ввода 'Фамилия'
    FAMILY = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле ввода 'Адрес'
    ADRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Контейнер с выбором метро (когда список закрыт)
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Контейнер с опциями (когда список открыт)
    OPTIONS_CONTAINER = (By.XPATH, "//div[contains(@class, 'select-search__select')]")
    # Поле ввода 'Телефон'
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка подтверждения заказа
    BUTTON_SUCCESESS_LOGIN = (By.XPATH, "//button[contains(text(), 'Далее')]")

    # Окно аренды самоката
    # Поле с выбором даты
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    DATE_CALENDAR = (By.XPATH, "//div[@class='react-datepicker__week']")
    # Поле срока аренды
    LIST_RENTAL_PERIODS = (By.XPATH, "//div[@class='Dropdown-control']")
    # Выпадающий список срока аренды
    DROP_DOWN_LIST_PERIODS = (By.XPATH, "//div[@class='Dropdown-option']")
    # Чекбокс цвета самоката
    SCOOTER_COLOR_CHECKBOX = (By.XPATH, '//input[@id="black"]')
    # Поле с комментариями для курьера
    COMMENT_FIELD_COURIER = (By.XPATH,"//input[@placeholder='Комментарий для курьера']")
    # Кнопка заказать
    BUTTON_SUCCESESS_RENT_DESIGN = (By.XPATH,"//div[@class='Order_Buttons__1xGrp']//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Кнопка подтверждения аренды
    BUTTON_SUCCESESS_ORDER_DESIGN = (By.XPATH, "//button[contains(text(), 'Да')]")
    # Попап подтверждения заказа
    ORDER_INFORMATION_POPUP = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
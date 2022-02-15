import time

from selenium.webdriver.common.by import By

def test_guest_should_see_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    time.sleep(5)
    try:
        assert button, 'Нету кнопки'
    except AssertionError:
        print("Кнопка не нейдена!")

import time


def test_add_button_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    browser.find_element_by_class_name("btn-add-to-basket")

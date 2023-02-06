import time

from selenium.webdriver.common.by import By


def test_find_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"), "add to basket button not found"

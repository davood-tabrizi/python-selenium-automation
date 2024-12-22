from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class Header(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')
    CART_BUTTON = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    def search_product_text(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        sleep(2)

    def search_button_click(self):
        self.click(*self.SEARCH_BUTTON)
        sleep(20)

    def cart_button_click(self):
       self.click(*self.CART_BUTTON)
       sleep(3)


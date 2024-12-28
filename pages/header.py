from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class Header(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]')
    CART_BUTTON = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    SIGN_IN_BUTTON_HEADER = (By.XPATH, "//span[contains(text(), 'Sign in')]")
    SIGN_IN_BUTTON_SIDE_NAVIGATION_MENU = (By.XPATH, "//button[@data-test='accountNav-signIn']")

    def search_product_text(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        sleep(2)

    def search_button_click(self):
        self.click(*self.SEARCH_BUTTON)
        sleep(20)

    def cart_button_click(self):
       self.click(*self.CART_BUTTON)
       sleep(3)

    def click_header_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON_HEADER)

    def click_sign_in_side_navigation_menu(self):
        #self.click(*self.SIGN_IN_BUTTON_SIDE_NAVIGATION_MENU)
        self.wait_and_click(*self.SIGN_IN_BUTTON_SIDE_NAVIGATION_MENU)

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    SIGN_IN_TEXT = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    def verify_signin_page(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TEXT)
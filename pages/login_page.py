from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    SIGN_IN_TEXT = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    SIGN_IN_URL = ("https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin")
    TERM_CONDITION_LINK = (By.XPATH, '//a[text()="Target terms and conditions"]')
    USER_NAME_PLACE_HOLDER =(By.CSS_SELECTOR, "input[id='username']")
    PASSWORD_PLACE_HOLDER =(By.CSS_SELECTOR, "input[id='password']")
    SIGNIN_WITH_PASSWORD_BUTTON =(By.CSS_SELECTOR, "button[id='login']")
    DENIED_MESSAGE_FOR_INCORRECT_USER_PASSWORD = (By.CSS_SELECTOR, "div[data-test=authAlertDisplay]")



    def verify_signin_page(self):
        self.verify_text('Sign into your Target account', *self.SIGN_IN_TEXT)

    def open_signin_page(self):
        self.open_url(self.SIGN_IN_URL)

    def target_term_and_condition_link(self):
        self.wait_and_click(*self.TERM_CONDITION_LINK)

    def insert_incorrect_user_password(self):
        self.input_text("Davood_tabrizi@yahoo.com", *self.USER_NAME_PLACE_HOLDER)
        self.input_text("Alot1234*", *self.PASSWORD_PLACE_HOLDER)
        self.click(*self.SIGNIN_WITH_PASSWORD_BUTTON)

    def verify_user_denied_to_access_with_wrong_user_password(self):
        self.verify_partial_text("Sorry, something went wrong", *self.DENIED_MESSAGE_FOR_INCORRECT_USER_PASSWORD)
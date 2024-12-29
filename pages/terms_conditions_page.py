from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TermsConditions(BasePage):

 def verify_term_condition_page_open(self):
     self.verify_partial_url("terms-conditions")
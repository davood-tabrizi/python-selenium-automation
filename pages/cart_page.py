from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class CartPage(BasePage):
 CART_EMPTY_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Your cart is empty')]")
 def verify_cart_empty(self):
     expected_result = 'Your cart is empty'
     actual_result = self.driver.find_element(*self.CART_EMPTY_MESSAGE).text
     assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
     print('Test case passed')
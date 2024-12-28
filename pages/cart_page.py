from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class CartPage(BasePage):
 CART_EMPTY_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Your cart is empty')]")
 ORDER_SUMMERY = (By.CSS_SELECTOR,  "h2[data-test='cart-summary-title']")
 ITEM_EXPECTED_NAME = (By.CSS_SELECTOR, "[data-test='product-title']")

 def verify_cart_empty(self):
     expected_result = 'Your cart is empty'
     actual_result = self.driver.find_element(*self.CART_EMPTY_MESSAGE).text
     assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
     print('Test case passed')

 def verify_cart_is_not_empty(self):

     self.verify_text("Order summary", *self.ORDER_SUMMERY)
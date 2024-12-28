from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class SearchResultsPage(BasePage):

 SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")
 ITEM_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
 ADD_TO_CART_BUTTON_SIDE_NAVIGATION = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
 VIEW_CART_CHECK_OUT_BUTTON = (By.XPATH, "//a[contains(text(), 'View cart & check out')]")

 def verify_search_results(self, product):
     sleep(5)
     actual_result = self.find_element(*self.SEARCH_RESULTS).text
     assert product in actual_result, f'Expected result -{product}- not in {actual_result}'
     sleep(10)

 def add_item_to_cart(self):
    self.wait_and_click(*self.ITEM_ADD_TO_CART_BUTTON)
    self.wait_and_click(*self.ADD_TO_CART_BUTTON_SIDE_NAVIGATION)
    self.wait_and_click(*self.VIEW_CART_CHECK_OUT_BUTTON)
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then("Verify 'Your cart is empty' message shown")
def verify_found_text(contex):
 expected_result = 'Your cart is empty'
 actual_result = contex.driver.find_element(By.XPATH, "//h1[contains(text(), 'Your cart is empty')]").text
 assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
 print('Test case passed')


@then("verify the cart is not empty")
def cart_is_not_empty(context):
    expected_result = "Lipton Black Tea Bags - 100ct"
    actual_result = context.driver.find_element(By.XPATH, "//div[text()='Lipton Black Tea Bags - 100ct']").text
    assert expected_result in actual_result , f"Test item {expected_result} is not in cart"
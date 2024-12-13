from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("verify the cart is not empty")
def cart_is_not_empty(context):
    expected_result = "Lipton Black Tea Bags - 100ct"
    actual_result = context.driver.find_element(By.XPATH, "//div[text()='Lipton Black Tea Bags - 100ct']").text
    assert expected_result in actual_result , f"Test item {expected_result} is not in cart"
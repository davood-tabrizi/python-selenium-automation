from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then("Verify 'Your cart is empty' message shown")
def verify_found_text(context):
  context.app.cart_page.verify_cart_empty()


@then("verify the cart is not empty")
def cart_is_not_empty(context):
    context.app.cart_page.verify_cart_is_not_empty()
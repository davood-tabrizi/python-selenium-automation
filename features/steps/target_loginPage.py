from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then("Verify Sign In form opened")
def verify_signin_form(context):
 context.app.login_page.verify_signin_page()

@given("Open sign in page")
def open_signin_page(context):
 context.app.login_page.open_signin_page()

@when("Store original window")
def store_original_window(context):
 context.original_window = context.app.base_page.get_current_window_handle()
 print(context.original_window)

@when("Click on Target terms and conditions link")
def target_term_and_condition_link(context):
  context.app.login_page.target_term_and_condition_link()






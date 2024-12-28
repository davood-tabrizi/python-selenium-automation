from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then("Verify Sign In form opened")
def verify_signin_form(context):
 context.app.login_page.verify_signin_page()
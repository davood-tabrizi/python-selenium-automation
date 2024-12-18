from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then("Verify Sign In form opened")
def verify_signin_form(contex):
 expected_result = 'Sign into your Target account'
 actual_result = contex.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
 assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
 print('Test case passed')
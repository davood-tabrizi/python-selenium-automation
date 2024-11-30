from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given("Open target main page")
def open_main(contex):
    contex.driver.get("https://www.target.com/")


@when("Click on cart icon, on the right side of the page")
def click_on_cart_icon(contex):
    contex.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(3)



@then("Verify 'Your cart is empty' message shown")
def verify_found_text(contex):
 expected_result = 'Your cart is empty'
 actual_result = contex.driver.find_element(By.XPATH, "//h1[contains(text(), 'Your cart is empty')]").text
 assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
 print('Test case passed')

@when("The user click on sign-in icon")
def click_on_signin(contex):
  contex.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]").click()
  sleep(3)


@when("Click Sign In from right side navigation menu")
def click_on_signin_navigation(contex):
  contex.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
  sleep(3)


@then("Verify Sign In form opened")
def verify_signin_form(contex):
 expected_result = 'Sign into your Target account'
 actual_result = contex.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
 assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
 print('Test case passed')

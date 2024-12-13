from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open target main page")
def open_main(context):
    context.driver.get("https://www.target.com/")
    sleep(5)

@when("Click on cart icon, on the right side of the page")
def click_on_cart_icon(contex):
    contex.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(3)


@when("The user click on sign-in icon")
def click_on_signin(contex):
  contex.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]").click()
  sleep(3)

@when("Click Sign In from right side navigation menu")
def click_on_signin_navigation(contex):
    contex.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(3)

@when("Input {product} into the search field")
def input_to_search_field(context,product):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]').send_keys(product)
    sleep(2)

@when('Click on the search icon')
def click_to_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()
    sleep(20)



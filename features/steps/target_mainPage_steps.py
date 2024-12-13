from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open target main page")
def open_main(context):
    context.driver.get("https://www.target.com/")
    sleep(5)


@when("Input {product} into the search field")
def input_to_search_field(context,product):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]').send_keys(product)
    sleep(2)

@when('Click on the search icon')
def click_to_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()
    sleep(20)



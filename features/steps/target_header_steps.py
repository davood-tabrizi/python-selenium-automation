from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when("Click on cart icon, on the right side of the page")
def click_on_cart_icon(context):
    context.app.header.cart_button_click()
    #context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-test='@web/CartIcon']"))).click()
    #context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    #sleep(3)

@when("Input {product} into the search field")
def input_to_search_field(context,product):
    context.app.header.search_product_text(product)
    #context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchInput"]').send_keys(product)
    #sleep(2)

@when('Click on the search icon')
def click_to_search_icon(context):
    context.app.header.search_button_click()
    #context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]'))).click()
    #context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]').click()
    #sleep(20)

@when("The user click on sign-in icon")
def click_on_signin(context):
    context.app.header.click_header_sign_in_button()
  #contex.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sign in')]"))).click()
  #contex.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]").click()
  #sleep(3)

@when("Click Sign In from right side navigation menu")
def click_on_signin_navigation(context):
    context.app.header.click_sign_in_side_navigation_menu()
    #context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='accountNav-signIn']"))).click()
    #contex.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    #sleep(3)

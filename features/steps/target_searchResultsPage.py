from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



@then('Results for {product} are shown')
def verify_found_results(context, product):
    context.app.search_results_page.verify_search_results(product)

    #sleep(5)
    #assert product.lower() in context.driver.current_url.lower(), \
        #f'Expected query not in {context.driver.current_url.lower()}'
    #sleep(10)


@when("add an item of results to cart by Clicking on Add to cart button")
def add_item_to_cart(context):
    context.app.search_results_page.add_item_to_cart()
    #context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='chooseOptionsButton'][id='addToCartButtonOrTextIdFor13010225']"))).click()
    #context.driver.find_element(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton'][id='addToCartButtonOrTextIdFor13010225']").click()
    #sleep(30)
    #context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='orderPickupButton'][id='addToCartButtonOrTextIdFor13010225']"))).click()
    #context.driver.find_element(By.CSS_SELECTOR, "button[data-test='orderPickupButton'][id='addToCartButtonOrTextIdFor13010225']").click()
    #sleep(30)
    #context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View cart & check out')]"))).click()
    #context.driver.find_element(By.XPATH, "//a[contains(text(), 'View cart & check out')]").click()
    #sleep(30)
   # button[class ='styles_baseIconButton__1zmiH styles_iconButtonClose__R7qvf styles_sm__ZqLFy nds-cell_mod_d_header__c_btn'] svg[viewBox='0 0 24 24']


@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "use[href='/icons/Cart.svg#Cart']").click()
    

@then('verify cart is not empty')
def cart_not_empty(context):
    result=context.driver.find_element(By.XPATH, '//h2[text()="Order summary"]')
    assert result == "Order summary", f"we couldn't verify cart is not empty"
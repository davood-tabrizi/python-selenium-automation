from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given("Open target circle page")
def open_circle_page(context):
    context.driver.get("https://www.target.com/circle")

@then("verify there is at least 10 benefit cells")
def number_of_benefit_cells(context):
    number_of_cells = context.driver.find_elements(By.CSS_SELECTOR, 'a[data-test="@web/slingshot-components/CellsComponent/Link"]')

    assert len(number_of_cells) >= 10, f"there is {len(number_of_cells)} benefit cells"



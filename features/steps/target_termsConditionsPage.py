from behave import given, when, then


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.app.terms_conditions_page.switch_to_new_window()

@then("Verify Terms and Conditions page is opened")
def verify_term_condition_page_open(context):
    context.app.terms_conditions_page.verify_term_condition_page_open()

@then("User can close new window and switch back to original")
def close_current_window_switch_to_original_page(context):
    context.app.terms_conditions_page.close()
    context.app.terms_conditions_page.switch_to_window_by_id(context.original_window)
from behave import given


@given("I navigate to the kayak main page")
def visit_login(context):
    return context.browser.visit("")

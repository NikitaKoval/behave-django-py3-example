from behave import *

use_step_matcher("re")


@given("I'm on hello page")
def step_impl(context):
    context.browser.visit(context.base_url + '/hello/')


@step('I see "(.*)" message')
def step_impl(context, message):
    assert context.browser.is_text_present(message)
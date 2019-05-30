from behave import given, when, then
import asserts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('Uzytkownik wchodzi na strone logowania shift')
def step_start_page(context):
    context.driver.get('http://pccorsachelp.compol2.com.pl/account/login')


@when('Uzytkownik wypelnia prawidlowo pola log i pass z wcisnietym shift')
def step_set_login_in(context):
    context.driver.find_element_by_id('login-input').send_keys(Keys.SHIFT +"admin")
    context.driver.find_element_by_id('password-input').send_keys(Keys.SHIFT +"pccorsachelp")


@when('Uzytkownik wciska klawisz ENTER, shift')
def step_set_login_in_shift(context):
    context.driver.find_element_by_id('password-input').send_keys(Keys.ENTER)
    context.driver.implicitly_wait(3)


@then('Uzytkownik loguje sie na strone administratora shift')
def step_valid_login(context):
    context.driver.save_screenshot("screenshot-login.png")
    #assert context.driver.find_element_by_id('calendar')
    context.driver.close()


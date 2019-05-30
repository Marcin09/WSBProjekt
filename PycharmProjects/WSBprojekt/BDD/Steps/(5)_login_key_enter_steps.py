from behave import given, when, then
import asserts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('Uzytkownik wchodzi na strone logowania enter')
def step_start_page(context):
    context.driver.get('http://pccorsachelp.compol2.com.pl/account/login')


@when('Uzytkownik wypelnia prawidlowo pola log i pass enter')
def step_set_login_in(context):
    context.driver.find_element_by_id('login-input').send_keys("admin")
    context.driver.find_element_by_id('password-input').send_keys("pccorsachelp")


@when('Uzytkownik wciska klawisz ENTER')
def step_set_login_in_enter(context):
    context.driver.find_element_by_id("password-input").send_keys(Keys.ENTER)

@then('Uzytkownik loguje sie na strone administratora')
def step_valid_login(context):
    context.driver.save_screenshot("screenshot-login.png")
    context.driver.close()


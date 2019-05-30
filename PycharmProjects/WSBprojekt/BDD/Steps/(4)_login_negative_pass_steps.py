from behave import given, when, then
import asserts

@given('Uzytkownik wchodzi na strone logowania negativ pass')
def step_start_page(context):
    context.driver.get('http://pccorsachelp.compol2.com.pl/account/login')


@when('Uzytkownik wypelnia pole login, pole pass pozostaje puste')
def step_set_login_in(context):
    context.driver.find_element_by_id('login-input').send_keys("admin")
    context.driver.find_element_by_id('password-input').clear()
    context.driver.find_element_by_css_selector('button.btn').click()



@then('Uzytkownik probuje zalogowac sie do panelu neg pass')
def step_valid_login(context):
    context.driver.save_screenshot("screenshot-login.png")
    context.driver.close()


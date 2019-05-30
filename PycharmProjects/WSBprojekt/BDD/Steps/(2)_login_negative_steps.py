from behave import given, when, then
import asserts

@given('Uzytkownik wchodzi na strone logowania negativ')
def step_start_page(context):
    context.driver.get('http://pccorsachelp.compol2.com.pl/account/login')


@when('Uzytkownik nie wypelnia pol formularza')
def step_set_login_in(context):
    context.driver.find_element_by_id('login-input').clear()
    context.driver.find_element_by_id('password-input').clear()
    context.driver.find_element_by_css_selector('button.btn').click()


@then('Uzytkownik probuje zalogowac sie do panelu')
def step_valid_login(context):
    context.driver.implicitly_wait(2)
    context.driver.save_screenshot("screenshot-login.png")
    assert context.driver.find_element_by_id("main-wrapper")
    context.driver.close()



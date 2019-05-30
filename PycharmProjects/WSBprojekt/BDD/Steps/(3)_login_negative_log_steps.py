from behave import given, when, then
import asserts

@given('Uzytkownik wchodzi na strone logowania negativ log')
def step_start_page(context):
    context.driver.get('http://pccorsachelp.compol2.com.pl/account/login')


@when('Uzytkownik pole log pozostawia puste, w pole pass wpisuje poprawne haslo')
def step_set_login_in(context):
    context.driver.find_element_by_id('login-input').clear()
    context.driver.find_element_by_id('password-input').send_keys('pccorsachelp')
    context.driver.find_element_by_css_selector('button.btn').click()



@then('Uzytkownik probuje zalogowac sie do panelu neg log')
def step_valid_login(context):
    context.driver.save_screenshot("screenshot-login.png")
    context.driver.close()



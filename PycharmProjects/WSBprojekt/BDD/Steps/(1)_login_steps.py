from behave import given, when, then
import asserts

@given('Uzytkownik wchodzi na strone logowania')
def step_start_page(context):
        context.driver.get('http://pccorsachelp.compol2.com.pl/account/login')
        context.driver.implicitly_wait(2)
        assert context.driver.find_element_by_id("wrapper")

@when('Uzytkownik wypelnia pola formularza wlasciwymi danymi i loguje sie na konto')
def step_set_login_in(context):
        context.driver.find_element_by_id('login-input').send_keys('admin')
        context.driver.find_element_by_id('password-input').send_keys('pccorsachelp')
        context.driver.implicitly_wait(2)



@then('Uzytkownik wchodzi do panelu administracyjnego')
def step_valid_login(context):
        context.driver.find_element_by_css_selector('button.btn').click()
        context.driver.save_screenshot("screenshot-login.png")
        context.driver.implicitly_wait(2)
        assert context.driver.find_element_by_id("main-wrapper")
        context.driver.close()



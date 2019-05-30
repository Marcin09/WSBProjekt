from behave import given, when, then
import asserts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('Uzytkownik wchodzi na strone administratora NP')
def step_start_page(context):
    context.driver.get('http://pccorsachelp.compol2.com.pl/account/login')


@when('Uzytkownik wchodzi do zakladki KA')
def step_set_login_in(context):
    context.driver.find_element_by_id('login-input').send_keys("admin")
    context.driver.find_element_by_id('password-input').send_keys('pccorsachelp')
    context.driver.find_element_by_css_selector('button.btn').click()
    context.driver.implicitly_wait(3)

@when('Uzytkownik wchodzi do NP')
def step_set_login_in_form(context):
    context.driver.find_element_by_xpath("/html/body/div[2]/aside/div/div[1]/nav/ul/li[9]/a/span").click()
    context.driver.find_element_by_xpath("/html/body/div[2]/aside/div/div[1]/nav/ul/li[9]/ul/li/a").click()
    context.driver.find_element_by_id("add-btn").click()
    context.driver.implicitly_wait(3)
# czasami wchodzi do formularza "nowy pacjent" - trudno powtoryc test pozytywny

@then('Uzytkownik widzi formularz NP')
def step_valid_login(context):
    context.driver.save_screenshot('foto.png')
    #context.driver.close()
    #assert context.driver.find_element_by_id('calendar')

from behave import given, when, then
import asserts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('Uzytkownik wypelnia pola formularza1 form2')
def step_start_page(context):
    context.driver.get("http://pccorsachelp.compol2.com.pl/phone_book/subscribers/create")
    assert context.driver.find_element_by_id('subscribers-name')

@when(' Uzytkownik wchodzi do zakladki NP form1 form2')
def step_set_login_in(context):
    context.driver.find_element_by_id('subscribers-name').send_keys('Marcin2')
    context.driver.find_element_by_id('subscribers-emailaddress').send_keys('maew1@wp.pl')
    context.driver.find_element_by_id('subscribers-address').send_keys('Os.Rusa1 22/14')
    context.driver.find_element_by_id('subscribers-city').send_keys('Poznań')
    context.driver.find_element_by_id('subscribers-zipcode').send_keys('61-635')
    context.driver.find_element_by_id("subscribernumbers-0-number").send_keys('3445336')


@when('Uzytkownik klika na dodaj form2')
def step_set_login_in_form(context):
    context.driver.find_element_by_id("action-btn").click()
    context.driver.save_screenshot('foto.10._1.png')

@then('Uzytkownik widzi formularz NP NP1 form2')
def step_valid_login(context):
    context.driver.save_screenshot('foto.10_2.png')
    context.driver.close()
    #assert context.driver.find_element_by_id('calendar')

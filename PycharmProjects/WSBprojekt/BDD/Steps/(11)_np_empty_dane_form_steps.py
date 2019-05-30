from behave import given, when, then
import asserts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('Uzytkownik wchodzi na strone formularza NP form3_11')
def step_start_page(context):
    context.driver.get("http://pccorsachelp.compol2.com.pl/phone_book/subscribers/create")
    #assert context.driver.find_element_by_id('subscribers-name')

#@when('Uzytkownik czysci i pozostawia puste pola formularza')
#def step_set_login_in(context):
    #context.driver.find_element_by_id('subscribers-name').clear()
    #context.driver.find_element_by_id('subscribers-emailaddress').clear()
   # context.driver.find_element_by_id('subscribers-address').clear()
    #context.driver.find_element_by_id('subscribers-city').clear()
   #context.driver.find_element_by_id('subscribers-zipcode').clear()
    #context.driver.find_element_by_id("subscribernumbers-0-number").clear()


@when('Uzytkownik klika na dodaj form3_11')
def step_set_login_in_form(context):
    context.driver.find_element_by_id("action-btn").click()


@then('Uzytkownik widzi formularz NP form z komunikatami o putych polach_11')
def step_valid_login(context):
    context.driver.save_screenshot('foto.png')
    assert context.driver.find_elements_by_class_name("alert alert-success alert-dismissible show")
    #context.driver.close()
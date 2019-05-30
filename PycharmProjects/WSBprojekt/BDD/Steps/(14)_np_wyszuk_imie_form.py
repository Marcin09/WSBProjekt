from behave import given, when, then
import asserts
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('Uzytkownik wchodzi na strone formularza NP form_14')
def step_start_page(context):
    context.driver.get("http://pccorsachelp.compol2.com.pl/phone_book/subscribers")
    #assert context.driver.find_element_by_id('subscribers-name')

@when('wyszukiwanie pacjenta imie NP form_14')
def step_set_login_in(context):
    context.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[4]/table/thead/tr[2]/td[3]/input").send_keys("Marcin")
    context.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[4]/table/thead/tr[2]/td[3]/input").send_keys(Keys.ENTER)



@then('Uzytkownik widzi formularz NP form_14')
def step_valid_login(context):
    context.driver.save_screenshot('foto.png')
    #assert context.driver.find_elements_by_id("subscribers-0-name-targ")
    context.driver.close()


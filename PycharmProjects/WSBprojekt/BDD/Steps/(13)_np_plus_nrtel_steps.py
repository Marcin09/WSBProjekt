from behave import given, when, then


@given('Uzytkownik wchodzi na strone formularza NPP form_13')
def step_start_page(context):
    context.driver.get("http://pccorsachelp.compol2.com.pl/phone_book/subscribers/create")
    #assert context.driver.find_element_by_id('subscribers-name')

@when('Uzytkownik wypelnia pola formularza_13')
def step_set_login_in(context):
    context.driver.find_element_by_id('subscribers-name').send_keys("name")
    context.driver.find_element_by_id('subscribers-emailaddress').send_keys("mail")
    context.driver.find_element_by_id('subscribers-address').send_keys("adress 1123")
    context.driver.find_element_by_id('subscribers-city').send_keys("City")
    context.driver.find_element_by_id('subscribers-zipcode').send_keys("ewer")
    context.driver.find_element_by_id("subscribernumbers-0-number").send_keys("cdcecd")
    context.driver.implicitly_wait(2)

@when('Uzytkownik klika na dodaj form_13')
def step_set_login_in_form(context):
    context.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div[1]/div/div/div[2]/button[1]").click()
    context.driver.find_element_by_id("subscribernumbers-1-number").send_keys("123456")
    context.driver.find_element_by_id("action-btn").click()

@then('Uzytkownik widzi dodany nr w formularzu NP form_13')
def step_valid_login(context):
    context.driver.save_screenshot('foto.png')
    #assert context.driver.find_elements_by_class_name("alert alert-success alert-dismissible show")
    #context.driver.close()
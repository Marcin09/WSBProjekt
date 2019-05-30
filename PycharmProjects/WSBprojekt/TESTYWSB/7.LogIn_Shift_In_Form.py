

# Test sprawdza modul logowania z wcisnietym
#przyciskiem Shift

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
PoleLog = driver.find_element_by_id("login-input").send_keys(Keys.SHIFT + 'admin')

PolePass = driver.find_element_by_id("password-input").send_keys(Keys.SHIFT + "pccorsachelp")
#driver.find_element_by_id("password-input").send_keys("pccorsachelp")
button = driver.find_element_by_tag_name("button").click()

driver.implicitly_wait(5)

if len(driver.find_elements_by_id("main-wrapper"))>0:
    print('Logowanie powiodlo sie')
else:
    print('Logowanie nie powiodlo sie')


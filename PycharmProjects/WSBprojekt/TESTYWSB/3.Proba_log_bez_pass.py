

# Test sprawdza modul logowania z wpisaniem
# poprawnego hasla za wyjatkiem loginu


import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
#PoleLog = driver.find_element_by_id("login-input").send_keys("admin")
#PoleLog = driver.find_element_by_id("login-pass").send_keys('admin')

PolePass = driver.find_element_by_id("password-input").send_keys("pccorsachelp")

button = driver.find_element_by_tag_name("button").click()

driver.implicitly_wait(2)

if len(driver.find_elements_by_id("main-wrapper"))>0:
    print('!!!Error!!! - logowanie powiodlo sie')
else:
    print('Test OK - logowanie nie powiodlo sie')


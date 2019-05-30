

# Test sprawdza modul logowania z wpisaniem
# poprawnego loginu za wyjatkiem hasla


import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
PoleLog = driver.find_element_by_id("login-input").send_keys("admin")

PolePass = driver.find_element_by_id("password-input").clear()

button = driver.find_element_by_tag_name("button").click()

driver.implicitly_wait(5)

if len(driver.find_elements_by_id("main-wrapper"))>0:
    print('!!!Error!!! - logowanie powiodlo sie')
else:
    print('Test OK - logowanie nie powiodlo sie')


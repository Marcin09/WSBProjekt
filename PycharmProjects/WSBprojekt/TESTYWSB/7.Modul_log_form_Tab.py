

# Test sprawdza modul logowania z wpisaniem poprawnych danych
# logowania i potwierdznie button ENTER
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
PoleLog = driver.find_element_by_id("login-input").send_keys('admin')

PolePass = driver.find_element_by_id("password-input").send_keys('pccorsachelp')
PolePass = driver.find_element_by_id("password-input").send_keys(Keys.ENTER)


#button = driver.find_element_by_tag_name("button").click()

driver.implicitly_wait(2)

if len(driver.find_elements_by_id("main-wrapper"))>0:
    print('Logowanie powiodlo sie')
else:
    print('Logowanie nie powiodlo sie')


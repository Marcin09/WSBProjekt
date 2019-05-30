#Test sprawdza czy zaladowana strona jest wlasciwa

import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
HomePage = driver.find_element_by_id("wrapper")
driver.implicitly_wait(5)
if len(driver.find_elements_by_id("wrapper"))>0:
    print("strona zaladowala sie poprawnie")
else:
    print('strona nie zaladowala sie')


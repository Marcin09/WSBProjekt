import time
from selenium import webdriver
#from webdriver_manager
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
elementloginu = driver.find_element_by_id("wrapper")




import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
element = driver.find_element_by_id("login-input").click()
element = driver.find_element_by_id("login-input")
element.clear()
element.send_keys('test')
element = driver.find_element_by_id("password-input").click()
elemental = driver.find_element_by_id("password-input")
#elemental.clear()
elemental.send_keys('test1')
button = driver.find_element_by_tag_name("button").click()

#http://pccorsachelp.compol2.com.pl/calendar/new

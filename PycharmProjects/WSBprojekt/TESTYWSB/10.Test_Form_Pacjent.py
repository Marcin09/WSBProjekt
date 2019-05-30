

# wypelnianie formularza nowy pacjent
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
PoleLog = driver.find_element_by_id("login-input").send_keys('admin')
PolePass = driver.find_element_by_id("password-input").send_keys("pccorsachelp")
button = driver.find_element_by_tag_name("button").click()
driver.implicitly_wait(5)

SelPacjent = driver.find_element_by_xpath("/html/body/div[2]/aside/div/div[1]/nav/ul/li[9]/a/span").click()
KsiazkaADres = driver.find_element_by_xpath("/html/body/div[2]/aside/div/div[1]/nav/ul/li[9]/ul/li/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/a").click()
time.sleep(3)
driver.find_element_by_id('subscribers-name').send_keys('Marcin')
driver.find_element_by_id('subscribers-emailaddress').send_keys('mail@wp.pl')
driver.find_element_by_id('subscribers-address').send_keys('Os.Rusa 23/18')
driver.find_element_by_id('subscribers-city').send_keys('Poznań')
driver.find_element_by_id('subscribers-zipcode').send_keys('61-645')
driver.find_element_by_id("subscribernumbers-0-number").send_keys('34456576')

driver.execute_script("window.scrollTo(0, document.body.scrollLow);")
time.sleep(3)

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div[2]/div/button").click()
driver.implicitly_wait(3)
driver.save_screenshot('foto.png')

#driver.close()







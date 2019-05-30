

# Test sprawdza poprawnosc wejscia do ksiazki adresowej
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

driver.save_screenshot('foto.png')
SCROLL_PAUSE_TIME = 2.0

mousescroll = ((driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")) (driver.execute_script("window.scrollTo(0, document.body.scrollLow);")))
SCROLL_PAUSE_TIME = 2.0
mousescroll = ((driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")) (driver.execute_script("window.scrollTo(0, document.body.scrollLow);")))
SCROLL_PAUSE_TIME = 2.0
mousescroll = ((driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")) (driver.execute_script("window.scrollTo(0, document.body.scrollLow);")))
SCROLL_PAUSE_TIME = 2.0
mousescroll = ((driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")) (driver.execute_script("window.scrollTo(0, document.body.scrollLow);")))



driver.close()






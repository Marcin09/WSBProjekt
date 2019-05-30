import time
from selenium import webdriver
#from webdriver_manager
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')
driver.save_screenshot('foto.png')
elementloginu = driver.find_element_by_id("wrapper")
#print (element_loginu == driver.find_element_by_id("wrapper"))
#<<< test wyszukujei zaznacza pole login >>>
element = driver.find_element_by_id("login-input").click()
element = driver.find_element_by_id("login-input")

element.clear() #<<< test czysci pole login >>>

element.send_keys('admin')#<<< test w polu login wpisuje "admin" >>>

elemental = driver.find_element_by_id("password-input").click() #<<< test zaznacza puste pole "password" >>>

elemental = driver.find_element_by_id("password-input")

elemental.clear() #<<< test czysci pole password >>>

elemental = driver.find_element_by_id("password-input")

elemental.send_keys('pccorsachel') #<<< test wpisuje w pole "password" !!nieprawidlowe!!  haslo >>>

button = driver.find_element_by_tag_name("button").click() #<<< test klika w przycisk "zaloguj"

driver.implicitly_wait(5) # <<< test czeka 5 sek na zaladowanie sie strony, nastepnie wykona kolejna instrukcje" >>>
#element_loginu = driver.find_element_by_id("main-wrapper")

if len(driver.find_elements_by_id("main-wrapper"))>0: #<<< instrukja warunkowa - test wyszukuje elementu ID na zaladowanej
    #stronie , celem uwierzytelnienia poprawnosci logowania.>>
    print("jestes zalogowany w panelu uzytkownika")
else:
    elemental = driver.find_element_by_id("password-input")
    elemental.clear()
    elemental = driver.find_element_by_id("password-input").send_keys('pccorsachelp')
    #elemental.send_keys('pccorsachelp')
    button = driver.find_element_by_tag_name("button").click()
    driver.implicitly_wait(20)


if len(driver.find_elements_by_id("main-wrapper"))>0:
    print("jestes zalogowany w panelu uzytkownika")
else:
    print("logowanie nie powiodlo sie ")
assert "No results found." not in driver.page_source
#--------------------------------------------------------------------------------------------------------------------





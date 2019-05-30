import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://pccorsachelp.compol2.com.pl/account/login')


classmethod GetText():
    def text(self):
        baseUrl: "http://pccorsachelp.compol2.com.pl/account/login"
        driver = webdriver.firefox()
        driver.get(baseUrl)

        openTabElement = driver.find_element_by_id('login-input')
        elementText = openTabElement.text
        print("logtext" + elementText)
        tome.sleep(2)
        driver.quit()


#http://pccorsachelp.compol2.com.pl/calendar/new

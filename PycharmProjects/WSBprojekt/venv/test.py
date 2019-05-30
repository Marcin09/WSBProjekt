from selenium import webdriver as wd
driver = wd.Firefox()
driver.get('http://www.wsb.pl')
driver.save_screenshot('screenshot.png')

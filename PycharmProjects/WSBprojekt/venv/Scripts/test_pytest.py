import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Wsb(unittest.TestCase):
    def setUp(self):
        driver = self.driver
        driver.get('http://www.wsb.pl')
        self.assertIn('WSB', driver.title)
        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys('testowanie')
        element.send_keys(Keys.RETURN)
        assert 'Nie znaleziono' not in driver.page_source

  






from selenium import webdriver

from twHomePage import twHomePage
import tribalwars
from locator import Locator

#Test Setup
browser = webdriver.Chrome()
test_value = 'works'

#Test page
testPage = twHomePage(driver=browser)

testPage.go()










from selenium.webdriver.common.by import By

from pageObjects.BaseElement import BaseElement


class LoginPage(BasePage):

    url = 'https://tribalwars.co.uk'

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.tribalwars.co.uk/'

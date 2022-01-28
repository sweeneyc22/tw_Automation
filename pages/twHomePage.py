from selenium.webdriver.common.by import By

from BasePage import BasePage
from BaseElement import BaseElement
from locator import Locator

#Build Tribal Wars Login screen
#Inheriting from BasePage
#__init__ from BasePage
class twHomePage(BasePage):

    url = 'https://www.tribalwars.co.uk'

    @property
    def loginButton(self):
        locator = Locator(By.CSS_SELECTOR, '#login_form > div > div > a')
        return BaseElement(
        driver=self.driver,
            locator=locator
        )


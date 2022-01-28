from locator import Locator
#What should every page be able to do/have?
class BasePage(object):
    url = None

    #Construct Page object
    def __init__(self, driver):
        self.driver = driver


    def go(self):
        self.driver.get(self.url)


    #Refresh

    #Check for Captcha


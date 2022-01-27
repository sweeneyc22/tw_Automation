from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.tribalwars.co.uk/'


    def go(self):
        self.driver.get(self.url)

    def writeUsername(self, text):
        box = self.driver.find_element(By.CSS_SELECTOR, "#user")
        box.clear()
        box.send_keys(text)
        return None

    def writePassword(self, text):
        box = self.driver.find_element(By.CSS_SELECTOR, "#password")
        box.send_keys(text)
        return None

    def getUserText(self):
        text = self.driver.find_element(By.CSS_SELECTOR, "#user")
        textValue = text.get_attribute('value')
        return textValue

    def getPassText(self):
        text = self.driver.find_element(By.CSS_SELECTOR, "#password")
        textValue = text.get_attribute('value')
        return textValue

    def clickLoginButton(self):
        loginButton = self.driver.find_element(By.CLASS_NAME, "btn-login")


browser = webdriver.Chrome()
test_Value = " pls work "

#Test 2
loginPage = LoginPage(driver=browser)
loginPage.go()
loginPage.writeUsername(test_Value)
loginPage.writePassword(test_Value)

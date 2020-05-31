import utilities.CustomLogger as cl
import logging
from base.basePage import BasePage
from pages.home_package.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #locators
    _login_link = "//a[@class='navbar-link fedora-navbar-link']"
    _email_field = "//*[@id='user_email']"
    _password_field = "//*[@id='user_password']"
    _login_button = "//*[@name='commit']"

    def clickLoginLink(self):
        self.clickElement(self._login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLogin(self):
        self.clickElement(self._login_button)

    def logging(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLogin()

    def clearing(self):
        self.clearField(self._email_field)
        self.clearField(self._password_field)

    def verifyLogin(self):
        verifier = self.isElementPresent("//img[@class='gravatar']")
        return verifier

    def verifyLoginFailed(self):
        verifier = self.isElementPresent("//div[contains(text(), 'Invalid email or password.')]")
        return verifier

    def verifyLoginTitle(self):
        #return self.verifyPageTitle("Google")
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigationToIconProfile()
        self.clickElement("//a[@href='/sign_out']")
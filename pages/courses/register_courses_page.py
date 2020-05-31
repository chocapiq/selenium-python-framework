import utilities.CustomLogger as cl
import logging
from base.basePage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_button = "//*[@name='commit']"
    _search_box = "//*[@id='search-courses']"
    _course = "//div[@data-course-id='56740']"
    _enroll_button = "//button[@id='enroll-button-top']"
    _cc_num = "//div//span//div//input[@name='cardnumber']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _cc_post = "//input[@name='postal']"
    _terms_checkbox = "//input[@id='agreed_to_terms_checkbox']"
    _submit_enroll = "//label[@for='spc-primary-submit']"
    _enroll_error_message = "//div[@class='payment-error-box only-on-mobile']"


    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)
        cCN = self.getElement("//div[contains(text(),'" + name + "')]")
        cCN.click()

    def clickEnrollButton(self):
        self.clickElement(self._enroll_button)

    def creditCardNumber(self, num):
        self.switchToFrame("//iframe[@name='__privateStripeFrame12']")
        self.waitForElement(self._cc_num)
        self.webScroll(self._cc_num)
        self.sendKeys(num, self._cc_num)
        self.driver.switch_to.default_content()

    def creditCardExp(self, exp):
        self.switchToFrame("//iframe[@name='__privateStripeFrame13']")
        self.waitForElement(self._cc_exp)
        self.sendKeys(exp, self._cc_exp)
        self.driver.switch_to.default_content()

    def creditCardCVV(self, cvv):
        self.switchToFrame("//iframe[@name='__privateStripeFrame14']")
        self.waitForElement(self._cc_cvv)
        self.sendKeys(cvv, self._cc_cvv)
        self.driver.switch_to.default_content()

    def cityPost(self, post):
        self.switchToFrame("//iframe[@name='__privateStripeFrame15']")
        #self.SwitchFrameByIndex(self._cc_post)
        self.waitForElement(self._cc_post)
        self.sendKeys(post, self._cc_post)
        self.driver.switch_to.default_content()

    def enterCreditCardInfo(self, num, exp, cvv, post):
        self.creditCardNumber(num)
        self.creditCardExp(exp)
        self.creditCardCVV(cvv)
        self.cityPost(post)

    def clickTermsCheckbox(self):
        self.clickElement(self._terms_checkbox)

    def clickEnrollSubmitButton(self):
        self.clickElement(self._submit_enroll)

    def verifyEnrollFailed(self):
        verify = self.isElementPresent('//button[@class="btn btn-primary spc__button is-disabled"]')
        return verify

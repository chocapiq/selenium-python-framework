from pages.home_package.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clearing()
        self.lp.logging("test@email.com", "abcabc")
        result2 = self.lp.verifyLoginTitle()
        self.ts.mark(result2, "Title verification.")
        result3 = self.lp.verifyLogin()
        self.ts.markFinal("test_validLogin", result3, "Login verification.")

    @pytest.mark.run(order=1)
    def test_failedLogin(self):
        self.lp.logout()
        self.lp.logging("test@email.com", "abcaaabc")
        result1 = self.lp.verifyLoginFailed()
        self.ts.mark(result1, "Testing login to fail.")
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def testInvalidEnrollment(self):
        self.courses.enterCourseName("JavaScript for")
        self.courses.clickEnrollButton()
        self.courses.enterCreditCardInfo("4280323963876221", "0521", "192", "00-001")
        self.courses.clickTermsCheckbox()
        self.courses.clickEnrollSubmitButton()
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("testInvalidEnrollment", result1, "Verify if fake card makes button enabled.")

from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class MultipleDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4280323963876221", "0521", "192", "00-001"), ("Complete Test Automation Bundle", "4280323963876221", "0622", "111", "00-002"))
    @unpack
    def testInvalidEnrollment(self, courseName, num, exp, cvv, post):
        self.courses.enterCourseName(courseName)
        self.courses.clickEnrollButton()
        self.courses.enterCreditCardInfo(num, exp, cvv, post)
        self.courses.clickTermsCheckbox()
        self.courses.clickEnrollSubmitButton()
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("testInvalidEnrollment", result1, "Verify if fake card makes button enabled.")
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
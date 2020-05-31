from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home_package.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ReadFromCSVTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/pawel/PycharmProjects/letskodeit/testdata.csv"))
    @unpack
    def testInvalidEnrollment(self, courseName, num, exp, cvv, post):
        self.courses.enterCourseName(courseName)
        self.courses.clickEnrollButton()
        self.courses.enterCreditCardInfo(num, exp, cvv, post)
        self.courses.clickTermsCheckbox()
        self.courses.clickEnrollSubmitButton()
        result1 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("testInvalidEnrollment", result1, "Verify if fake card makes button enabled.")
        self.nav.navigationToIcon()
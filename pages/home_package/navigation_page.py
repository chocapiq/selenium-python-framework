import utilities.CustomLogger as cl
import logging
from base.basePage import BasePage

class NavigationPage(BasePage):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators for https://letskodeit.teachable.com/
    _icon = "//a[@class='navbar-brand header-logo']"
    _practice_page = "Practice"
    _login_page = "//a[@class='navbar-link fedora-navbar-link']"
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _icon_profile = "//a[@class='fedora-navbar-link navbar-link dropdown-toggle open-my-profile-dropdown']"

    def navigationToIcon(self):
        self.clickElement(self._icon)

    def navigationToPracticePage(self):
        self.clickElement(self._practice_page, locatorType="link")

    def navigationToLoginPage(self):
        self.clickElement(self._login_page)

    def navigationToMyCourses(self):
        self.clickElement(self._my_courses, locatorType="link")

    def navigationToAllCourses(self):
        self.clickElement(self._all_courses, locatorType="link")

    def navigationToIconProfile(self):
        self.clickElement(self._icon_profile)
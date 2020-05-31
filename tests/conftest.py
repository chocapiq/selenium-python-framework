import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home_package.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Running method level SetUp")
    yield
    print("Running method level TearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("*Running one time method level SetUp*")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.logging("kappa123@gmail.com", "kappakappa")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("*Running one time method level TearDown*")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

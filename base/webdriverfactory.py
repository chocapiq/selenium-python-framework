from selenium import webdriver

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = "https://letskodeit.teachable.com/"
        if self.browser == "ie":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        return driver
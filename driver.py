from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumDriver():
    def get_driver_options(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.headless = False
        return options

    def get_instance(self):
        driver = webdriver.Chrome(options=self.get_driver_options())
        driver.maximize_window()
        return driver
    

selenium_driver = SeleniumDriver()
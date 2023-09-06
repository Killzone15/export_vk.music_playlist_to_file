from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service


class Browser:

    def __init__(self, url, timeout=10):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users\\Yuri\\AppData\\Local\\Google\\Chrome\\User Data")
        service = Service(executable_path=binary_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)
        self.browser = driver
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

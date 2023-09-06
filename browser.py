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

    def find_element_is_present(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def find_elements_is_present(self, how, what):
        try:
            elements = self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return elements

    def scroll_element_to_bottom(self, element):
        current_height = self.execute_script("return arguments[0].scrollHeight;", element)

        while True:
            self.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)
            self.implicitly_wait(3)  # Ждем некоторое время для загрузки контента внутри элемента

            new_height = self.execute_script("return arguments[0].scrollHeight;", element)
            if new_height == current_height:
                break

            current_height = new_height

import time, os
from selenium.common import NoSuchElementException
from selenium import webdriver
import chromedriver_autoinstaller
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service


class Browser:

    def __init__(self, url, timeout=10):
        options = webdriver.ChromeOptions()
        user_name = os.getlogin()
        options.add_argument(f"user-data-dir=C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data")
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

    def scroll_element_to_bottom(self):

        previous_page_height = self.browser.execute_script("return document.body.scrollHeight")

        while True:
            # Прокручиваем страницу до конца
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Ждем некоторое время (можно настроить под свои нужды)
            time.sleep(2)

            # Получаем текущую высоту страницы
            current_page_height = self.browser.execute_script("return document.body.scrollHeight")

            # Если высота изменилась, это может указывать на обновление контента
            if current_page_height > previous_page_height:
                print("Контент обновился. Продолжаем прокручивать страницу.")
                previous_page_height = current_page_height
            else:
                print("Контент больше не обновляется. Завершаем скрипт.")
                time.sleep(2)
                break

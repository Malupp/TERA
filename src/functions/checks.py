from selenium.common.exceptions import NoSuchElementException
from config.driver import WebDriverManager
from interactions import Interactions

class Checks:
    @staticmethod
    def check_xpath(xpath):
        try:
            elem = WebDriverManager.return_driver().find_element("xpath", xpath)
            print(f"Element found: {xpath}")
            return elem
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            return None

    @staticmethod
    def check_existence(xpath):
        try:
            elem = WebDriverManager.return_driver().find_element("xpath", xpath)
            print(f"{xpath} is present")
            if elem.is_displayed():
                
                Interactions.screenshot_element(xpath)
        except NoSuchElementException:
            print(f"{xpath} isn't present")
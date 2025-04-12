from turtledemo.sorting_animate import start_ssort

from selenium.common.exceptions import NoSuchElementException
from config.driver import WebDriverManager
from interactions import Interactions

class Checks:
    @staticmethod
    def check_xpath(xpath):
        try:
            elem = Interactions.find_element(xpath)
            print(f"Element found: {xpath}")
            return elem
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            return None

    @staticmethod
    def is_element_displayed(xpath):
        try:
            elem = Interactions.find_element(xpath)
            if elem.is_displayed():
                print(f"{xpath} is visible")
            else:
                print(f"{xpath} is hidden")
        except NoSuchElementException:
            print(f"{xpath} isn't present")

    @staticmethod
    def check_existence_with_screenshot(xpath):
        try:
            elem = Interactions.find_element(xpath)
            print(f"{xpath} is present")
            if elem.is_displayed():
                Interactions.screenshot_element(xpath)
        except NoSuchElementException:
            print(f"{xpath} isn't present")

    @staticmethod
    def is_element_enabled(xpath):
        try:
            elem = Interactions.find_element(xpath)
            print(f"{xpath} is present")
            if elem.is_displayed():
                if elem.is_enabled():
                    print("The element is enabled")
                else:
                    print("The element is disabled")
            else:
                print("The element is not visible")
        except NoSuchElementException:
            print(f"{xpath} isn't present")

    @staticmethod
    def check_element_status(xpath):
        try:
            elem = Interactions.find_element(xpath)
            print(f"Element found: {xpath}")

            # Visibility
            if elem.is_displayed():
                print(" → Element is visible")
            else:
                print(" → Element is NOT visible")

            # Enabled
            if elem.is_enabled():
                print(" → Element is enabled")
            else:
                print(" → Element is DISABLED")

            # Selected
            if elem.is_selected():
                print(" → Element is SELECTED")
            else:
                print(" → Element is NOT selected")

        except NoSuchElementException:
            print(f"Element NOT found: {xpath}")
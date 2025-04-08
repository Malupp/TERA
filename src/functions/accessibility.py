from selenium.common.exceptions import NoSuchElementException
from src.functions.interactions import Interactions
from colour import Color
from color_contrast import AccessibilityLevel, check_contrast

class Accessibility:
    @staticmethod
    def check_element_by_aria_label(label_text):
        xpath = (
            f"//*[contains(@aria-label, '{label_text}')]"
            f"|//*[contains(@aria-label, '{label_text.lower()}')]"
            f"|//*[contains(@aria-label, '{label_text.upper()}')]"
        )
        try:
            elem = Interactions.find_element(xpath)
            if elem:
                print(f"Element found with aria-label: {label_text}")
                return True
        except NoSuchElementException:
            pass
        print(f"Element not found (aria-label): {label_text}")
        return False

    @staticmethod
    def check_accessibility_attributes(xpath):
        try:
            elem = Interactions.find_element(xpath)
            has_alt = elem.get_attribute("alt") is not None
            has_aria = elem.get_attribute("aria-label") is not None
            has_title = elem.get_attribute("title") is not None
            has_role = elem.get_attribute("role") is not None

            if has_alt or has_aria or has_title or has_role:
                print(f"Element has accessibility attributes: {xpath}")
                return True
            else:
                print(f"Element missing accessibility attributes: {xpath}")
                return False
        except NoSuchElementException:
            print(f"Element not found for accessibility check: {xpath}")
            return False

    @staticmethod
    def get_element_color(driver, element, css_property):
        color_value = element.value_of_css_property(css_property)
        return Color(color_value)

    @staticmethod
    def check_color_contrast(driver, element1, element2, level=AccessibilityLevel.AA):
        color1 = driver.get_element_color(driver, element1, 'color')
        color2 = driver.get_element_color(driver, element2, 'background-color')
        return check_contrast(color1, color2, level=level)

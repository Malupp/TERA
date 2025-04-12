## Here there will be only interaction methods ##
### Clicking, input and other stuff like that ###

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import pyautogui
import time, os, random, string

from twisted.web.domhelpers import findElements

from config.driver import WebDriverManager

class Interactions:
    contatoreScreenshot = 1

    @staticmethod
    def find_element(xpath):
        try:
            elem = WebDriverManager.return_driver().find_element(By.XPATH, xpath)
            print(f"Element found: {xpath}")
            return elem
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            return None

    @staticmethod
    def click_element(xpath):
        try:
            elem = Interactions.find_element(xpath)
            if elem:
                Interactions.wait(2)
                elem.click()
                Interactions.wait(2)
                print(f"Element clicked: {xpath}")
        except NoSuchElementException:
            print(f"Element not clicked: {xpath}")

    @staticmethod
    def click_element_by_text(text):
        try:
            xpath = (
                f"//*[contains(text(), '{text}')]"
                f"|//*[contains(text(), '{text.lower()}')]"
                f"|//*[contains(text(), '{text.upper()}')]"
            )
            elem = Interactions.find_element(xpath)
            if elem:
                Interactions.wait(2)
                elem.click()
                Interactions.wait(2)
                print(f"Element clicked with text: {text}")
        except NoSuchElementException:
            print(f"Element not clicked: {text}")


    @staticmethod
    def check_element_by_text(text):
        xpath = (
            f"//*[contains(text(), '{text}')]"
            f"|//*[contains(text(), '{text.lower()}')]"
            f"|//*[contains(text(), '{text.upper()}')]"
        )
        try:
            elem = Interactions.find_element(xpath)
            if elem:
                print(f"Element found with text: {text}")
                return True
        except NoSuchElementException:
            pass
        print(f"Element not found: {text}")
        return False

    @staticmethod
    def check_element_by_placeholder(text):
        xpath = (
            f"//*[[contains(@placeholder, '{text}')]"
            f"|//*[contains(@placeholder, '{text.lower()}')]"
            f"|//*[contains(@placeholder, '{text.upper()}')]"
        )
        try:
            elem = Interactions.find_element(xpath)
            if elem:
                print(f"Element found with placeholder: {text}")
                return True
        except NoSuchElementException:
            pass
        print(f"Element not found (placeholder): {text}")
        return False

    @staticmethod
    def click_if_present(xpath):
        elem = Interactions.find_element(xpath)
        if elem and elem.is_displayed():
            Interactions.wait(2)
            elem.click()
            print(f"Element clicked: {xpath}")
        else:
            print(f"Element not clicked: {xpath}")

    @staticmethod
    def click_with_retry(xpath, timeout=5, retries=3):
        driver = WebDriverManager.return_driver()
        for attempt in range(retries):
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                element.click()
                return True
            except Exception as e:
                if attempt == retries - 1:  # Last attempt
                    raise
                time.sleep(1)  # Brief pause before retry
        return False

    @staticmethod
    def scroll_to_element(xpath):
        elem = Interactions.find_element(xpath)
        actions = ActionChains(WebDriverManager.return_driver())
        actions.move_to_element(elem).perform()

    @staticmethod
    def scroll_click_element(elem):
        ActionChains(WebDriverManager.return_driver()).move_to_element(elem).click().perform()
        print("trying to find element with a scroll and click it")

    @staticmethod
    def scroll_down(times=1):
        body = WebDriverManager.return_driver().find_element(By.TAG_NAME, 'body')
        for _ in range(times):
            body.send_keys(Keys.PAGE_DOWN)

    @staticmethod
    def scroll_up(times=1):
        body = WebDriverManager.return_driver().find_element(By.TAG_NAME, 'body')
        for _ in range(times):
            body.send_keys(Keys.PAGE_UP)

    @staticmethod
    def input_text(xpath, text):
        try:
            driver = WebDriverManager.return_driver()
            elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            elem.click()
            print(f"clicking the element...{xpath}")
            elem.clear()
            print(f"clearing the input text...{xpath}")
            elem.send_keys(text)
            print(f"sending text in...{xpath}")
        except Exception as e:
            print(f"Error to input the text in '{xpath}': {e}")

    @staticmethod
    def input_text_by_placeholder(placeholder_text, text_to_send):
        try:
            xpath = (
                f"//*[contains(@placeholder, '{placeholder_text}')]"
                f"|//*[contains(@placeholder, '{placeholder_text.lower()}')]"
                f"|//*[contains(@placeholder, '{placeholder_text.upper()}')]"
            )
            driver = WebDriverManager.return_driver()
            elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))

            elem.click()
            print(f"Clicking input with placeholder: {placeholder_text}")
            elem.clear()
            print(f"Clearing input with placeholder: {placeholder_text}")
            elem.send_keys(text_to_send)
            print(f"Sending text '{text_to_send}' to input with placeholder: {placeholder_text}")
        except Exception as e:
            print(f"Error to input text in field with placeholder '{placeholder_text}': {e}")

    @staticmethod
    def input_text_force(xpath, text):
        try:
            driver = WebDriverManager.return_driver()
            elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            driver.execute_script("arguments[0].removeAttribute('disabled')", elem)
            elem.click()
            elem.clear()
            elem.send_keys(text)
        except Exception as e:
            print(f"Error to input the text in '{xpath}': {e}")

    @staticmethod
    def switch_to_frame(name):
        try:
            WebDriverManager.return_driver().switch_to.frame(name)
            print(f"Switching to the frame: '{name}'")
        except Exception:
            print(f"Impossible to switch to the frame")

    @staticmethod
    def return_to_main():
        try:
            WebDriverManager.return_driver().switch_to.default_content()
            print("Switching to the main frame")
        except Exception:
            print(f"Impossible to switch to the MAIN frame")

    @staticmethod
    def press_enter():
        actions = ActionChains(WebDriverManager.return_driver())
        actions.send_keys(Keys.ENTER).perform()
        print("Press Enter")

    @staticmethod
    def wait(seconds):
        time.sleep(seconds)
        print(f"Waiting: {seconds} seconds...")

    @staticmethod
    def wait_until(timeout, condition):
        WebDriverWait(WebDriverManager.return_driver(), timeout).until(condition)

    @staticmethod
    def take_screenshot(name, folder="screenshots"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        timestamp = datetime.now().isoformat(timespec='seconds').replace(':', '-')
        filename = f"{name}_{Interactions.contatoreScreenshot}_{timestamp}.png"
        path = os.path.join(folder, filename)
        WebDriverManager.return_driver().save_screenshot(path)
        print(f"Screenshot saved: {path}")
        Interactions.contatoreScreenshot += 1

    @staticmethod
    def screenshot_element(xpath, folder="screenshots"):
        try:
            elem = WebDriverManager.return_driver().find_element(By.XPATH, xpath)
            if not os.path.exists(folder):
                os.makedirs(folder)
            timestamp = datetime.now().isoformat(timespec='seconds').replace(':', '-')
            filename = f"{Interactions.contatoreScreenshot}_{timestamp}.png"
            path = os.path.join(folder, filename)
            elem.screenshot(path)
            print(f"Screenshot saved: {path}")
            Interactions.contatoreScreenshot += 1
            return path
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
            return None
        
    @staticmethod
    def refreshing_page():
        WebDriverManager.return_driver().refresh()
        print("Reloading browser page...")

    @staticmethod
    def go_forward():
        WebDriverManager.return_driver().forward()
        print("Going to the next page...")

    @staticmethod
    def go_back():
        WebDriverManager.return_driver().back()
        print("Going to the previous page...")

    @staticmethod
    def importoRandom():
        # Genera un numero con la virgola a 2 cifre da 1 a 100
        importo = round(random.uniform(1, 100), 2)
        print(importo)
        return importo

    @staticmethod
    def randomText():
        text = ''.join(random.choices(string.ascii_lowercase, k=5))
        return text

    @staticmethod
    def return_title_site():
        WebDriverManager.return_driver().title()

    @staticmethod
    def get_source_page():
        WebDriverManager.return_driver().page_source()

    @staticmethod
    def get_location_element(xpath):
        elem = Interactions.find_element(xpath)
        if elem and elem.is_displayed():
            Interactions.wait(2)
            point = elem.location
            print(f"X coordinate: {point['x']} Y coordinate: {point['y']}")

    @staticmethod
    def click_by_coordinates(x, y):
        screen_width, screen_height = pyautogui.size()
        if 0 <= x <= screen_width and 0 <= y <= screen_height:
            print(f"Clicking X: {x}, Y: {y} (Resolution: {screen_width}x{screen_height})")
            Interactions.wait(2)
            #The mouse will hover over the indicated position
            pyautogui.moveTo(x, y)
            pyautogui.click()
        else:
            print(f"Coordinates out of window: X={x}, Y={y}")

    @staticmethod
    def click_if_enabled(xpath):
        try:
            elem = Interactions.find_element(xpath)
            if elem.is_displayed():
                if elem.is_enabled():
                    elem.click()
                    print(f"Clicked on: {xpath}")
                else:
                    print(f"Element is disabled: {xpath}")
            else:
                print(f"Element is not visible: {xpath}")
        except NoSuchElementException:
            print(f"Element not found: {xpath}")
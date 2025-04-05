## Here there will be only interaction methods ##
### Clicking, input and other stuff like that ###

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time, os

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
    def click_if_present(xpath):
        elem = Interactions.find_element(xpath)
        if elem and elem.is_displayed():
            Interactions.wait(2)
            elem.click()
            print(f"Element clicked: {xpath}")
        else:
            print(f"Element not clicked: {xpath}")

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
            elem.clear()
            elem.send_keys(text)
        except Exception as e:
            print(f"Error to input the text in '{xpath}': {e}")

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
        WebDriverManager.return_driver().navigate().refresh()
        print("Reloading browser page...")
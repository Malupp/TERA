from config import requestsUrl
from src.pages.googleSearch import GoogleSearch
from src.functions.interactions import Interactions
class LoginSteps:
    def __init__(self, driver):
        self.driver = driver  # Store the driver for reuse

    @staticmethod
    def navigateTo(site):
        requestsUrl.getURL(f'{site}')

    @staticmethod
    def loginExample():
        try:
            LoginSteps.navigateTo("www.google.it")
            Interactions.click_element(GoogleSearch.rifiutaTutto)
            Interactions.input_text(GoogleSearch.inputArea, "Demo")
            Interactions.press_enter()

        except Exception as e:
            print(f"ERRORE: {e}")
        
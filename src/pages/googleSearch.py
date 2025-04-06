## Example of a locator class, you must save here or in other pages like this your xpath and you can reuses in every part of the project
from config import requestsUrl
from src.functions.interactions import Interactions

class GoogleSearch:
    searchButton = "//button[@aria-label='Cerca']"
    inputArea = "//textarea[@id='APjFqb']"
    rifiutaTutto = "//button[@id='W0wltc']"

    def __init__(self, driver):
        self.driver = driver  # Store the driver for reuse

    @staticmethod
    def navigateTo(site):
        requestsUrl.getURL(f'{site}')

    @staticmethod
    def loginExample():
        try:
            GoogleSearch.navigateTo("www.google.it")
            Interactions.click_element(GoogleSearch.rifiutaTutto)
            Interactions.input_text(GoogleSearch.inputArea, "Demo")
            Interactions.wait(3)
            Interactions.press_enter()

        except Exception as e:
            print(f"ERRORE: {e}")

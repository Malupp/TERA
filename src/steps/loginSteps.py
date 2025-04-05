from config import requestsUrl
from src.pages.googleSearch import GoogleSearch
from functions.interactions import *
class LoginSteps:

    @staticmethod
    def navigateTo(site):
        requestsUrl.getURL(f'{site}')

    def loginExample(self):
        try:
            self.navigateTo("www.google.it")
            Interactions.click_element(GoogleSearch.searchButton)

        except Exception as e:
            # se qualcosa non va lo dice qui
            print(f"ERRORE: {e}")
        
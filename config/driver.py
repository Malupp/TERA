from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class WebDriverManager:
    _driver = None  # Variabile privata per mantenere un'unica istanza
    _browser_type = None
    _browser = None
    _driver_inuse = None

    @classmethod
    def get_driver(cls, browser_type):
        """Restituisce un'unica istanza del driver"""
        if cls._driver is None:
            cls._browser_type = browser_type
            if browser_type == "chrome":
                chrome_options = ChromeOptions()
                chrome_options.add_argument("--disable-notifications")  # Disabilita notifiche
                chrome_options.add_argument("--disable-popup-blocking")  # Disabilita popup
                chrome_options.add_argument(
                    "--disable-infobars")  # Rimuove il messaggio "Chrome is being controlled by automated test software"
                chrome_options.add_argument("--disable-autofill-dropdown")  # Rimuove popup di autoill
                chrome_options.add_argument(
                    "--disable-save-password-bubble")  # Rimuove popup di salvataggio del metodo di pagamento
                chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
                chrome_options.add_experimental_option("useAutomationExtension", False)
                chrome_options.add_experimental_option("detach", True)
                chrome_options.add_experimental_option("prefs", {
                    "profile.default_content_setting_values.notifications": 2,  # 2 = Blocca notifiche
                    "profile.default_content_setting_values.popups": 2,  # 2 = Blocca popup
                    "credentials_enable_service": False,  # Disabilita salvataggio credenziali
                    "profile.password_manager_enabled": False  # Disabilita il gestore delle password
                })
                cls._driver = webdriver.Chrome(service=Service(), options=chrome_options)


            elif browser_type == "firefox":
                firefox_options = FirefoxOptions()
                cls._driver = webdriver.Firefox(service=Service(), options=firefox_options)
                firefox_options.set_preference("dom.webnotifications.enabled", False)  # Disabilita notifiche
                firefox_options.set_preference("dom.disable_open_during_load", True)  # Blocca popup
                firefox_options.set_preference("signon.rememberSignons", False)  # Disabilita salvataggio password
                firefox_options.set_preference("permissions.default.desktop-notification",
                                               2)  # Blocca notifiche desktop

            elif browser_type == "edge":
                edge_options = EdgeOptions()
                cls._driver = webdriver.Edge(service=Service(), options=edge_options)

            elif browser_type == "safari":
                cls._driver = webdriver.Safari()

            else:
                raise ValueError(f"Browser '{browser_type}' non supportato")

            cls._driver_inuse = cls._driver
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """Chiude e resetta il driver"""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def define_browser(cls):
        return cls._browser_type

    @classmethod
    def return_driver(cls):
        return cls._driver_inuse
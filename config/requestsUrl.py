import os
import time
from config.driver import WebDriverManager

#In order to use this methods you should have a .env in which you indicate what URL wants to navigate
def getPrivateURL(url_key):
    driver = WebDriverManager.return_driver()
    url = os.getenv(url_key)
    if not url:
        raise ValueError("URL not found in environment variables")

    # print(url)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    return

def getURL(url_key):
    driver = WebDriverManager.return_driver()
    url = url_key
    if not url:
        raise ValueError("URL not specified")
    # print(url)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    return
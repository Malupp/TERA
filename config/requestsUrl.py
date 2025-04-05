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


def getURL(url):
    driver = WebDriverManager.return_driver()
    if not url:
        raise ValueError("URL not specified")

    # Ensure URL starts with http:// or https://
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"  # Default to HTTPS

    driver.get(url)
    driver.maximize_window()
    time.sleep(5)  # Consider replacing with WebDriverWait for better reliability
    return
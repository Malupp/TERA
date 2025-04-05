import urllib3
import os

import requests
from dotenv import load_dotenv

# ------NOTA------- dump di configurazioni e roba da importare altrove. metti nel modulo che vuoi import config e sei ok


load_dotenv()
BT=os.getenv("BT")
PIN=os.getenv("PIN")
urlots=os.getenv("urlOTS")
headers=os.getenv("headers")
data=os.getenv("data")

# Disabilita gli avvisi SSL per tutte le richieste HTTP nel progetto
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


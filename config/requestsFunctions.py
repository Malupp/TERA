import json
import os
import re
import time
import requests
import urllib3
from fixtures import config
from fixtures.driver import WebDriverManager



def get_ots(codice_arr):
    url = os.getenv("urlOTS")
 
    data = {
        "canaleOrig": "HI",
        "canaleProv": "AG",
        "id": codice_arr,
        "resultLimit": "1"
    }
    # data= os.getenv("data")
    # data= data.replace("codice_arr",codice_arr)
    print(data)
 
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=UTF-8"
    }

    url_proxy ={
    "http": "http://10.17.79.235:8080"
    }

 
    try:
        print("Dati inviati:", data)  # Debug
        response = requests.post(url, json=data, headers=headers, proxies=url_proxy, verify=False)
 
        print("Risposta ricevuta:", response.text)  # Debug della risposta
 
        if response.status_code == 200:
            response_data = response.json()
            time.sleep(5)
            codes = response_data.get("codes", [])
 
            if codes:
                msg_text = codes[0].get("msgText", "")
 
                if msg_text:
                    match = re.search(r"Codice:\s(\d{6})", msg_text)
                    if match:
                        codice = match.group(1)
                        print("Codice trovato:", codice)
                        return codice
                    else:
                        print("Codice non trovato nel msgText.")
                else:
                    print("msgText non trovato in 'codes'.")
            else:
                print("Lista 'codes' vuota. Nessun codice trovato.")
 
        else:
            print(f"Errore HTTP: {response.status_code}")
 
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta: {e}")
 
    return ""

def forceDevice(codice_arr):
    try:
        # Dati da inviare nel corpo della richiesta
        data = {
            "revoke": False,
            "userAggiorna": "null",
            "userID": codice_arr
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        url = "https://core-wfcbu-v1-cbmu0-test.cloudapps-test.intesasanpaolo.com/toolForzature/forzaDevice"

        # Effettua la richiesta POST
        response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
        
        status_code = response.status_code
        response_text = response.text

        # Cerca il pattern "esito"
        esito_pattern = r'"esito":\s*(\d+)'
        matcher = re.search(esito_pattern, response_text)

        if matcher:
            esito = matcher.group(1)
            print(f"Device non verificato. Esito: {esito}")

            if status_code == 200 and esito == "0":
                print(f"Device verificato con successo. Esito: {esito}")
            else:
                print(f"Errore, device non verificato. Stato HTTP: {status_code}, Esito: {esito}")

    except Exception as e:
        # Log dell'errore senza interrompere l'esecuzione
        print("Si è verificato un errore durante la verifica del device: ", exc_info=True)

def getBT():
    return config.BT

def getPIN():
    return config.PIN

def getURL(url_key):
    driver = WebDriverManager.return_driver()
    url = os.getenv(url_key)
    if not url:
        raise ValueError("URL not found in environment variables")

    # print(url)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    return

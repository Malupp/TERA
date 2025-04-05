from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import string
import time
import random
from fixtures.driver import WebDriverManager
from datetime import datetime
import os



# Ottieni il driver tramite WebDriverManager

# Funzione per cercare un elemento tramite XPath
def findElement(element_id):
    try:
        elem = WebDriverManager.return_driver().find_element(By.XPATH, element_id)
        print(f"Elemento trovato: {element_id}")
        return elem
    except NoSuchElementException:
        print(f"Elemento non trovato: {element_id}")
        return None

# Funzione per cliccare un elemento, dato il suo XPath
def clickElement(element_id):
    try:
        elem = findElement(element_id)
        if elem:
            waitSeconds(2)
            elem.click()
            waitSeconds(2)
            print(f"Elemento cliccato: {element_id}")
    except NoSuchElementException:
        print(f"Elemento non trovato: {element_id}")
        return None
    
def clickElementIfPresent(element_id):
        elem = findElement(element_id)
        if elem.is_displayed():
            waitSeconds(2)
            elem.click()
            print(f"Elemento cliccato: {element_id}")
        else:
            print(f"Elemento non trovato: {element_id}")


# Funzione per fare uno scroll della pagina fino al fondo
def scrollDownUntilTheEnd():
    WebDriverManager.return_driver().execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scrollToTheElement(element_id):
    elem = findElement(element_id) 
    actions = ActionChains(WebDriverManager.return_driver())
    actions.move_to_element(elem).perform()

def scrollDown(times):
    body = WebDriverManager.return_driver().find_element(By.TAG_NAME, 'body')
    for x in range(times):
        body.send_keys(Keys.PAGE_DOWN)

def scrollUp(times):
    body = WebDriverManager.return_driver().find_element(By.TAG_NAME, 'body')
    for x in range(times):
        body.send_keys(Keys.PAGE_UP)

# Funzione per verificare la presenza di un elemento tramite XPath e restituirlo
def checkXpath(element):
    try:
        elem = findElement(element)
        print(f"Elemento trovato: {element}")
        return elem
    except NoSuchElementException:
        print(f"Elemento non trovato: {element}")
        return None

# Funzione per fare una pausa di un numero specificato di secondi
def waitSeconds(seconds):
    time.sleep(seconds)
    print(f'Aspetto: {seconds} secondi')

# Funzione per aspettare che una condizione diventi vera dopo un determinato timeout
def waitSecondsUntilTrue(timeout, condition):
    WebDriverWait(WebDriverManager.return_driver(), timeout).until(condition)


# questa funzione fa uno screenshot e li numera attravero il contatore inizializzato a 1, continua ad aumentare fintanto che il test va
contatoreScreenshot = 1
def screenshot(name, folder="screenshots"):
    global contatoreScreenshot  # Uso della variabile globale contatore
    # Crea la cartella se non esiste
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Genera il nome del file con timestamp
    timestamp = datetime.now().isoformat(timespec='seconds').replace(':', '-')
    filename = f"{name}_{contatoreScreenshot}_{timestamp}.png"
    # Percorso completo del file
    filepath = os.path.join(folder, filename)
    # Salva lo screenshot
    WebDriverManager.return_driver().save_screenshot(filepath)
    print(f"Screenshot salvato: {filepath}")
    # Incrementa il contatore
    contatoreScreenshot += 1

def screenshotElement(element_id, folder="screenshots"):
    global contatoreScreenshot  # Uso della variabile globale contatore
    
    try:
        # Trova l'elemento
        elem = WebDriverManager.return_driver().find_element("xpath", element_id)  # Modifica il tipo di selezione se necessario
        
        # Crea la cartella se non esiste
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Genera un nome univoco per il file screenshot
        timestamp = datetime.now().isoformat(timespec='seconds').replace(':', '-')
        filename = f"{contatoreScreenshot}_{timestamp}.png"
        filepath = os.path.join(folder, filename)
        size = elem.size
        print(size)
        # Salva lo screenshot dell'elemento
        elem.screenshot(filepath)
        print(f"Screenshot salvato: {filepath}")

        # Incrementa il contatore
        contatoreScreenshot += 1

        return filepath  # Ritorna il percorso dello screenshot salvato

    except NoSuchElementException:
        print(f"Elemento non trovato: {element_id}")
        return None

#Fa un check se esiste l'elemento e lo screena
def checkExistence(element_id):
    elem = WebDriverManager.return_driver().find_element("xpath", element_id)
    print(f"{element_id} è presente")
    if elem.is_displayed:
        screenshotElement(WebDriverManager.return_driver(),element_id,folder="screenshots")

# Funzione per inserire del testo all'interno di un campo di input (dato un XPath)
def inputInsideElement(element, text):
    try:
        # Attendere che l'elemento sia presente nel DOM
        elem = WebDriverWait(WebDriverManager.return_driver(), 5).until(
            EC.presence_of_element_located((By.XPATH, element))
        )

        # Attendere che l'elemento sia visibile e interattivo
        WebDriverWait(WebDriverManager.return_driver(), 5).until(
            EC.element_to_be_clickable((By.XPATH, element))
        )

        # Fare un click sull'elemento per attivarlo
        elem.click()

        # Cancellare il testo preesistente (se necessario)
        elem.clear()

        # Inserire il testo
        elem.send_keys(text)
    except Exception as e:
        print(f"Errore nell'inserire il testo in '{element}': {e}")


def inputInsideElementWithDisabledState(element, text):
    try:
        # Attendere che l'elemento sia presente nel DOM
        elem = WebDriverWait(WebDriverManager.return_driver(), 5).until(
            EC.presence_of_element_located((By.XPATH, element))
        )

        # Attendere che l'elemento sia visibile e interattivo
        WebDriverWait(WebDriverManager.return_driver(), 5).until(
            EC.element_to_be_clickable((By.XPATH, element))
        )
        
        WebDriverManager.return_driver().execute_script("arguments[0].removeAttribute('disabled')", elem)
        # Fare un click sull'elemento per attivarlo
        elem.click()

        # Cancellare il testo preesistente (se necessario)
        elem.clear()

        # Inserire il testo
        elem.send_keys(text)
    except Exception as e:
        print(f"Errore nell'inserire il testo in '{element}': {e}")

#Per usarla devi inserire all'interno della funzione il nome del frame a cui vuoi switchare
def switchToFrame(nameFrame):
    try:
        WebDriverManager.return_driver().switch_to.frame(nameFrame)
        print(f"Switcho all'iframe indicato: '{nameFrame}'")
    except Exception as e:
        print(f"Impossibile switchare al frame richiesto")

#Per ritornare al contenuto principale
def returnToMainPage():
    try:
        WebDriverManager.return_driver().switch_to.default_content()
        print("Switcho al default content dall'iframe")
    except Exception as e:
        print(f"Impossibile switchare al main frame")

#Scrolla sull'elemento per cliccarlo
def scrollToElement(element):
    ActionChains(WebDriverManager.return_driver()).move_to_element(element).click().perform()
    print("Scrollato sull'elemento e provato a cliccare")


#Premere Invio senza un elemento specifico
def pressEnter():
    actions = ActionChains(WebDriverManager.return_driver())
    actions.send_keys(Keys.ENTER)
    actions.perform()
    print("Premuto invio")

def importoRandom():
    # Genera un numero con la virgola a 2 cifre da 1 a 100
    importo = round(random.uniform(1,100),2)
    print(importo)
    return importo

def randomText():
    text = ''.join(random.choices(string.ascii_lowercase, k=5))
    return text



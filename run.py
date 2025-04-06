import sys
import importlib
from config.driver import WebDriverManager

if __name__ == "__main__":
    browser = sys.argv[1].lower() if len(sys.argv) > 1 else "chrome"
    test_path = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"[DEBUG] Browser indicato: {browser}")
    print(f"[DEBUG] Test indicato: {test_path}")

    if not test_path:
        print("Errore: specifica un modulo da eseguire (es: OurApp.enrollment)")
        sys.exit(1)

    # Inizializza il driver
    driver = WebDriverManager.get_driver(browser)

    # Costruzione del path dinamico (da test_path tipo "OurApp.enrollment")
    try:
        mod = importlib.import_module(f"tests.{test_path}")
        print(f"[DEBUG] Import riuscito: tests.{test_path}")
    except ModuleNotFoundError:
        print(f"[ERRORE] Modulo 'tests.{test_path}' non trovato.")
        sys.exit(1)
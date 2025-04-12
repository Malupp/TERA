import sys
import importlib
from config.driver import WebDriverManager

if __name__ == "__main__":
    browser = sys.argv[1].lower() if len(sys.argv) > 1 else "chrome"
    test_path = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"[DEBUG] Browser specified: {browser}")
    print(f"[DEBUG] Test specified: {test_path}")

    if not test_path:
        print("Error: specify a module to execute")
        sys.exit(1)

    # Initialize the driver
    driver = WebDriverManager.get_driver(browser)

    # Dynamic path construction
    try:
        mod = importlib.import_module(f"tests.{test_path}")
        print(f"[DEBUG] Test completed: tests.{test_path}")
    except ModuleNotFoundError:
        print(f"[ERROR] Module 'tests.{test_path}' not found.")
        sys.exit(1)
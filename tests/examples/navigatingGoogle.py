from src.steps.loginSteps import LoginSteps
from config.driver import WebDriverManager

driver = WebDriverManager.get_driver("chrome")

# This is a first test example, it will be replaced soon with pytest 
LoginSteps.loginExample()
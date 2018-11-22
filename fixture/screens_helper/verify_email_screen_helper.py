from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class VerifyEmailHelper():

    def __init__(self, app):
        self.app = app

    def screen_verify_email_is_presented(self):
        element = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, "h2.ygWV5")
        if len(element) > 0:
            text = element.text
            if text == 'Verify Your E-mail Address':
                return True
            else:
                return False
        else:
            return False
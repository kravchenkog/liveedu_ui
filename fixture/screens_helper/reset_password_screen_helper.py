from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class ResetPasswordHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.main_title = 'h2.ygWV5'


    def screen_reset_pasword_is_presented(self):
        elts = self.driver.find_elements_by_css_selector(self.main_title)
        if len(elts) > 0:
            if elts[0].text == 'Reset your password':
                return True
        else:
            return False

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class ResetPasswordHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.file_forgot1 = 'login-signup-header'

        self.header = {By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_forgot1)}


    def screen_reset_pasword_is_presented(self):
        elts = self.app.general.find_elS_and_return(self.header)
        if len(elts) > 0:
            return elts[0].text == 'Reset your password'

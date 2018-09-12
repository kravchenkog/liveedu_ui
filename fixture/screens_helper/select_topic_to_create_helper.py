from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SelectTopicToCreateHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def screen_select_topic_to_create_is_presented(self):
        elements = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, "input[name='skype']")
        if len(elements) > 0:
            return True
        else:
            return False

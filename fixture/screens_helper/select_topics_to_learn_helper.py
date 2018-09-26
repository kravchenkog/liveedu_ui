from selenium.webdriver.common.by import By

class SelectTopicstoLearnHelper():

    def __init__(self, app):
        self.app = app
        self.file_topic = "login-signup-header"

        self.header_title = {By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_topic)}


    def screen_select_topic_is_presented(self):
        elements = self.app.general.find_elS_and_return(self.header_title)
        if len(elements) > 0:
            try:
                text = elements[0].text
                if text == 'What do you want to learn?':
                    return True
            except:
                return False

        else:
            return False

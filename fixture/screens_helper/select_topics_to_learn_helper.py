from selenium.webdriver.common.by import By

class SelectTopicstoLearnHelper():

    def __init__(self, app):
        self.app = app


    def screen_select_topic_is_presented(self):
        elements = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, "h2.ygWV5")
        if len(elements) > 0:
            try:
                text = elements[0].text
                if text == 'What do you want to learn?':
                    return True
            except:
                return False

        else:
            return False

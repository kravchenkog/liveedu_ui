
class SelectTopicToCreateHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def screen_select_topic_to_create_is_presented(self):
        elements = self.driver.find_elements_by_css_selector("input[name='skype']")
        if len(elements) > 0:
            return True
        else:
            return False

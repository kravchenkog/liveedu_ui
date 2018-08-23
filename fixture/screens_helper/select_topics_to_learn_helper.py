class SelectTopicstoLearnHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def screen_select_topic_is_presented(self):
        elements = self.driver.find_elements_by_css_selector("h2.ygWV5")
        if len(elements) > 0:
            try:
                text = elements[0].text
                if text == 'What do you want to learn?':
                    return True
            except:
                return False

        else:
            return False

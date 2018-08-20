

class GeneralHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def element_is_displayed(self, element):
        if element.is_displayed():
            return True
        else:
            return False

    def find_element_by(self, locator, value):
        return self.driver.find_element(locator, value)

    def find_elements_by(self, locator, value):
        return self.driver.find_elements(locator, value)

    def screen_is_presented_by_url(self, url):
        if self.driver.current_url == url:
            return True
        else:
            return False








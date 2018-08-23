



class VerifyEmailHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def screen_verify_email_is_presented(self):
        element = self.driver.find_elements_by_css_selector("h2.ygWV5")
        if len(element) > 0:
            text = element.text
            if text == 'Verify Your E-mail Address':
                return True
        else:
            return False
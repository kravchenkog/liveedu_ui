from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class UsernameHelper():



    def __init__(self, app):
        self.app = app
        self.file_username1 = 'signup-username-form'
        self.file_username2 = 'login-signup-header'
        self.button_next = {By.CSS_SELECTOR: "button[class^='{}__form-button']".format(self.file_username1)}
        self.title_top = {By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_username2)}
        self.field_username = {By.CSS_SELECTOR: 'input[name="username"]'}
        self.title_lower = {By.CSS_SELECTOR: "p[class^='{}__text']".format(self.file_username2)}



    def screen_username_is_presented(self):
        return self.app.general.el_is_presented(self.field_username)

    def screen_username_wait_presenting(self):
        self.app.general.wait_presence_of_el(self.field_username, 5)

    def title_top_is_displayed(self):
        return self.app.general.el_is_displayed(self.title_top)

    def title_lower_is_displayed(self):
        return self.app.general.el_is_displayed(self.title_lower)

    def field_username_is_displayed(self):
        return self.app.general.el_is_displayed(self.field_username)

    def button_next_is_displayed(self):
        return self.app.general.el_is_displayed(self.button_next)

    def button_next_click(self):
        self.app.general.but_press(self.button_next)

    def field_username_send_keys(self, user):
        self.app.general.send_k(self.field_username, user.username)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class UsernameHelper():



    def __init__(self, app):
        self.app = app
        self.button_next = "button[type='submit']"
        self.field_username = 'input[name="username"]'
        self.title_top_css = "h2.ygWV5"
        self.title_lower_css = "p._16y2Q"


    def screen_username_is_presented(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.field_username)

    def screen_username_wait_presenting(self):
        self.app.general.wait_presence_of_element(By.CSS_SELECTOR, self.field_username, 5)

    def title_top_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.title_top_css)

    def title_lower_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.title_lower_css)

    def field_username_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.field_username)

    def button_next_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_next)

    def button_next_click(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_next)

    def field_username_send_keys(self, user):
        self.app.general.send_key(By.CSS_SELECTOR, self.field_username, user.username)

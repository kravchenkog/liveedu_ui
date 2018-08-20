from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class UsernameHelper():
    button_next = "button[type='submit']"
    field_username = 'input[name="username"]'

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
       # self.button_next = "button[type='submit']"

    def screen_username_is_presented(self):
        elements = self.driver.find_elements_by_css_selector(self.field_username)
        if len(elements) > 0:
            return True
        else:
            return False

    def screen_username_wait_presenting(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.field_username)))

    def title_top_is_presented(self):
        return self.app.general.element_is_displayed(self.app.driver.find_element_by_css_selector
                                                     ("h2.ygWV5"))

    def title_lower_is_presented(self):
        return self.app.general.element_is_displayed(self.app.driver.find_element_by_css_selector
                                                     ("p._16y2Q"))

    def field_username_is_presented(self):
        return self.app.general.element_is_displayed(self.app.driver.find_element_by_css_selector
                                                     ("input[name='username']"))

    def button_next_is_presented(self):
        return self.app.general.element_is_displayed(self.app.driver.find_element_by_css_selector
                                                     (self.button_next))

    def button_next_click(self):
        self.app.driver.find_element_by_css_selector(self.button_next).click()

    def field_username_send_keys(self, value):
        self.app.driver.find_element_by_css_selector(self.field_username).send_keys(value)
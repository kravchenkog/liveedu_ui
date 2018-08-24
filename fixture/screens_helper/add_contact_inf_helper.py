from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class AddYouContactsInformationHelper():
    button_next_css = 'button[type="submit"]'
    hanouts_css = 'input[name="hangouts"]'
    skype_css = 'input[name="skype"]'

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def screen_add_contact_inf_is_presented(self):
        elements = self.driver.find_elements_by_css_selector("input[name='skype']")
        if len(elements) > 0:
            return True
        else:
            return False

    def title_top_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('h2.ygWV5'))

    def title_below_top_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('p._16y2Q'))

    def field_skype_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector(self.skype_css))

    def field_google_hang_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector(self.hanouts_css))

    def button_next_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector(self.button_next_css))

    def go_to_add_contact_inf_screen(self, user):
        self.app.signup.signup_fillall_press_done_wait_username(user)
        if user.username == None:
            user.username = self.app.string.get_random_username()
        self.app.username.field_username_send_keys(user)
        self.app.username.button_next_click()
        self.app.chose_role.button_create_project_tap()


    def field_skype_send_key(self, user):
        self.driver.find_element_by_css_selector(self.skype_css).send_keys(user.skype)

    def button_next_tap(self):
        self.driver.find_element_by_css_selector(self.button_next_css).click()


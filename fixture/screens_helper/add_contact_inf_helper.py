from selenium.webdriver.common.by import By



class AddYouContactsInformationHelper():
    button_next_css = 'button[type="submit"]'
    hanouts_css = 'input[name="hangouts"]'
    skype_css = 'input[name="skype"]'
    title_top_css = 'h2.ygWV5'
    title_below_top_css = 'p._16y2Q'

    def __init__(self, app):
        self.app = app

    def screen_add_contact_inf_is_presented(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.skype_css)

    def title_top_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.title_top_css)

    def title_below_top_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.title_below_top_css)


    def field_skype_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.skype_css)

    def field_google_hang_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.hanouts_css)

    def button_next_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_next_css)

    def go_to_add_contact_inf_screen(self, user):
        self.app.signup.signup_fillall_press_done_wait_username(user)
        self.app.username.field_username_send_keys(user)
        self.app.username.button_next_click()
        self.app.chose_role.button_create_project_tap()

    def field_skype_send_key(self, user):
        self.app.general.send_key(By.CSS_SELECTOR, self.skype_css, user.skype)

    def button_next_tap(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_next_css)



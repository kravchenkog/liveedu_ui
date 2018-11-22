from selenium.webdriver.common.by import By



class AddYouContactsInformationHelper():
    file_topic = "login-signup-header"
    file_topic2 = 'signup-contact-form'

    header_title = {By.CSS_SELECTOR: "h2[class^='{}__title']".format(file_topic)}
    header_text = {By.CSS_SELECTOR: "p[class^='{}__text']".format(file_topic)}

    button_next = {By.CSS_SELECTOR:'button[class^={}__form-button]'.format(file_topic2)}
    hanouts = {By.CSS_SELECTOR: 'input[name="hangouts"]'}
    skype = {By.CSS_SELECTOR: 'input[name="skype"]'}

    title_below_top_css = 'p._16y2Q'

    def __init__(self, app):
        self.app = app

    def screen_add_contact_inf_is_presented(self):
        return self.app.general.el_is_presented(self.skype)

    def title_top_is_displayed(self):
        return self.app.general.el_is_displayed(self.header_title)

    def title_below_top_is_displayed(self):
        return self.app.general.el_is_displayed(self.header_text)


    def field_skype_is_displayed(self):
        return self.app.general.el_is_displayed(self.skype)

    def field_google_hang_is_displayed(self):
        return self.app.general.el_is_displayed(self.hanouts)

    def button_next_is_displayed(self):
        return self.app.general.el_is_displayed(self.button_next)

    def go_to_add_contact_inf_screen(self, user):
        self.app.signup.signup_fillall_press_done_wait_username(user)
        self.app.username.field_username_send_keys(user)
        self.app.username.button_next_click()
        self.app.chose_role.button_create_project_tap()

    def field_skype_send_key(self, user):
        self.app.general.send_k(self.skype, user.skype)

    def button_next_tap(self):
        self.app.general.but_press(self.button_next)



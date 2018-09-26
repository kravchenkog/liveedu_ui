from selenium.webdriver.common.by import By


class ChoseYourRoleHelper():

    def __init__(self, app):
        self.app = app
        self.file_role1 = "signup-role-form"
        self.file_role2 = "login-signup-header"

        self.study_button = {By.CSS_SELECTOR: "button[class^='{}__form-left']".format(self.file_role1)}
        self.create_project_button = {By.CSS_SELECTOR: "button[class^='{}__form-right']".format(self.file_role1)}
        self.title_top = {By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_role2)}
        self.title_below_top = {By.CSS_SELECTOR: "p[class^='{}__text']".format(self.file_role2)}



    def screen_choseyourrole_is_presented(self):
        return self.app.general.el_is_presented(self.study_button)

    def title_top_is_displayed(self):
        return self.app.general.el_is_presented(self.title_top)

    def title_below_top_is_displayed(self):
        return self.app.general.el_is_presented(self.title_below_top)

    def button_study_is_displayed(self):
        return self.app.general.el_is_presented(self.study_button)

    def button_create_project_is_displayed(self):
        return self.app.general.el_is_presented(self.create_project_button)

    def title_lower_is_displayed(self):
        return self.app.general.el_is_presented(self.title_below_top)

    def button_create_project_tap(self):
        self.app.general.but_press(self.create_project_button)

    def button_study_tap(self):
        self.app.general.but_press(self.study_button)

    def go_to_choose_role_screen(self, user):
        self.app.signup.signup_fillall_press_done_wait_username(user)
        user.username = self.app.string.get_random_username()
        self.app.username.field_username_send_keys(user)
        self.app.username.button_next_click()

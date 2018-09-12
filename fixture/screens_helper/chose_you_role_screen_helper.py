from selenium.webdriver.common.by import By


class ChoseYourRoleHelper():

    def __init__(self, app):
        self.app = app
        self.create_project_but_css = 'button._36dlQ'
        self.study_button_css = 'button._1Dk7f'
        self.title_top_css = 'h2.ygWV5'
        self.title_below_top_css = 'p._16y2Q'
        self.title_lower_css = 'p._16y2Q'


    def screen_choseyourrole_is_presented(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, "button[class='_1Dk7f']")

    def title_top_is_displayed(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.title_top_css)

    def title_below_top_is_displayed(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.title_below_top_css)

    def button_study_is_displayed(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.study_button_css)

    def button_create_project_is_displayed(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.create_project_but_css)

    def title_lower_is_displayed(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.title_lower_css)

    def button_create_project_tap(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.create_project_but_css)

    def button_study_tap(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.study_button_css)

    def go_to_choose_role_screen(self, user):
        self.app.signup.signup_fillall_press_done_wait_username(user)
        user.username = self.app.string.get_random_username()
        self.app.username.field_username_send_keys(user)
        self.app.username.button_next_click()


class ChoseYourRoleHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.create_project_but_css = 'button._36dlQ'
        self.study_button_css = 'button._1Dk7f'

    def screen_choseyourrole_is_presented(self):
        elements = self.driver.find_elements_by_css_selector("button[class='_1Dk7f']")
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

    def button_study_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector(self.study_button_css))

    def button_create_project_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector(self.create_project_but_css))

    def title_lower_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('p._16y2Q'))

    def button_create_project_tap(self):
        self.driver.find_element_by_css_selector(self.create_project_but_css).click()

    def button_study_tap(self):
            self.driver.find_element_by_css_selector(self.study_button_css).click()

    def go_to_choose_role_screen(self, user):
        self.app.signup.signup_fillall_press_done_wait_username(user)
        user.username = self.app.string.get_random_username()
        self.app.username.field_username_send_keys(user)
        self.app.username.button_next_click()

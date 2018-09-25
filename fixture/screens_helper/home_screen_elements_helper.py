

from selenium.webdriver.common.by import By



class HomeElements():

    def __init__(self, app):
        self.app = app
        self.general = self.app.general

        self.file_home1 = 'guest-nav-links'
        self.file_home2 = 'auth-buttons'
        self.file_home3 = 'guest-header'
        self.file_home4 = 'search-bar'

        self.header_buttons = {By.CSS_SELECTOR: "a[class^='{}__link']".format(self.file_home1)}
        self.auth_buttons = {By.CSS_SELECTOR: "a[class^='{}__link']".format(self.file_home2)}
        self.logo = {By.CSS_SELECTOR: "a[class^='{}__logo']".format(self.file_home3)}
        self.serach_bar = {By.CSS_SELECTOR: "a[class^='{}__search-bar']".format(self.file_home4)}


    def get_button_by_name(self, button_name, locator):
        button = self.general.get_el_by_text(text=button_name, element=locator)
        return button

    def home_screen_is_presented(self):
        return self.app.general.el_is_presented(self.logo)

    def button_learnlive_click(self):
        button = self.get_button_by_name("Learn Live!", locator=self.header_buttons)
        self.app.general.button_press_element(button)

    def button_pricing_click(self):
        button_pricing = self.get_button_by_name("Pricing", locator=self.header_buttons)
        self.app.general.button_press_element(button_pricing)

    def go_home_and_wait(self):

        self.app.general.go_to_url("https://dev.liveedu.tv/")
        self.app.general.wait_presence_of_element(By.CSS_SELECTOR, "a[class='_2NV3A _38w0o']", 5)

    def logout_go_home_and_wait(self):
        if self.app.login.user_is_logged_in():
            self.app.general.logout_perform()
        self.app.general.go_to_url("https://dev.liveedu.tv/")
        self.app.general.wait_presence_of_el(element=self.logo, time=5)

    def logo_is_presented(self):
        return self.app.general.el_is_displayed(self.logo)


    def button_learnlive_is_displayed(self):
        button = self.get_button_by_name("Learn Live!", locator=self.header_buttons)
        return self.app.general.element_is_displayed_by_element(button)


    def button_learnondemand_is_displayed(self):
        button = self.get_button_by_name("Learn on Demand", self.header_buttons)
        return self.app.general.element_is_displayed_by_element(button)


    def button_pricing_is_displayed(self):
        button_pricing = self.get_button_by_name("Pricing", locator=self.header_buttons)
        return self.app.general.element_is_displayed_by_element(button_pricing)


    def button_search_is_displayed(self):
        return self.app.general.el_is_displayed(self.serach_bar)


    def button_login_is_displayed(self):
        button = self.get_button_by_name(button_name="Log in", locator=self.auth_buttons)
        return self.app.general.element_is_displayed_by_element(button)


    def button_signup_is_displayed(self):
        button = self.get_button_by_name(button_name="Sign Up", locator=self.auth_buttons)
        return self.app.general.element_is_displayed_by_element(button)




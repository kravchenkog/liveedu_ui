

from selenium.webdriver.common.by import By



class HomeElements():

    def __init__(self, app):
        self.app = app
        self.button_pricing = 'a[href="/pricing"]'
        self.button_learn_live = 'a[href="/live"]'
        self.button_sign_up = 'a[href="/signup"]'
        self.logo = '._1_fnJ'
        self.learn_on_demand = "a[href='/projects']"
        self.search_css = 'svg[data-id="5fa51239e3874c4badb514a895707d9e"]'
        self.button_login_css = 'a[href="/login"]'


    def button_signup_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_sign_up)

    def home_screen_is_presented(self):
        if self.button_signup_is_presented():
            return True
        else:
            return False

    def button_learnlive_click(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_learn_live)

    def logout_go_home_and_wait(self):
        if self.app.login.user_is_logged_in():
            self.app.general.logout_perform()
        self.app.general.go_to_url("https://dev.liveedu.tv/")
        self.app.general.wait_presence_of_element(By.CSS_SELECTOR, "a[class='_2NV3A _38w0o']", 5)

    def logo_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.logo)


    def button_learnlive_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_learn_live)


    def button_learnondemand_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.learn_on_demand)


    def button_pricing_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_pricing)


    def button_search_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.search_css)


    def button_login_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_login_css)

    def button_pricing_click(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_pricing)



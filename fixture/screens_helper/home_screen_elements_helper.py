from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class HomeElements():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.button_pricing = 'a[href="/pricing"]'
        self.button_learn_live = 'a[href="/live"]'


    def button_signup_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector('a[href="/signup"]'))

    def home_screen_is_presented(self):
        driver = self.app.driver
        if driver.current_url == "https://dev.liveedu.tv/":
            return True
        else:
            return False
    def button_learnlive_click(self):
        self.driver.find_element_by_css_selector(self.button_learn_live).click()
    def logout_go_home_and_wait(self):
        if self.app.login.user_is_logged_in():
            self.app.general.logout_perform()
        self.driver.get("https://dev.liveedu.tv/")

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[class='_2NV3A _38w0o']"))
        )
    def logo_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                           ('._1_fnJ'))

    def button_learnlive_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                           (self.button_learn_live))

    def button_learnondemand_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                           ("a[href='/projects']"))

    def button_pricing_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                           (self.button_pricing))

    def button_search_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                           ('svg[data-id="5fa51239e3874c4badb514a895707d9e"]'))

    def button_login_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector('a[href="/login"]'))

    def button_pricing_click(self):
        self.driver.find_element_by_css_selector(self.button_pricing).click()


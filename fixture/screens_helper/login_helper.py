from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.email_css = "input[name='username']"
        self.password = "input[name='password']"
        self.login_top_title_css = 'h2.ygWV5'

    def button_login_press_and_wait(self):
        self.driver.find_element_by_css_selector('a[href="/login"]').click()
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.email_css)))

    def screen_login_is_presented(self):
        elements = self.driver.find_elements_by_css_selector(self.login_top_title_css)
        if len(elements) > 0:
            if elements[0].text == 'Log In':
                return True
        else:
            return False

    def fields_clear(self):
        self.field_login_clear()
        self.field_password_clear()

    def field_login_clear(self):
        field = self.driver.find_element_by_css_selector(self.email_css)
        field.clear()

    def field_password_clear(self):
        field = self.driver.find_element_by_css_selector(self.password)
        field.clear()

    def section_top_is_presented(self):
        return self.app.general.element_is_displayed(
            self.driver.find_element_by_css_selector('div._3Mtqt'))

    def section_login_with_social_is_presented(self):
        return self.app.general.element_is_displayed(
            self.driver.find_element_by_css_selector("div._2vNGx"))

    def  section_login_with_email_is_presented(self):
        return self.app.general.element_is_displayed(
            self.driver.find_element_by_css_selector('div._1rrbV'))

    def title_social_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("p._3vdgo"))

    def button_google_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi _3WrhD']"))
    def button_fb_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi _2z_ha']"))
    def button_vk_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi _1RGiq']"))
    def button_linkedin_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi TehRz']"))
    def button_yandex_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi _1VtQ-']"))
    def button_live_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi _2W6eI']"))
    def button_github_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi _3IuXa']"))
    def button_twitch_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi UhJfk']"))
    def button_gg_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("button[class='_2nXzi _1QVNY']"))

    def title_login_is_presented(self):
        elements = self.driver.find_elements_by_css_selector("p[class='_3vdgo']")
        if self.app.general.element_is_displayed(elements[1]):
            if elements[1].text == 'Log in with email':
                return True
        else:
            return False

    def field_email_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("input[name='username']"))
    def field_password_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("input[name='password']"))
    def button_enter_is_presented(self):
        element = self.driver.find_element_by_css_selector("button[class='_2XfOr']")
        if self.app.general.element_is_displayed(element):
            if element.text == 'Enter':
                return True
        else:
            return False

    def button_forgot_password_is_presented(self):
        element = self.driver.find_element_by_css_selector("a[class='_2Cz26']")
        if self.app.general.element_is_displayed(element):
            if element.text == 'Forgot Password?':
                return True
        else:
            return False





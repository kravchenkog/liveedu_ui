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
        self.button_enter_css = "button[class='_2XfOr']"
        self.error_message_css = 'p._5jWkD'
        self.forgot_password_css = "a[class='_2Cz26']"

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
                                                     (self.email_css))
    def field_password_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.password))
    def button_enter_is_presented(self):
        element = self.driver.find_element_by_css_selector(self.button_enter_css)
        if self.app.general.element_is_displayed(element):
            if element.text == 'Enter':
                return True
        else:
            return False

    def button_forgot_password_is_presented(self):
        element = self.driver.find_element_by_css_selector(self.forgot_password_css)
        if self.app.general.element_is_displayed(element):
            if element.text == 'Forgot Password?':
                return True
        else:
            return False

    def field_password_send_key(self, value):
        self.driver.find_element_by_css_selector(self.password).send_keys(value)


    def button_enter_press(self):
        self.driver.find_element_by_css_selector(self.button_enter_css).click()

    def field_email_send_key(self, value):
        self.driver.find_element_by_css_selector(self.email_css).send_keys(value)

    def register_new_user_and_go_to_login_screen(self, app):
        self.app.string.get_random_userdata(self.app.user)
        self.app.home_el.logout_go_home_and_wait()
        self.app.signup.button_signup_press_and_wait()
        self.app.signup.complete_registration(self.app.user)
        self.app.api.email_confirmation(app=self.app, user=self.app.user)
        self.app.home_el.logout_go_home_and_wait()
        self.button_login_press_and_wait()

    def user_is_logged_in(self):
        if len(self.app.driver.find_elements_by_css_selector('button._1pGNL')) > 0:
            return self.app.general.element_is_displayed(
                    self.app.driver.find_element_by_css_selector('button._1pGNL'))
        else: return False

    def error_message_appears(self, error_message):
        el = self.driver.find_element_by_css_selector(self.error_message_css)
        if el.text == error_message:
            return True
        else:
            return False

    def button_forgot_password_press(self):
        self.driver.find_element_by_css_selector(self.forgot_password_css).click()





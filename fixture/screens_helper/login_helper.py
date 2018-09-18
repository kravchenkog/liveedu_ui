from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginHelper():

    def __init__(self, app):
        self.app = app
        self.general = self.app.general

        self.email_css = "input[name='username']"
        self.password = "input[name='password']"
        self.login_top_title_css = 'h2.ygWV5'
        self.button_enter_css = "button[class='_2XfOr']"
        self.error_message_css = 'p._5jWkD'
        self.forgot_password_css = "a[class='_2Cz26']"
        self.button_login_css = 'a[href="/login"]'
        self.section_top = 'div._3Mtqt'
        self.section_login_with_social_css = "div._2vNGx"
        self.section_login_with_email_css = 'div._1rrbV'
        self.title_social_css = "p._3vdgo"
        self.button_google_css = "button[class='_2nXzi _3WrhD']"
        self.button_fb_css = "button[class='_2nXzi _2z_ha']"
        self.button_vk_css = "button[class='_2nXzi _1RGiq']"
        self.button_linkedin_css = "button[class='_2nXzi TehRz']"
        self.button_yandex_css = "button[class='_2nXzi _1VtQ-']"
        self.button_live_css = "button[class='_2nXzi _2W6eI']"
        self.button_github_css = "button[class='_2nXzi _3IuXa']"
        self.button_twitch_css = "button[class='_2nXzi UhJfk']"
        self.button_gg_css = "button[class='_2nXzi _1QVNY']"
        self.login_title_css = "div._1rrbV p[class='_3vdgo']"
        self.user_menu_open_but = {By.CSS_SELECTOR: 'button._1pGNL'}
        self.user_role = {By.CSS_SELECTOR: 'p._3-xEp'}
        self.user_menu_section = {By.CSS_SELECTOR: 'ul.e_dik'}


    def button_login_press_and_wait(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_login_css)
        self.app.general.wait_presence_of_element(By.CSS_SELECTOR, self.email_css, 5)

    def screen_login_is_presented(self):
        elements = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, self.login_top_title_css)
        if len(elements) > 0:
            if elements[0].text == 'Log In':
                return True
        else:
            return False

    def fields_clear(self):
        self.field_login_clear()
        self.field_password_clear()

    def field_login_clear(self):
        self.app.general.field_clear(By.CSS_SELECTOR, self.email_css)

    def field_password_clear(self):
        self.app.general.field_clear(By.CSS_SELECTOR, self.password)

    def section_top_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section_top)

    def section_login_with_social_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section_login_with_social_css)

    def section_login_with_email_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section_login_with_email_css)

    def title_social_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.title_social_css)

    def button_google_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_google_css)

    def button_fb_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_fb_css)

    def button_vk_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_vk_css)

    def button_linkedin_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_linkedin_css)

    def button_yandex_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_yandex_css)

    def button_live_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_live_css)

    def button_github_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_github_css)

    def button_twitch_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_twitch_css)

    def button_gg_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_gg_css)

    def title_login_is_displayed(self):

        if self.app.general.element_is_displayed(By.CSS_SELECTOR, self.login_title_css):
            if self.app.general.get_text_of_element(By.CSS_SELECTOR, self.login_title_css) == 'Log in with email':
                return True
        else:
            return False

    def field_email_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.email_css)

    def field_password_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.password)

    def button_enter_is_displayed(self):

        if self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_enter_css):
            if self.app.general.get_text_of_element(By.CSS_SELECTOR, self.button_enter_css) == 'Enter':
                return True
        else:
            return False

    def button_forgot_password_is_displayed(self):
        if self.app.general.element_is_displayed(By.CSS_SELECTOR, self.forgot_password_css):
            if self.app.general.get_text_of_element(By.CSS_SELECTOR, self.forgot_password_css) == 'Forgot Password?':
                return True
        else:
            return False

    def field_password_send_key(self, value):
        self.app.general.send_key(By.CSS_SELECTOR, self.password, value)

    def button_enter_press(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_enter_css)

    def field_email_send_key(self, value):
        self.app.general.send_key(By.CSS_SELECTOR, self.email_css, value)

    def register_new_user_and_go_to_login_screen(self, app):
        self.app.string.get_random_userdata(self.app.user)
        self.app.home_el.logout_go_home_and_wait()
        self.app.signup.button_signup_press_and_wait()
        self.app.signup.complete_registration(self.app.user)
        self.app.api.email_confirmation(app=self.app, user=self.app.user)
        self.app.home_el.logout_go_home_and_wait()
        self.button_login_press_and_wait()

    def login_perform(self, user):
        self.button_login_press_and_wait()
        self.field_email_send_key(user.email)
        self.app.login.field_password_send_key(user.password1)
        self.app.login.button_enter_press()

    def user_is_logged_in(self):
        if len(self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'button._1pGNL')) > 0:
            return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'button._1pGNL')
        else:
            return False

    def error_message_appears(self, error_message):
        el = self.app.general.find_element_and_return(By.CSS_SELECTOR, self.error_message_css)
        if el.text == error_message:
            return True
        else:
            return False

    def button_forgot_password_press(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.forgot_password_css)

    def get_logged_user_type(self):
        self.general.but_press(self.user_menu_open_but)
        role = self.general.get_txt_of_el(self.user_role)
        if role == 'Subscriber':
            return 1
        if role == 'Project Creator':
            return 2

    def user_menu_is_opened(self):
        return self.general.el_is_presented(self.user_menu_section)







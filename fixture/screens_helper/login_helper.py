from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginHelper():

    def __init__(self, app):
        self.app = app
        self.general = self.app.general
        self.home = self.app.home_el

        self.file_login1 = "login"
        self.file_login2 = "login-signup-header"
        self.file_login3 = "login-form"
        self.file_login4 = "form-error"
        self.file_login5 = "login-signup-social"
        self.file_login6 = "user-menu"

        self.login_form_left = {By.CSS_SELECTOR: "div[class^='{}__form-left']".format(self.file_login1)}
        self.login_form_right = {By.CSS_SELECTOR: "div[class^='{}__form-right']".format(self.file_login1)}
        self.login_header = {By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_login2)}
        self.email_field = {By.CSS_SELECTOR: "input[name='username']"}
        self.password_field = {By.CSS_SELECTOR: "input[name='password']"}
        self.enter_button = {By.CSS_SELECTOR: "button[class^='{}__form-button']".format(self.file_login3)}
        self.error_txt = {By.CSS_SELECTOR: "p[class^='{}__form-error-text']".format(self.file_login4)}
        self.forgot_password = {By.CSS_SELECTOR: "a[class^='{}__form-link']".format(self.file_login1)}
        self.left_right_titles = {By.CSS_SELECTOR: "p[class^='{}__form-text']".format(self.file_login1)}
        self.social_buttons = {By.CSS_SELECTOR: "button[class^='{}__link']".format(self.file_login5)}
        self.user_menu_button = {By.CSS_SELECTOR: "button[class^='{}__button']".format(self.file_login6)}
        self.user_menu_role = {By.CSS_SELECTOR: "button[class^='{}__role']".format(self.file_login6)}
        self.user_menu_section = {By.CSS_SELECTOR: "button[class^='{}__menu-user']".format(self.file_login6)}




    def button_login_press_and_wait(self):
        button = self.home.get_button_by_name(button_name="Log In", locator=self.home.auth_buttons)
        self.app.general.button_press_element(button)
        self.app.general.wait_presence_of_el(self.login_form_left, 5)

    def screen_login_is_presented(self):
        elements = self.app.general.find_elS_and_return(self.login_header)
        if len(elements) > 0:
            if elements[0].text == 'Log In':
                return True
        else:
            return False

    def fields_clear(self):
        self.field_login_clear()
        self.field_password_clear()

    def field_login_clear(self):
        self.app.general.fld_clear(self.email_field)

    def field_password_clear(self):
        self.app.general.fld_clear(self.password_field)

    def section_top_is_displayed(self):
        return self.app.general.el_is_displayed(self.login_header)

    def section_login_with_social_is_displayed(self):
        return self.app.general.el_is_displayed(self.login_form_left)

    def section_login_with_email_is_displayed(self):
        return self.app.general.el_is_displayed(self.login_form_right)

    def title_social_is_displayed(self):
        el = self.general.get_el_by_name(name='Log in with social', locator=self.left_right_titles)
        return self.app.general.element_is_displayed_by_element(el)

    def button_social_is_displayed(self, name):
        el = self.general.get_el_by_name(name=name, locator=self.social_buttons)
        return self.general.element_is_displayed_by_element(el)
    #
    # def button_google_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_google_css)
    #
    # def button_fb_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_fb_css)
    #
    # def button_vk_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_vk_css)
    #
    # def button_linkedin_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_linkedin_css)
    #
    # def button_yandex_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_yandex_css)
    #
    # def button_live_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_live_css)
    #
    # def button_github_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_github_css)
    #
    # def button_twitch_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_twitch_css)
    #
    # def button_gg_is_displayed(self):
    #     return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_gg_css)

    def title_login_is_displayed(self):
        el = self.general.get_el_by_name('Log in with email', self.left_right_titles)
        return self.app.general.element_is_displayed_by_element(el)


    def field_email_is_displayed(self):
        return self.app.general.el_is_displayed(self.email_field)

    def field_password_is_displayed(self):
        return self.app.general.el_is_displayed(self.password_field)

    def button_enter_is_displayed(self):

        if self.app.general.el_is_displayed(self.enter_button):
            return self.app.general.get_txt_of_el(self.enter_button) == 'Enter'
        return False

    def button_forgot_password_is_displayed(self):
        if self.app.general.el_is_displayed(self.forgot_password):
            return self.app.general.get_txt_of_el(self.forgot_password) == 'Forgot Password?'
        return False

    def field_password_send_key(self, value):
        self.app.general.send_k(self.password_field, value)

    def button_enter_press(self):
        self.app.general.but_press(self.enter_button)

    def field_email_send_key(self, value):
        self.app.general.send_k(self.email_field, value)

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

        return False

    def error_message_appears(self, error_message):
        el = self.app.general.find_el_and_return(self.error_txt)
        return el.text == error_message


    def button_forgot_password_press(self):
        self.app.general.but_press(self.forgot_password)

    def get_logged_user_type(self):
        self.general.but_press(self.user_menu_button)
        role = self.general.get_txt_of_el(self.user_menu_role)
        if role == 'Subscriber':
            return 1
        if role == 'Project Creator':
            return 2
        else:print("incorrect Role!!!!!!!!!!")

    def user_menu_is_opened(self):
        return self.general.el_is_presented(self.user_menu_section)







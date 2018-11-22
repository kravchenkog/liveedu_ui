from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class SignUpHelper():

    def __init__(self, app):
        self.app = app
        self.general = self.app.general
        self.home = self.app.home_el
        self.file_signup1 = "signup-step-0"
        self.file_signup2 = "login-signup-header"
        self.file_signup3 = "login-signup-social"
        self.file_signup4 = "signup-form"


        self.form_left = {By.CSS_SELECTOR: "div[class^='{}__form-left']".format(self.file_signup1)}
        self.form_right = {By.CSS_SELECTOR: "div[class^='{}__form-right']".format(self.file_signup1)}
        self.field_confirm_password = {By.CSS_SELECTOR: "input[name='passwordConfirm']"}
        self.signup_form = {By.CSS_SELECTOR: "div[class^='{}__form']".format(self.file_signup1)}
        self.top_section = {By.CSS_SELECTOR: "div[class^='{}__header']".format(self.file_signup2)}
        self.lower_title = {By.CSS_SELECTOR: "p[class^='{}__caption']".format(self.file_signup1)}
        self.social_buttons = {By.CSS_SELECTOR: "div[class^='{}__link']".format(self.file_signup3)}
        self.title_email = {By.CSS_SELECTOR: "p[class^='{}__form-text']".format(self.file_signup1)}
        self.field_email = {By.CSS_SELECTOR: "input[name='email']"}
        self.field_password = {By.CSS_SELECTOR: "input[name='password']"}
        self.field_password_confirm = {By.CSS_SELECTOR: "input[name='passwordConfirm']"}
        self.button_start_learning = {By.CSS_SELECTOR: "button[class^='{}__form-button']".format(self.file_signup4)}
        self.signup_titles = {By.CSS_SELECTOR: f"p[class^='{self.file_signup1}__form-text']"}



        self.title_social_xpath = "//p[contains(text(),'Sign up with social')]"







    def button_signup_press_and_wait(self):
        button = self.home.get_button_by_name("Sign Up", locator=self.home.auth_buttons)
        self.general.button_press_element(button)
        self.app.general.wait_presence_of_el(self.field_confirm_password, 5)
        self.app.general.wait_presence_of_el(self.form_left, 5)

    def screen_signup_is_presented(self):
        return self.app.general.el_is_presented(self.signup_form)

    def screen_signup_is_displayed(self):
        return self.app.general.el_is_displayed(self.field_confirm_password)

    def section_top_is_displayed(self):
        return self.app.general.el_is_displayed(self.top_section)

    def section_signup_with_social_is_displayed(self):
        return self.app.general.el_is_displayed(self.form_left)

    def section_sign_up_with_email_is_displayed(self):
        return self.app.general.el_is_displayed(self.form_right)

    def section_lower_title_is_presented(self):
        return self.app.general.el_is_displayed(self.lower_title)

    def signup_social_button_is_displayed(self, button_name):
        el = self.app.general.get_el_by_text(text=button_name, element=self.social_buttons)
        return self.app.general.element_is_displayed_by_element(el)

    def title_social_is_displayed(self):
        title = self.app.general.get_el_by_text(element=self.signup_titles, text="Sign up with social")
        return self.app.general.element_is_displayed_by_element(title)


    def title_email_is_displayed(self):
        return self.app.general.el_is_displayed(self.title_email)

    def field_email_is_displayed(self):
        return self.app.general.el_is_displayed(self.field_email)

    def field_password_is_displayed(self):
        return self.app.general.el_is_displayed(self.field_password)

    def field_confirm_password_is_displayed(self):
        return self.app.general.el_is_displayed(self.field_confirm_password)

    def button_start_learning_is_displayed(self):
        return self.app.general.el_is_displayed(self.button_start_learning)

    def field_email_send_keys(self, user):
        self.app.general.send_k(self.field_email, user.email)

    def field_email_clear(self):
        self.app.general.fld_clear(self.field_email)

    def field_password_send_keys(self, user):
        self.app.general.send_k(self.field_password, user.password1)

    def field_password_clear(self):
        self.app.general.fld_clear(self.field_password)

    def field_confirm_password_send_keys(self, user):

        self.app.general.send_k(element=self.field_confirm_password, string=user.password2)

    def field_confirm_password_clear(self):
        self.app.general.fld_clear(self.field_confirm_password)

    def button_start_learning_press(self):
        self.app.general.but_press(self.button_start_learning)

    def fields_clear(self):
        self.field_email_clear()
        self.field_password_clear()
        self.field_confirm_password_clear()

    def signup_fillall_press_done_wait_username(self, user):
        # if user.email == None or user.password1 == None:
        #     user.email = self.app.string.get_random_email()
        #     user.password1, user.password2 = self.app.string.get_random_two_passwords()
        self.field_email_send_keys(user)
        self.field_password_send_keys(user)
        self.field_confirm_password_send_keys(user)
        self.button_start_learning_press()
        self.app.username.screen_username_wait_presenting()

    def complete_registration(self, user):
        self.app.cont_inf.go_to_add_contact_inf_screen(user)
        self.app.cont_inf.field_skype_send_key(user)
        self.app.cont_inf.button_next_tap()



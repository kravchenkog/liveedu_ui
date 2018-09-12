from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class SignUpHelper():

    def __init__(self, app):
        self.app = app
        self.button_sign_up = 'a[href="/signup"]'
        self.field_confirm_password_css = "input[name='passwordConfirm']"
        self.section_signup_with_social_css = 'div._27wqJ'
        self.section_top_xpath = '//div[@class="_3Mtqt"]'
        self.section_signup_with_social_xpath = "//div[@class='_27wqJ']"
        self.section_signup_with_email_xpath = '//div[@class="_1ncq1"]'
        self.section_lower_title_xpath = '//p[@class="_3ncBY"]'
        self.title_social_xpath = "//p[contains(text(),'Sign up with social')]"
        self.button_google_xpath = "//*[contains(@class,'svg-inline--fa fa-google-plus-g fa-w-20')]"
        self.button_fb_xpath = '//*[@class="svg-inline--fa fa-facebook-f fa-w-9 "]'
        self.button_vk_xpath = '//*[@class="svg-inline--fa fa-vk fa-w-18 "]'
        self.button_linkedin_xpath = '//*[@class="svg-inline--fa fa-linkedin-in fa-w-14 "]'
        self.button_yandex_xpath = "//*[@data-id='bb383ceadcc74bb9b5aafb22a713ae93']"
        self.button_live_xpath = '//*[@class="svg-inline--fa fa-windows fa-w-14 "]'
        self.button_github_xpath = '//*[@class="svg-inline--fa fa-github fa-w-16 "]'
        self.button_twitch_xpath = '//*[@class="svg-inline--fa fa-twitch fa-w-14 "]'
        self.button_gg_xpath = '//*[@data-id="c5d9b18ffcc6474abb11849bfdee11d1"]'
        self.title_email_css = "div[class='_1ncq1']"
        self.field_email_css = "input[name='email']"
        self.field_password = "input[name='password']"
        self.button_start_learning_css = 'button[class="_2WGwi"]'



    def button_signup_press_and_wait(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_sign_up)
        self.app.general.wait_presence_of_element(By.CSS_SELECTOR, self.field_confirm_password_css, 5)
        self.app.general.wait_presence_of_element(By.CSS_SELECTOR, self.section_signup_with_social_css, 5)

    def screen_signup_is_presented(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.field_confirm_password_css)

    def screen_signup_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.field_confirm_password_css)

    def section_top_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.section_top_xpath)

    def section_signup_with_social_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.section_signup_with_social_xpath)

    def section_sign_up_with_email_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.section_signup_with_email_xpath)

    def section_lower_title_is_presented(self):
        return self.app.general.element_is_displayed(By.XPATH, self.section_lower_title_xpath)

    def title_social_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.title_social_xpath)

    def button_google_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_google_xpath)

    def button_fb_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_fb_xpath)

    def button_vk_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_vk_xpath)

    def button_linkedin_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_linkedin_xpath)

    def button_yandex_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_yandex_xpath)

    def button_live_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_live_xpath)

    def button_github_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_github_xpath)

    def button_twitch_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_twitch_xpath)

    def button_gg_is_displayed(self):
        return self.app.general.element_is_displayed(By.XPATH, self.button_gg_xpath)

    def title_email_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.title_email_css)

    def field_email_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.field_email_css)

    def field_password_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.field_password)

    def field_confirm_password_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.field_confirm_password_css)

    def button_start_learning_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.button_start_learning_css)

    def field_email_send_keys(self, user):
        self.app.general.send_key(By.CSS_SELECTOR, self.field_email_css, user.email)

    def field_email_clear(self):
        self.app.general.field_clear(By.CSS_SELECTOR, self.field_email_css)

    def field_password_send_keys(self, user):
        self.app.general.send_key(By.CSS_SELECTOR, self.field_password, user.password1)

    def field_password_clear(self):
        self.app.general.field_clear(By.CSS_SELECTOR, self.field_password)

    def field_confirm_password_send_keys(self, user):
        self.app.general.send_key(By.CSS_SELECTOR, self.field_confirm_password_css, user.password2)

    def field_confirm_password_clear(self):
        self.app.general.field_clear(By.CSS_SELECTOR, self.field_confirm_password_css)

    def button_start_learning_press(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_start_learning_css)

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



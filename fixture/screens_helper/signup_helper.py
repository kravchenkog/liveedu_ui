from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class SignUpHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def button_signup_press_and_wait(self):
        self.driver.find_element_by_css_selector('a[href="/signup"]').click()
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='passwordConfirm']")))

        element = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div._27wqJ")))

    def screen_signup_is_presented(self):
        elements = self.driver.find_elements_by_css_selector('input[name="passwordConfirm"]')
        if len(elements) > 0:
            return True
        else:
            return False

    def screen_signup_is_displayed(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                      ('input[name="passwordConfirm"]'))

    def section_top_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//div[@class="_3Mtqt"]'))

    def section_signup_with_social_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ("//div[@class='_27wqJ']"))

    def section_sign_up_with_email_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//div[@class="_1ncq1"]'))

    def section_lower_title_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath('//p[@class="_3ncBY"]'))

    def title_social_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ("//p[contains(text(),'Sign up with social')]"))

    def button_google_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ("//*[contains"
                                                      "(@class,'svg-inline--fa fa-google-plus-g fa-w-20')]"))
    def button_fb_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//*[@class="svg-inline--fa fa-facebook-f fa-w-9 "]'))
    def button_vk_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//*[@class="svg-inline--fa fa-vk fa-w-18 "]'))
    def button_linkedin_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//*[@class="svg-inline--fa fa-linkedin-in fa-w-14 "]'))

    def button_yandex_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ("//*[@data-id='bb383ceadcc74bb9b5aafb22a713ae93']"))

    def button_live_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//*[@class="svg-inline--fa fa-windows fa-w-14 "]'))

    def button_github_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//*[@class="svg-inline--fa fa-github fa-w-16 "]'))

    def button_twitch_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//*[@class="svg-inline--fa fa-twitch fa-w-14 "]'))

    def button_gg_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_xpath
                                                     ('//*[@data-id="c5d9b18ffcc6474abb11849bfdee11d1"]'))

    def title_email_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("div[class='_1ncq1']"))

    def field_email_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                         ("input[name='email']"))

    def field_password_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                         ("input[name='password']"))

    def field_confirm_password_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ("input[name='passwordConfirm']"))

    def button_start_learning_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                 ('button[class="_2WGwi"]'))

    def field_email_send_keys(self, email):
        field = self.driver.find_element_by_css_selector("input[name='email']")
        field.send_keys(email)

    def field_email_clear(self):
        field = self.driver.find_element_by_css_selector("input[name='email']")
        field.clear()

    def field_password_send_keys(self, password):
        self.driver.find_element_by_css_selector("input[name='password']").send_keys(password)

    def field_password_clear(self):
        self.driver.find_element_by_css_selector("input[name='password']").clear()

    def field_confirm_password_send_keys(self, confirm_pass):
        self.driver.find_element_by_css_selector("input[name='passwordConfirm']").send_keys(confirm_pass)

    def field_confirm_password_clear(self):
        self.driver.find_element_by_css_selector("input[name='passwordConfirm']").clear()

    def button_start_learning_press(self):
        self.driver.find_element_by_css_selector('button[class="_2WGwi"]').click()

    def fields_clear(self):
        self.field_email_clear()
        self.field_password_clear()
        self.field_confirm_password_clear()

    def signup_fillall_press_done_wait_username(self):
        user_data = {}
        user_data['email'] = self.app.string.get_random_email()
        self.field_email_send_keys(user_data['email'])
        user_data['passwords'] = self.app.string.get_random_two_passwords()
        self.field_password_send_keys(user_data['passwords'][0])
        self.field_confirm_password_send_keys(user_data['passwords'][1])
        self.button_start_learning_press()
        self.app.username.screen_username_wait_presenting()
        return user_data


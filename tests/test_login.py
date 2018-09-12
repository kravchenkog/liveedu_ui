import pytest
from time import sleep

class TestClass():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, app_login):
        self.app = app_login

    def test_WHEN_login_screen_EXPECTED_3general_sections_are_presented_TC3200(self):
        elts_dct = {}
        elts_dct['topsection'] = self.app.login.section_top_is_displayed()
        elts_dct['login_with_social'] = self.app.login.section_login_with_social_is_displayed()
        elts_dct['login_with_email'] = self.app.login.section_login_with_email_is_displayed()

        for x in elts_dct.values():
            assert x is True

    def test_WHEN_login_open_EXPECTED_10elements_in_social_are_presented_TC3210(self):
        elts_dct = {}
        elts_dct['title_soc'] = self.app.login.title_social_is_displayed()
        elts_dct['google_soc'] = self.app.login.button_google_is_displayed()
        elts_dct['fb_social'] = self.app.login.button_fb_is_displayed()
        elts_dct['vk_social'] = self.app.login.button_vk_is_displayed()
        elts_dct['linkedin_soc'] = self.app.login.button_linkedin_is_displayed()
        elts_dct['yandex_soc'] = self.app.login.button_yandex_is_displayed()
        elts_dct['live_soc'] = self.app.login.button_live_is_displayed()
        elts_dct['github_soc'] = self.app.login.button_github_is_displayed()
        elts_dct['twitch_soc'] = self.app.login.button_twitch_is_displayed()
        elts_dct['qq_soc'] = self.app.login.button_gg_is_displayed()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_login_open_EXPECTED_5elements_in_email_are_presented_TC3240(self):
        elts_dct = {}

        elts_dct['title_login'] = self.app.login.title_login_is_displayed()
        elts_dct['email_field'] = self.app.login.field_email_is_displayed()
        elts_dct['password'] = self.app.login.field_password_is_displayed()
        elts_dct['enter_button'] = self.app.login.button_enter_is_displayed()
        elts_dct['forgot_passwprd'] = self.app.login.button_forgot_password_is_displayed()
        for x in elts_dct.values():
            assert x is True
    def test_WHEN_login_is_performed_AND_data_is_correct_EXPECTED_screen_is_presented_TC3250(self):

        self.app.login.register_new_user_and_go_to_login_screen(self.app)
        self.app.login.field_email_send_key(self.app.user.email)
        self.app.login.field_password_send_key(self.app.user.password1)
        self.app.login.button_enter_press()
        sleep(1)
        assert self.app.login.user_is_logged_in()

    def test_WHEN_email_is_incorrect_AND_try_to_login_EXPECTED_error_message_appears_TC3260(self):


        self.app.login.field_email_send_key(self.app.string.get_random_incorrect_email_type1())
        self.app.login.field_password_send_key(self.app.user.password1)
        self.app.login.button_enter_press()
        error_message = 'Unable to log in with provided credentials.'
        assert self.app.login.error_message_appears(error_message)

    def test_WHEN_password_is_incorrect_AND_try_to_login_EXPECTED_error_message_appears_TC3270(self):


        self.app.login.field_password_send_key(self.app.string.get_random_two_passwords_numeric()[0])
        self.app.login.field_email_send_key(self.app.user.email)
        self.app.login.button_enter_press()
        error_message = 'Unable to log in with provided credentials.'
        assert self.app.login.error_message_appears(error_message)

    def test_WHEN_forgot_password_but_pressed_EXPECTED_forgot_password_is_presented_TC3290(self):
        self.app.login.button_forgot_password_press()
        assert self.app.reset_pass.screen_reset_pasword_is_presented()





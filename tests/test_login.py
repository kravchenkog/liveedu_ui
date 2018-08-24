import pytest


class TestClass():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, app_login):
        self.app = app_login

    def test_WHEN_login_screen_EXPECTED_3general_sections_are_presented_TC3200(self):
        elts_dct = {}
        elts_dct['topsection'] = self.app.login.section_top_is_presented()
        elts_dct['login_with_social'] = self.app.login.section_login_with_social_is_presented()
        elts_dct['login_with_email'] = self.app.login.section_login_with_email_is_presented()

        for x in elts_dct.values():
            assert x is True

    def test_WHEN_login_open_EXPECTED_10elements_in_social_are_presented_TC3210(self):
        elts_dct = {}
        elts_dct['title_soc'] = self.app.login.title_social_is_presented()
        elts_dct['google_soc'] = self.app.login.button_google_is_presented()
        elts_dct['fb_social'] = self.app.login.button_fb_is_presented()
        elts_dct['vk_social'] = self.app.login.button_vk_is_presented()
        elts_dct['linkedin_soc'] = self.app.login.button_linkedin_is_presented()
        elts_dct['yandex_soc'] = self.app.login.button_yandex_is_presented()
        elts_dct['live_soc'] = self.app.login.button_live_is_presented()
        elts_dct['github_soc'] = self.app.login.button_github_is_presented()
        elts_dct['twitch_soc'] = self.app.login.button_twitch_is_presented()
        elts_dct['qq_soc'] = self.app.login.button_gg_is_presented()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_login_open_EXPECTED_5elements_in_email_are_presented_TC3240(self):
        elts_dct = {}

        elts_dct['title_login'] = self.app.login.title_login_is_presented()
        elts_dct['email_field'] = self.app.login.field_email_is_presented()
        elts_dct['password'] = self.app.login.field_password_is_presented()
        elts_dct['enter_button'] = self.app.login.button_enter_is_presented()
        elts_dct['forgot_passwprd'] = self.app.login.button_forgot_password_is_presented()
        for x in elts_dct.values():
            assert x is True
    def test_WHEN_login_is_performed_AND_data_is_correct_EXPECTED_screen_is_presented(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.home_el.go_to_home_screen_and_wait()
        self.app.signup.button_signup_press_and_wait()
        self.app.signup.complete_registration(self.app.user)
        self.app.api.email_confirmation(self.app)
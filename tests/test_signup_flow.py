from time import sleep
import pytest


class TestClass():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, app_signup):
        self.app = app_signup


    def test_WHEN_signup_screen_open_EXPECTED_4general_sections_are_presented_TC2000(self):
        elts_dct = {}
        elts_dct['topsection'] = self.app.signup.section_top_is_displayed()
        elts_dct['signup_with_social_section'] = self.app.signup.section_signup_with_social_is_displayed()
        elts_dct['signup_with_email_section'] = self.app.signup.section_sign_up_with_email_is_displayed()
        elts_dct['lower_title'] = self.app.signup.section_lower_title_is_presented()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_signup_open_EXPECTED_10elements_in_social_are_presented_TC2100(self):
        elts_dct = {}
        elts_dct['title_soc'] = self.app.signup.title_social_is_displayed()
        elts_dct['google_soc'] = self.app.signup.button_google_is_displayed()
        elts_dct['fb_social'] = self.app.signup.button_fb_is_displayed()
        elts_dct['vk_social'] = self.app.signup.button_vk_is_displayed()
        elts_dct['linkedin_soc'] = self.app.signup.button_linkedin_is_displayed()
        elts_dct['yandex_soc'] = self.app.signup.button_yandex_is_displayed()
        elts_dct['live_soc'] = self.app.signup.button_live_is_displayed()
        elts_dct['github_soc'] = self.app.signup.button_github_is_displayed()
        elts_dct['twitch_soc'] = self.app.signup.button_twitch_is_displayed()
        elts_dct['qq_soc'] = self.app.signup.button_gg_is_displayed()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_signup_open_EXPECTED_10elements_in_email_are_presented_TC2200(self):
        elts_dct = {}

        elts_dct['title_email'] = self.app.signup.title_email_is_displayed()
        elts_dct['email_field'] = self.app.signup.field_email_is_displayed()
        elts_dct['password'] = self.app.signup.field_password_is_displayed()
        elts_dct['confirm_password'] = self.app.signup.field_confirm_password_is_displayed()
        elts_dct['start_learning'] = self.app.signup.button_start_learning_is_displayed()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_email_pass_confpass_entered_EXPECTED_username_screen_is_presented_TC2210(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.user.email = self.app.string.get_random_email()
        self.app.signup.field_email_send_keys(self.app.user)
        self.app.user.password1, self.app.user.password2 = self.app.string.get_random_two_passwords()
        self.app.signup.field_password_send_keys(self.app.user)
        self.app.signup.field_confirm_password_send_keys(self.app.user)
        self.app.signup.button_start_learning_press()
        sleep(1)
        assert self.app.username.screen_username_is_presented()

    def test_WHEN_email_is_incorrect_AND_press_startlearn_button_EXPECTED_username_screen_is_not_presented_TC2220(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.user.email = self.app.string.get_random_incorrect_email_type1()
        self.app.signup.field_email_send_keys(user=self.app.user)
        self.app.user.password1, self.app.user.password2 = self.app.string.get_random_two_passwords()
        self.app.signup.field_password_send_keys(self.app.user)
        self.app.signup.field_confirm_password_send_keys(self.app.user)
        self.app.signup.button_start_learning_press()
        assert self.app.username.screen_username_is_presented() is not True


    def test_WHEN_passwords_are_not_the_same_AND_press_start_EXPECTED_username_screen_is_not_presented_TC2240(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.user.email = self.app.string.get_random_email()
        self.app.signup.field_email_send_keys(user=self.app.user)
        self.app.user.password1, self.app.user.password2 = self.app.string.get_random_two_passwords_not_the_same()
        self.app.signup.field_password_send_keys(self.app.user)
        self.app.signup.field_confirm_password_send_keys(self.app.user)
        self.app.signup.button_start_learning_press()
        assert self.app.username.screen_username_is_presented() is not True

    def test_WHEN_password_incorrect_AND_press_start_EXPECTED_username_screen_is_not_presented_TC2250(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.user.email = self.app.string.get_random_email()
        self.app.signup.field_email_send_keys(self.app.user)
        self.app.user.password1, self.app.user.password2 = self.app.string.get_random_two_passwords_numeric()
        self.app.signup.field_password_send_keys(user=self.app.user)
        self.app.signup.field_confirm_password_send_keys(user=self.app.user)
        self.app.signup.button_start_learning_press()
        assert self.app.username.screen_username_is_presented() is not True

    def test_WHEN_email_is_registered_AND_press_start_EXPECTED_username_screen_is_not_presented_TC2230(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.user.email = "artem.merkulov@gmail.com"
        self.app.signup.field_email_send_keys(self.app.user)
        self.app.user.password1, self.app.user.password2 = self.app.string.get_random_two_passwords()
        self.app.signup.field_password_send_keys(self.app.user)
        self.app.signup.field_confirm_password_send_keys(self.app.user)
        self.app.signup.button_start_learning_press()
        assert self.app.username.screen_username_is_presented() is not True

    def test_WHEN_username_sc_open_EXPECTED_4elements_are_presented_TC2300(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.signup.signup_fillall_press_done_wait_username(self.app.user)
        elts_dct = {}
        elts_dct['top_title'] = self.app.username.title_top_is_displayed()
        elts_dct['lower_title'] = self.app.username.title_lower_is_displayed()
        elts_dct['username_field'] = self.app.username.field_username_is_displayed()
        elts_dct['next_button'] = self.app.username.button_next_is_displayed()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_username_is_correct_AND_tap_next_EXPECTED_choseyourrole_is_presented_TC2310(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.signup.signup_fillall_press_done_wait_username(self.app.user)
        self.app.user.username = self.app.string.get_random_username()
        self.app.username.field_username_send_keys(self.app.user)
        self.app.username.button_next_click()
        sleep(1)
        assert self.app.chose_role.screen_choseyourrole_is_presented()

    def test_WHEN_username_is_incorrect_AND_tap_next_EXPECTED_choseyourrole_is_not_presented_TC2310(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.signup.signup_fillall_press_done_wait_username(self.app.user)
        self.app.user.username = self.app.string.get_random_username_short()

        self.app.username.field_username_send_keys(self.app.user)
        self.app.username.button_next_click()
        sleep(1)
        assert self.app.chose_role.screen_choseyourrole_is_presented() is not True

    def test_WHEN_choserole_screen_is_presentede_EXPECTED_elements_are_correct_TC2500(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.signup.signup_fillall_press_done_wait_username(self.app.user)
        self.app.user.username = self.app.string.get_random_username()
        self.app.username.field_username_send_keys(self.app.user)
        self.app.username.button_next_click()

        elts_dct = {}
        elts_dct['top_title'] = self.app.chose_role.title_top_is_displayed()
        elts_dct['below_top_title'] = self.app.chose_role.title_below_top_is_displayed()
        elts_dct['study_button'] = self.app.chose_role.button_study_is_displayed()
        elts_dct['create_project_button'] = self.app.chose_role.button_create_project_is_displayed()
        sleep(1)
        elts_dct['lower_title'] = self.app.chose_role.title_lower_is_displayed()
        for x in elts_dct.values():
            assert x is True


    def test_WHEN_want_create_button_press_EXPECTED_add_contact_info_screen_TC2520(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.chose_role.go_to_choose_role_screen(self.app.user)
        self.app.chose_role.button_create_project_tap()
        assert self.app.cont_inf.screen_add_contact_inf_is_presented()

    def test_WHEN_want_learn_button_press_EXPECTED_add_contact_info_screen_TC2510(self):
        self.app.string.get_random_userdata(self.app.user)
        self.app.chose_role.go_to_choose_role_screen(self.app.user)
        self.app.chose_role.button_study_tap()
        assert self.app.select_topic_learn.screen_select_topic_is_presented()

    def test_WHEN_add_contacts_screen_EXPECTED_elements_are_correct_TC2600(self):
        self.app.cont_inf.go_to_add_contact_inf_screen(self.app.user)
        elts_dct = {}
        elts_dct['top_title'] = self.app.cont_inf.title_top_is_displayed()
        elts_dct['below_top_title'] = self.app.cont_inf.title_below_top_is_displayed()
        elts_dct['skype'] = self.app.cont_inf.field_skype_is_displayed()
        elts_dct['hangouts'] = self.app.cont_inf.field_google_hang_is_displayed()
        elts_dct['next'] = self.app.cont_inf.button_next_is_displayed()

        for x in elts_dct.values():
            assert x is True
    #
    # def test_WHEN_skype_is_entered_EXPECTED_create_project_screen_presented_TC2610(self):
    #     user_data = self.app.cont_inf.go_to_add_contact_inf_screen()
    #     skype = self.app.string.get_random_username()
    #     self.app.cont_inf.field_skype_send_key(skype)
    #     data_confirm = {'email': user_data['email'], 'key': '992927E5B1C8A237875C70A302A34E22'}
    #     self.app.api.general_post(app=self.app, route=self.app.route.email_confirmation,
    #                               data=data_confirm)
    #     self.app.cont_inf.button_next_tap()
    #     assert self.app.select_topic.screen_select_topic_is_presented()




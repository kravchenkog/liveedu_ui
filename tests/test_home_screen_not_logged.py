import pytest


class TestClass():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, app_home):
        self.app = app_home


    def test_WHEN_home_screen_open_AND_not_logged_EXPECTED_sign_up_button_is_presented_TC1000(self):
        assert self.app.home_el.button_signup_is_displayed()

    def test_WHEN_home_screen_open_AND_not_logged_EXPECTED_logo_button_is_presented_TC1000(self):
        assert self.app.home_el.logo_is_presented()

    # def test_WHEN_home_screen_open_AND_not_logged_EXPECTED_learnlive_button_is_presented_TC1000(self):
    #     assert self.app.home_el.button_learnlive_is_displayed()

    def test_WHEN_home_screen_open_AND_not_logged_EXPECTED_learnondemand_button_is_presented_TC1000(self):
        assert self.app.home_el.button_learnondemand_is_displayed()

    def test_WHEN_home_screen_open_AND_not_logged_EXPECTED_pricing_button_is_presented_TC1000(self):
        assert self.app.home_el.button_pricing_is_displayed()

    def test_WHEN_home_screen_open_AND_not_logged_EXPECTED_search_field_is_presented_TC1000(self):
        assert self.app.home_el.button_login_is_displayed()

    def test_WHEN_button_login_press_EXPECTED_login_screen_is_presented_TC1080(self):
        self.app.login.button_login_press_and_wait()
        assert self.app.login.screen_login_is_presented()

    def test_WHEN_button_signup_press_EXPECTED_signup_screen_is_presented_TC1090(self):
        self.app.signup.button_signup_press_and_wait()
        assert self.app.signup.screen_signup_is_displayed()


from time import sleep
import pytest


class TestClass():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, app_live):
        self.app = app_live

    def test_WHEN_live_screen_open_EXPECTED_3general_sections_are_presented_TC3600(self):
        elts_dct = {}
        elts_dct['navigation'] = self.app.live.section_navigation_is_presented()
        elts_dct['header'] = self.app.live.section_header_is_presented()
        elts_dct['main'] = self.app.live.section_main_is_presented()
        for x in elts_dct.values(): assert x

    def test_WHEN_live_screen_open_EXPECTED_8buttons_are_presented_in_navigation_TC3610(self):
        elts_dct = {}
        elts_dct['logo'] = self.app.live.navigation_button_logo_is_presented()
        elts_dct['live_now'] = self.app.live.navigation_button_live_now_is_presented('Live Now')
        elts_dct['projects'] = self.app.live.navigation_button_projects_is_presented('Projects')
        elts_dct['guides'] = self.app.live.navigation_button_guides_is_presented('Guides')
        elts_dct['schedule'] = self.app.live.navigation_button_schedule_is_presented('Schedule')
        elts_dct['requests'] = self.app.live.navigation_button_requests_is_presented('Requests')
        elts_dct['subscribe'] = self.app.live.navigation_button_subscribe_is_presented('Subscribe')
        elts_dct['more'] = self.app.live.navigation_button_more_is_presented('More')
        for x in elts_dct.values(): assert x

    def test_WHEN_logo_pressed_EXPECTED_home_screen_opened_TC3620(self):
        self.app.live.navigation_button_logo_press()
        assert self.app.home_el.home_screen_is_presented()

    def test_WHEN_logo_pressed_EXPECTED_home_screen_opened_TC3631(self):
        self.app.live.navigation_button_livenow_press()
        assert self.app.live.screen_live_is_presented()

    def test_WHEN_live_screen_EXPECTED_live_now_button_selected_by_default_TC3630(self):
        assert self.app.live.screen_live_navigation_is_selected_button('Live Now')

    def test_WHEN_live_screen_AND_projects_but_pressed_EXPECTED_project_scr_opened_TC3640(self):
        self.app.live.navigation_button_projects_press()
        assert self.app.live.navigation_screen_is_changed_to('Projects')

    def test_WHEN_live_screen_AND_guides_but_pressed_EXPECTED_guides_scr_opened_TC3650(self):
        self.app.live.navigation_button_guides_press()
        assert self.app.live.navigation_screen_is_changed_to('Guides')

    def test_WHEN_live_screen_AND_schedule_but_pressed_EXPECTED_schedule_scr_opened_TC3660(self):
        self.app.live.navigation_button_schedule_press()
        assert self.app.live.navigation_screen_is_changed_to('Schedule')

    def test_WHEN_live_screen_AND_requests_but_pressed_EXPECTED_requests_scr_opened_TC3670(self):
        self.app.live.navigation_button_requests_press()
        assert self.app.live.navigation_screen_is_changed_to('Requests')

    def test_WHEN_live_screen_AND_subscribe_but_pressed_EXPECTED_pricing_scr_opened_TC3680(self):
        self.app.live.navigation_button_subscribe_press()
        assert self.app.pricing.screen_pricing_is_presented()

    def test_WHEN_live_screen_AND_more_but_pressed_EXPECTED_12buttons_is_presented_TC3690(self):
        list_of_buttons = ['How it Works', 'Project creator guide', 'Make money', 'Tokens', 'API',
                           'Pastebin', 'About us', 'Blog', 'Press', 'Support', 'Partnership',
                           'Contact us']

        self.app.live.navigation_button_more_press()
        assert self.app.live.navigation_more_sub_elements_are_presented(list_of_buttons)



import pytest
from time import sleep

class TestClass():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, app_project_requests, app_test_users):
        self.app = app_project_requests
        self.app.user_creator = app_test_users.user_creator
        self.app.user_student = app_test_users.user_student


    def test_WHEN_choose_every_subcategory_EXPECTED_requests_lrkated_to_subcategory_TC6220(self, app_project_requests):
        dict_of_subcategories = self.app.request_project.get_list_of_sub_cat()
        assert self.app.request_project.requests_are_related_to_sub_categories(dict_of_subcategories)

    def test_WHEN_requests_button_is_pressed_EXPECTED_project_requests_scr_opens_TC6200(self):
        self.app.home_el.logout_go_home_and_wait()
        self.app.home_el.button_learnlive_click()
        self.app.live.navigation_button_requests_press()
        assert self.app.request_project.screen_project_requests_is_presented()

    def test_WHEN_requests_screen_opened_EXPECTED_5_sections_presented_TC6205(self):
        elts_dct = {}
        elts_dct['main_menu_section'] = self.app.request_project.main_menu_section_is_presented()
        elts_dct['filters_section'] = self.app.request_project.filters_section_is_presented()
        elts_dct['requests_list_section'] = self.app.request_project.requests_list_section_is_presented()
        elts_dct['instruction_section'] = self.app.request_project.instruction_section_is_presented()
        #elts_dct['pagination_section'] = self.app.request_project.pagination_section_is_presented()
        assert all(elts_dct.values())

    def test_WHEN_requests_screen_opened_EXPECTED_5_elements_in_filters_TC6210(self):
        elts_dct = {}
        main_cat_filters = ['All', 'Programming', 'Game development', 'Data science', 'Design',
                            'Artificial intelligence', 'CryptoCurrency', 'VR & AR', 'Cybersecurity']

        elts_dct['main_cat_filters'] = self.app.request_project.main_cat_filters_is_presented(main_cat_filters)
        elts_dct['subcategory_filters'] = self.app.request_project.subcategory_filters_is_presented()
        elts_dct['popularity_latest_sorting'] = self.app.request_project.popularity_latest_sorting_is_presented()
        elts_dct['difficulty_filter'] = self.app.request_project.difficulty_filter_section_is_presented()
        elts_dct['language_filter'] = self.app.request_project.language_filter_is_presented()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_main_category_selected_EXPECTED_all_request_relatred_to_selected_category_TC6215(self):
        assert self.app.request_project.list_of_requests_related_to_each_selected_category()


    def test_WHEN_maincategory_and_subcat_selected_EXPECTED_project_requests_are_proper_TC6222(self, app_project_requests):
        main_cat = 'Programming'
        sub_cat = 'Python'
        assert self.app.request_project.all_requests_related_to_sub_and_main_cat(main_cat, sub_cat)


    def test_WHEN_subcategory_is_selected_EXPECTED_x_button_is_presented_TC6223(self, app_project_requests):
        self.app.request_project.select_and_enter_random_subcategory()
        assert self.app.request_project.close_x_button_is_presented(self.app.request_project.buttons_in_filter_css)

    def test_WHEN_subcategory_is_selected_and_x_pressed_EXPECTED_filter_is_reseted_TC6223(self, app_project_requests):
        filter = self.app.request_project.get_filter_by_text('Choose a category')
        self.app.request_project.select_and_enter_random_subcategory()
        self.app.request_project.close_x_button_click(filter)
        assert self.app.request_project.close_x_button_is_presented(self.app.request_project.buttons_in_filter_css) is not True

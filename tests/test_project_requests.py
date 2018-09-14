import pytest
from time import sleep

class TestClass():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, app_pr_r, app_test_users):
        self.app = app_pr_r
        self.app.user_creator = app_test_users.user_creator
        self.app.user_student = app_test_users.user_student
        self.pr = app_pr_r.request_project


    def test_WHEN_choose_every_subcategory_EXPECTED_requests_lrkated_to_subcategory_TC6220(self, app_pr_r):
        dict_of_subcategories = self.app.request_project.get_list_of_sub_cat()
        assert self.app.request_project.requests_are_related_to_sub_categories(dict_of_subcategories)

    def test_WHEN_requests_button_is_pressed_EXPECTED_project_requests_scr_opens_TC6200(self):
        self.app.home_el.logout_go_home_and_wait()
        self.app.home_el.button_learnlive_click()
        self.app.live.navigation_button_requests_press()
        assert self.app.request_project.screen_project_requests_is_displayed()

    def test_WHEN_requests_screen_opened_EXPECTED_5_sections_presented_TC6205(self):
        elts_dct = {}
        elts_dct['main_menu_section'] = self.pr.main_menu_section_is_presented()
        elts_dct['filters_section'] = self.pr.filters_section_is_presented()
        elts_dct['requests_list_section'] = self.pr.requests_list_section_is_presented()
        elts_dct['instruction_section'] = self.pr.instruction_section_is_presented()
        #elts_dct['pagination_section'] = self.app.request_project.pagination_section_is_presented()
        assert all(elts_dct.values())

    def test_WHEN_requests_screen_opened_EXPECTED_5_elements_in_filters_TC6210(self):
        elts_dct = {}
        main_cat_filters = ['All', 'Programming', 'Game development', 'Data science', 'Design',
                            'Artificial intelligence', 'CryptoCurrency', 'VR & AR', 'Cybersecurity']

        elts_dct['main_cat_filters'] = self.pr.main_cat_filters_is_presented(main_cat_filters)
        elts_dct['subcategory_filters'] = self.pr.subcategory_filters_is_presented()
        elts_dct['popularity_latest_sorting'] = self.pr.popularity_latest_sorting_is_presented()
        elts_dct['difficulty_filter'] = self.pr.difficulty_filter_section_is_presented()
        elts_dct['language_filter'] = self.pr.language_filter_is_presented()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_main_category_selected_EXPECTED_all_request_relatred_to_selected_category_TC6215(self):
        assert self.pr.list_of_requests_related_to_each_selected_category()


    def test_WHEN_maincategory_and_subcat_selected_EXPECTED_project_requests_are_proper_TC6222(self, app_pr_r):
        main_cat = 'Programming'
        sub_cat = 'Python'
        assert self.pr.all_requests_related_to_sub_and_main_cat(main_cat, sub_cat)


    def test_WHEN_subcategory_is_selected_EXPECTED_x_button_is_presented_TC6223(self, app_pr_r):
        self.pr.select_and_enter_random_subcategory()
        assert self.pr.close_x_button_is_presented(self.app.request_project.buttons_in_filter)

    def test_WHEN_subcategory_is_selected_and_x_pressed_EXPECTED_filter_is_reseted_TC6223(self, app_pr_r):
        filter = self.pr.get_filter_by_text('Choose a category')
        self.pr.select_and_enter_random_subcategory()
        self.pr.close_x_button_click(filter, self.pr.choose_a_category)
        assert not self.pr.close_x_button_is_presented(self.pr.buttons_in_filter)

    def test_WHEN_sorting_by_popularity_is_selected_EXPECTED_items_are_sorted_TC6225(self, app_pr_r):
        self.pr.select_value_in_right_filters(0, 'Most Popular') #0=Popular/New 1=Difficulty 2=Language
        assert self.pr.list_of_requests_sorted_by_popularity()

    def test_WHEN_sorting_by_latest_is_selected_EXPECTED_items_are_sorted_TC6226(self, app_pr_r):
        self.pr.select_value_in_right_filters(0, 'Latest') #0=Popular/New 1=Difficulty 2=Language
        assert self.pr.list_of_requests_sorted_by_latest()

    def test_WHEN_filter_by_difficulty_is_selected_EXPECTED_items_are_filtered_TC6231(self, app_pr_r):
        self.pr.select_value_in_right_filters(1, 'Beginner')
        list_api = self.pr.get_list_of_requests_by_api(difficulty=1)
        assert self.pr.list_of_pr_req_related_to_api_list(list_api)

    def test_WHEN_diffic_is_selected_and_x_pressed_EXPECTED_filter_is_reseted_TC6232(self, app_pr_r):
        filter_d = self.pr.get_difficulty_filter()
        button = self.pr.select_value_in_right_filters(1, 'Beginner')
        self.pr.close_x_button_click(filter_d, button, 1) #1 if click of element (not locator)
        assert not self.pr.close_x_button_is_presented(self.pr.buttons_in_filter, filter_d)

    def test_WHEN_filter_by_language_is_selected_EXPECTED_items_are_filtered_TC6231(self, app_pr_r):
        self.pr.select_value_in_right_filters(2, 'English')
        list_api = self.pr.get_list_of_requests_by_api(language='en') #english
        assert self.pr.list_of_pr_req_related_to_api_list(list_api)

    def test_WHEN_lang_is_selected_and_x_pressed_EXPECTED_filter_is_reseted_TC6232(self, app_pr_r):
        filter_l = self.pr.get_language_filter()
        button = self.pr.select_value_in_right_filters(2, 'English')
        self.pr.close_x_button_click(filter_l, button, 1) #1 if click of element (not locator)
        assert not self.pr.close_x_button_is_presented(self.pr.buttons_in_filter, filter_l)

    def test_WHEN_several_filters_are_selected_EXPECTED_items_are_filtered_TC6231(self, app_pr_r):
        self.pr.select_value_in_right_filters(2, 'English')
        self.pr.select_value_in_right_filters(1, 'Beginner')
        list_api = self.pr.get_list_of_requests_by_api(language='en', difficulty=1)  # english
        assert self.pr.list_of_pr_req_related_to_api_list(list_api)

import pytest
import time
import random

class TestClassPrRequest_not_logged():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, pr_notlogged, app_test_users):
        self.app = pr_notlogged
        self.app.user_creator = app_test_users.user_creator
        self.app.user_student = app_test_users.user_student
        self.pr = pr_notlogged.request_project


    def test_WHEN_choose_every_subcategory_EXPECTED_requests_lrkated_to_subcategory_TC6220(self, pr_notlogged):
        dict_of_subcategories = self.app.request_project.get_list_of_sub_cat()
        assert self.app.request_project.requests_are_related_to_sub_categories(dict_of_subcategories)

    def test_WHEN_requests_button_is_pressed_EXPECTED_project_requests_scr_opens_TC6200(self):
        self.app.home_el.logout_go_home_and_wait()
        self.app.home_el.button_learnondemand_click()
        self.app.live.navigation_button_press('Requests')
        assert self.app.request_project.screen_project_requests_is_displayed()

    def test_WHEN_requests_screen_opened_EXPECTED_5_sections_presented_TC6205(self):
        elts_dct = {}
        elts_dct['main_menu_section'] = self.pr.main_menu_section_is_displayed()
        elts_dct['filters_section'] = self.pr.filters_section_is_displayed()
        elts_dct['requests_list_section'] = self.pr.requests_list_section_is_displayed()
        elts_dct['instruction_section'] = self.pr.instruction_section_is_presented()
        #elts_dct['pagination_section'] = self.app.request_project.pagination_section_is_presented()
        assert all(elts_dct.values())

    def test_WHEN_requests_screen_opened_EXPECTED_5_elements_in_filters_TC6210(self):
        elts_dct = {}
        main_cat_filters = ['All', 'Programming', 'Game development', 'Data science', 'Design',
                            'Artificial intelligence', 'CryptoCurrency', 'VR & AR', 'Cybersecurity']

        elts_dct['main_cat_filters'] = self.pr.main_cat_filters_is_presented(main_cat_filters)
        elts_dct['subcategory_filters'] = self.pr.subcategory_filters_is_presented()
        elts_dct['popularity_latest_sorting'] = self.pr.sort_filter_is_presented('Most Popular')
        elts_dct['difficulty_filter'] = self.pr.sort_filter_is_presented('Difficulty')
        elts_dct['language_filter'] = self.pr.sort_filter_is_presented('Language')
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_main_category_selected_EXPECTED_all_request_relatred_to_selected_category_TC6215(self):
        assert self.pr.list_of_requests_related_to_each_selected_category()


    def test_WHEN_maincategory_and_subcat_selected_EXPECTED_project_requests_are_proper_TC6222(self, pr_notlogged):
        main_cat = 'Programming'
        sub_cat = 'Python'
        assert self.pr.all_requests_related_to_sub_and_main_cat(main_cat, sub_cat)


    def test_WHEN_subcategory_is_selected_EXPECTED_x_button_is_presented_TC6223(self, pr_notlogged):
        self.pr.select_and_enter_random_subcategory()
        assert self.pr.close_x_button_is_presented(self.app.request_project.buttons_in_filter)

    def test_WHEN_subcategory_is_selected_and_x_pressed_EXPECTED_filter_is_reseted_TC6223(self, pr_notlogged):
        filter = self.pr.get_filter_by_text('Choose a category')
        self.pr.select_and_enter_random_subcategory()
        self.pr.close_x_button_click(filter, self.pr.sub_cat_filter)
        assert not self.pr.close_x_button_is_presented(self.pr.buttons_in_filter)

    def test_WHEN_sorting_by_popularity_is_selected_EXPECTED_items_are_sorted_TC6225(self, pr_notlogged):
        self.pr.select_value_in_right_filters(0, 'Most Popular') #0=Popular/New 1=Difficulty 2=Language
        assert self.pr.list_of_requests_sorted_by_popularity()

    def test_WHEN_sorting_by_latest_is_selected_EXPECTED_items_are_sorted_TC6226(self, pr_notlogged):
        self.pr.select_value_in_right_filters(0, 'Latest') #0=Popular/New 1=Difficulty 2=Language
        assert self.pr.list_of_requests_sorted_by_latest()

    def test_WHEN_filter_by_difficulty_is_selected_EXPECTED_items_are_filtered_TC6231(self, pr_notlogged):
        self.pr.select_value_in_right_filters(1, 'Beginner')
        list_api = self.pr.get_list_of_requests_by_api(difficulty=1)
        assert self.pr.list_of_pr_req_related_to_api_list(list_api)

    def test_WHEN_diffic_is_selected_and_x_pressed_EXPECTED_filter_is_reseted_TC6232(
            self,  pr_notlogged):

        filter_d = self.pr.get_difficulty_filter()
        button = self.pr.select_value_in_right_filters(1, 'Beginner')
        self.pr.close_x_button_click(filter_d, button, 1) #1 if click of element (not locator)
        assert not self.pr.close_x_button_is_presented(self.pr.buttons_in_filter, filter_d)

    def test_WHEN_filter_by_language_is_selected_EXPECTED_items_are_filtered_TC6231(
            self, pr_notlogged):

        self.pr.select_value_in_right_filters(2, 'English')
        list_api = self.pr.get_list_of_requests_by_api(language='en') #english
        assert self.pr.list_of_pr_req_related_to_api_list(list_api)

    def test_WHEN_lang_is_selected_and_x_pressed_EXPECTED_filter_is_reseted_TC6232(self, pr_notlogged):
        filter_l = self.pr.get_language_filter()
        button = self.pr.select_value_in_right_filters(2, 'English')
        self.pr.close_x_button_click(filter_l, button, 1) #1 if click of element (not locator)
        assert not self.pr.close_x_button_is_presented(self.pr.buttons_in_filter, filter_l)


    def test_WHEN_several_filters_are_selected_EXPECTED_items_are_filtered_TC6231(self, pr_notlogged):
        self.pr.select_value_in_right_filters(2, 'English')
        self.pr.select_value_in_right_filters(1, 'Beginner')
        list_api = self.pr.get_list_of_requests_by_api(language='en', difficulty=1)  # english
        assert self.pr.list_of_pr_req_related_to_api_list(list_api)

    def test_WHEN_user_is_not_logged_EXPECTED_elements_in_pr_correct_TC6252(self, pr_notlogged):
        elts_dct = {}
        elts_dct['likes_counter'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.likes_button)
        elts_dct['likes_button'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.likes_counter)
        elts_dct['title'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.project_request_titles)
        elts_dct['description'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.description_of_pr)
        elts_dct['language'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.language_title)
        elts_dct['subcategory_icon'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.subcategory_icon)
        elts_dct['name_of_creator'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.creator_name)
        elts_dct['creation_date'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.date_of_proj_request)


        assert all(elts_dct.values())
class TestClassPrRequest_student():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, pr_student, app_test_users):
        self.app = pr_student
        self.app.user_creator = app_test_users.user_creator
        self.app.user_student = app_test_users.user_student
        self.pr = pr_student.request_project

    def test_WHEN_student_is_logged_EXPECTED_elements_in_pr_correct_TC6250(self, pr_student):
        elts_dct = {}
        elts_dct['likes_counter'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.likes_button)
        elts_dct['likes_button'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.likes_counter)
        elts_dct['title'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.project_request_titles)
        elts_dct['description'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.description_of_pr)
        elts_dct['language'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.language_title)
        elts_dct['subcategory_icon'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.subcategory_icon)
        elts_dct['name_of_creator'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.creator_name)
        elts_dct['creation_date'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.date_of_proj_request)


        assert all(elts_dct.values())

    def test_WHEN_student_pressed_likes_button_EXPECTED_counter_is_increased_TC6260(self, pr_student):
        counter_value = self.pr.get_counter_of_likes(0)
        self.pr.press_likes_button(0)
        time.sleep(3)
        counter_value_after = self.pr.get_counter_of_likes(0)
        assert counter_value + 1 == counter_value_after

    def test_WHEN_student_is_logged_EXPECTED_make_section_is_correct_TC6290(self, pr_student):
        elts_dct = {}
        elts_dct['icon_of_section'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.make_section_icon)
        elts_dct['make your own request'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.request_project_button)
        elts_dct['text'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.make_section_text)
        elts_dct['title'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.make_section_title)
        assert all(elts_dct.values())

    def test_WHEN_request_project_button_pressed_EXPECTED_rp_popup_appears_TC6292(self, pr_student):
        self.app.general.but_press(self.pr.request_project_button)
        assert self.app.general.el_is_displayed(self.pr.pr_popup)

    def test_WHEN_pr_popup_opens_EXPECTED_fileds_are_correct_TC6300(self, pr_student):
        self.app.general.but_press(self.pr.request_project_button)
        elts_dct = {}
        elts_dct['main title'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.pr_popup_main_title)
        elts_dct['close_x_button'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.close_popup_button)
        elts_dct['pr name'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.pr_popup_pname)
        elts_dct['choose a category, difficulty, language'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.pr_popup_cat_dif_lang)
        elts_dct['choose a subcategory'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.pr_popup_subcategory)
        elts_dct['describe your idea'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.pr_popup_description)
        elts_dct['submit request'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.pr_popup_submit_button)
        assert all(elts_dct.values())

    def test_WHEN_x_button_pressed_in_popup_EXPECTED_pr_popup_closed_TC6301(self, pr_student):
        self.app.general.but_press(self.pr.request_project_button)
        self.app.general.but_press(self.pr.close_popup_button)
        assert not self.app.general.el_is_presented(self.pr.pr_popup)

    def _test_WHEN_all_fields_filled_in_prpopup_EXPECTED_pr_is_saved(self, pr_student):
        random_pr = self.pr.get_random_pr_data()
        self.app.general.but_press(self.pr.request_project_button)
        self.app.general.send_k(self.pr.pr_popup_pname, random_pr['pr_name'])
        self.app.general.send_k(self.pr.pr_popup_description, random_pr['description'])
        self.pr.choose_value_on_popup(random_pr, 'Choose a topic')

        self.app.general.but_press(self.pr.pr_popup_submit_button)
        assert not self.app.general.el_is_presented(self.pr.pr_popup)



class TestClassPrRequest_creator():
    @pytest.fixture(autouse=True)
    def _request_signup_page(self, pr_creator, app_test_users):
        self.app = pr_creator
        self.app.user_creator = app_test_users.user_creator
        self.app.user_student = app_test_users.user_student
        self.pr = pr_creator.request_project



    def test_WHEN_creator_is_logged_EXPECTED_elements_in_pr_correct_TC6251(self, pr_creator):
        elts_dct = {}
        elts_dct['likes_counter'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.likes_button)
        elts_dct['likes_button'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.likes_counter)
        elts_dct['title'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.project_request_titles)
        elts_dct['description'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.description_of_pr)
        elts_dct['language'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.language_title)
        elts_dct['subcategory_icon'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.subcategory_icon)
        elts_dct['name_of_creator'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.creator_name)
        elts_dct['creation_date'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.date_of_proj_request)
        elts_dct['create_project'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.create_this_project)


        assert all(elts_dct.values())

    def test_WHEN_create_project_button_is_pressed_EXPECTED_creation_is_started_TC6275(self, pr_creator):
        self.pr.press_random_create_this_proj_button()
        assert self.app.general.get_txt_of_el(self.pr.main_title) == 'CREATE PROJECT'

    def test_WHEN_creator_is_logged_EXPECTED_make_section_is_correct_TC6291(self, pr_creator):
        elts_dct = {}
        elts_dct['icon_of_section'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.make_section_icon)
        elts_dct['text'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.make_section_text)
        elts_dct['title'] = self.pr.pr_element_is_displayed_in_each(
            self.pr.make_section_title)
        assert all(elts_dct.values())


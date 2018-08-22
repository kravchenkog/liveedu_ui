import pytest


class TestClass():
    @pytest.fixture(autouse=True)
    def _request_pricing_page(self, app_pricing):
        self.app = app_pricing

    # @staticmethod
    # def tt(elts_dct):
    #     for x in elts_dct.values():
    #         assert x is True

    def test_WHEN_pricing_screen_open_EXPECTED_10general_sections_are_presented_TC3400(self):
        elts_dct = {}
        elts_dct['1_section'] = self.app.pricing.main_section_1_is_presented()
        elts_dct['2_section'] = self.app.pricing.main_section_2_is_presented()
        elts_dct['3_section'] = self.app.pricing.main_section_3_is_presented()
        elts_dct['4_section'] = self.app.pricing.main_section_4_is_presented()
        elts_dct['5_section'] = self.app.pricing.main_section_5_is_presented()
        elts_dct['6_section'] = self.app.pricing.main_section_6_is_presented()
        elts_dct['7_section'] = self.app.pricing.main_section_7_is_presented()
        elts_dct['8_section'] = self.app.pricing.main_section_8_is_presented()
        elts_dct['9_section'] = self.app.pricing.main_section_9_is_presented()
        elts_dct['10_section'] = self.app.pricing.main_section_10_is_presented()

        for x in elts_dct.values(): assert x is True


    def test_WHEN_pricing_screen_EXPECTED_in_1st_section_7el_TC3410(self):
        elts_dct = {}
        elts_dct['1sec_top_title'] = self.app.pricing.sec1_title_top_is_presented()
        elts_dct['1sec_2nd_title'] = self.app.pricing.sec1_title_2nd_is_presented()
        elts_dct['1sec_switcher'] = self.app.pricing.sec1_switcher_is_presented()
        elts_dct['1sec_icons_names_3'] = self.app.pricing.sec1_icon_name_is_presented()
        elts_dct['1sec_prices'] = self.app.pricing.sec1_prices_is_presented()
        elts_dct['1sec_bonuses_list'] = self.app.pricing.sec1_bonuses_list_is_presented()
        elts_dct['1sec_button_try'] = self.app.pricing.sec1_button_try_is_presented()
        for x in elts_dct.values():
            assert x is True
    def test(self):
        pass

    def test_WHEN_pricing_screen_EXPECTED_in_1st_section_switcher_in_annual_state_default_TC3420(self):
        assert self.app.pricing.switcher_default_state_is_annual()


    def test_WHEN_pricing_screen_open_EXPECTED_8elements_in_2nd_section_TC3430(self):
        elts = ['Programming', 'Design', 'Data Science', 'Artificial Intelligence',
                'AR & VR', 'Cybersecurity', 'Cryptocurrency', 'Game Development']
        elts_in = self.app.pricing.sec2_all_elements_texts()

        assert [x in elts for x in elts_in]

    def test_WHEN_pricing_screen_open_EXPECTED_4rows_in_3nd_section_TC3440(self):
        elts_dct = {}
        elts_dct['main_titles'] = self.app.pricing.sec3_main_titles_3_is_presented()
        elts_dct['images'] = self.app.pricing.sec3_images_3_is_presented()
        elts_dct['subtitles'] = self.app.pricing.sec3_subtitles_3_is_presented()
        elts_dct['titles_second_row'] = self.app.pricing.sec3_second_row_8el_is_presented()
        for x in elts_dct.values():
            assert x is True


    def test_WHEN_pricing_screen_open_EXPECTED_3_elements_in_4th_sec_TC3450(self):
        elts_dct = {}
        elts_dct['icon'] = self.app.pricing.sec4_icon_is_presented()
        elts_dct['top_title'] = self.app.pricing.sec4_top_title_is_presented()
        elts_dct['lower_title'] = self.app.pricing.sec4_lower_title_is_presented()
        for x in elts_dct.values():
            assert x is True

    def test_WHEN_pricing_screen_open_EXPECTED_3_elements_in_5th_sec_TC3460(self):
        elts_dct = {}
        elts_dct['icons'] = self.app.pricing.sec5_icons_is_presented()
        elts_dct['top_titles'] = self.app.pricing.sec5_top_titles_is_presented()
        elts_dct['lower_titles'] = self.app.pricing.sec5_lower_titles_is_presented()
        for x in elts_dct.values():
            assert x is True


    def test_WHEN_pricing_screen_open_EXPECTED_2_elements_in_6th_and_10th_sec_TC3470_3510(self):
        elts_dct = {}
        elts_dct['titles'] = self.app.pricing.sec6and10_titles_are_presented()
        elts_dct['buttons'] = self.app.pricing.sec6and10_buttons_are_presented()

        for x in elts_dct.values():
            assert x is True

    def test_WHEN_pricing_screen_open_EXPECTED_2_subsections_in_7th_sec_TC3480(self):
        elts_dct = {}
        elts_dct['titles'] = self.app.pricing.sec7_titles_are_presented()
        elts_dct['reviews'] = self.app.pricing.sec7_reviews_are_presented()

        for x in elts_dct.values():
            assert x is True

    def test_WHEN_pricing_screen_open_EXPECTED_2_subsections_in_8th_sec_TC3490(self):
        elts_dct = {}
        elts_dct['titles'] = self.app.pricing.sec8_titles_are_presented()
        elts_dct['projects'] = self.app.pricing.sec8_projects_are_presented()

        for x in elts_dct.values():
            assert x is True

    def test_WHEN_pricing_screen_open_EXPECTED_video_preview_is_correct_in_8th_sec_TC3490(self):
        elts_dct = {}
        elts_dct['image_preview'] = self.app.pricing.sec8_image_preview_are_presented()
        elts_dct['rating'] = self.app.pricing.sec8_rating_are_presented()
        elts_dct['counter_of_views'] = self.app.pricing.sec8_counter_of_view_are_presented()
        elts_dct['name_of_project'] = self.app.pricing.sec8_name_project_are_presented()
        elts_dct['project_creator'] = self.app.pricing.sec8_project_creator_are_presented()
        for x in elts_dct.values(): assert x is True

    def test_WHEN_pricing_screen_open_EXPECTED_2_elements_are_correct_in_9th_sec_TC3500(self):
        elts_dct = {}
        elts_dct['title'] = self.app.pricing.sec9_title_are_presented()
        elts_dct['faq_list'] = self.app.pricing.sec9_faq_list8_are_presented()

        for x in elts_dct.values(): assert x is True

    def test_WHEN_pricing_screen_open_AND_faq_element_press_EXPECTED_element_expanded_sec_TC3510(self):
        self.app.pricing.button_faq_rendompress()
        assert self.app.pricing.button_faq_is_expanded()
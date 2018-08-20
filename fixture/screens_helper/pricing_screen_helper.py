import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class PricingHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def screen_pricing_is_presented(self):
        elements = self.driver.find_elements_by_css_selector("div.global-faq-accordion")
        if len(elements) > 0:
            return True
        else:
            return False

    def main_section_1_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._3Cz_2'))
    def main_section_2_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._3U5zj'))
    def main_section_3_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._1iqyF'))
    def main_section_4_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._2d1zH'))
    def main_section_5_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._2M8gV'))
    def main_section_6_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._3W4c4'))
    def main_section_7_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._2j0yL'))
    def main_section_8_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('div._2WsdE'))
    def main_section_9_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section.NEXHN'))
    def main_section_10_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('section._3W4c4'))

    def sec1_title_top_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('h2._2rs1N'))
    def sec1_title_2nd_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('p._1Cdl0'))
    def sec1_switcher_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('div._1EN96'))
    def sec1_icon_name_is_presented(self):
        elements = self.app.driver.find_elements_by_css_selector('div._1zvVP')
        if len(elements) == 4:
            return True


    def sec1_prices_is_presented(self):
        elements = self.app.driver.find_elements_by_css_selector('div.EFjG8')
        if len(elements) == 3:
            return True


    def sec1_bonuses_list_is_presented(self):
        elements = self.app.driver.find_elements_by_css_selector('ul._34Q7P')
        if len(elements) == 4:
            return True


    def sec1_button_try_is_presented(self):
        elements = self.app.driver.find_elements_by_css_selector('div._31k7N')
        if len(elements) == 4:
            return True

    def switcher_default_state_is_annual(self):
        el = self.app.driver.find_element_by_css_selector('p[class="_3lW-D _3l3bp"]')
        if 'Annual' in el.text:
            return True


    def sec2_all_elements_texts(self):
        elements = self.driver.find_elements_by_css_selector('p._2lT9G')
        texts = [x.text for x in elements]
        return texts

    def sec3_main_titles_3_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('h2._3Svjc')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec3_images_3_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('img._1wB1S')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec3_subtitles_3_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('p._1yPQN')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec3_second_row_8el_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('li._1vVHM')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 8:
            return False
        return True


    def sec4_icon_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                              ('svg._2jxhU'))
    def sec4_top_title_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                              ('h2._2PCtJ'))
    def sec4_lower_title_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                              ('p._3r0G0'))

    def sec5_icons_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('div._1rLzo')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec5_top_titles_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('p._1UoJ0')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec5_lower_titles_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('p.pyqlO')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec6and10_titles_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('h2.qMXHL')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 2:
            return False
        return True
    def sec6and10_buttons_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('a._35klt')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 2:
            return False
        return True

    def sec7_titles_are_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     ('h2.APSOh'))
    def sec7_reviews_are_presented(self):
        elements = self.app.driver.find_elements_by_css_selector('li._2hHoa')
        el_dict = {}
        el_dict['quotes'] = [self.app.general.element_is_displayed
                         (x.find_element_by_css_selector('svg._3IIv8'))for x in elements]

        el_dict['text'] = [self.app.general.element_is_displayed
                  (x.find_element_by_css_selector('p._28t_a')) for x in elements]
        el_dict['photo'] = [self.app.general.element_is_displayed
                  (x.find_element_by_css_selector('div._15-bd')) for x in elements]
        el_dict['name'] = [self.app.general.element_is_displayed
                  (x.find_element_by_css_selector('p._1XJkU')) for x in elements]
        el_dict['position'] = [self.app.general.element_is_displayed
                  (x.find_element_by_css_selector('p._35P51')) for x in elements]
        #el_dict['position'][0] = 'False'
        keys = el_dict.keys()
        for k in keys:
            for x in el_dict[k]:
                if x is not True:
                    return False

        return True

    def sec8_titles_are_presented(self):
        return self.app.general.element_is_displayed(self.app.driver.find_element_by_css_selector('h2._1UcFP'))


    def sec8_projects_are_presented(self):
        return self.app.general.element_is_displayed(self.app.driver.find_element_by_css_selector('ul._2qkDP'))

    def sec8_image_preview_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector('img._3HPu6')]

        res = [x for x in elements_disp if not x]
        if res and len(elements_disp)==5:
            return False
        return True
    # div[class="dv-star-rating dv-star-rating-non-editable _1mKjs"]
    def sec8_rating_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector
                         ('div[class="dv-star-rating dv-star-rating-non-editable _1mKjs"]')]

        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True
    def sec8_counter_of_view_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector
                         ('div._6tuaY')]

        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True
    def sec8_name_project_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector
                         ('p._3q1hj')]

        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True
    def sec8_project_creator_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector
                         ('p._3tluy')]

        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True

    def sec9_title_are_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector('h2._1gbPJ'))
    def sec9_faq_list8_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed(x)
                         for x in self.app.driver.find_elements_by_css_selector
                         ('button.panel__label')]

        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True

    def button_faq_rendompress(self):
        all_faq_but = self.app.driver.find_elements_by_css_selector('button.panel__label')
        random_faq = all_faq_but[random.randint(0, len(all_faq_but)-1)]
        random_faq.click()

    def button_faq_is_expanded(self):
        return self.driver.find_element_by_css_selector('div[aria-expanded="true"]').is_displayed()


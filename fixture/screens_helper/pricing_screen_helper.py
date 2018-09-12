import random
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class PricingHelper():

    def __init__(self, app):
        self.app = app
        self.section1_css = 'section._3Cz_2'
        self.section2_css = 'section._3U5zj'
        self.section3_css = 'section._1iqyF'
        self.section4_css = 'section._2d1zH'
        self.section5_css = 'section._2M8gV'
        self.section6_css = 'section._3W4c4'
        self.section7_css = 'section._2j0yL'
        self.section8_css = 'div._2WsdE'
        self.section9_css = 'section.NEXHN'
        self.section10_css = 'section._3W4c4'
        self.title_top = 'h2._2rs1N'
        self.sec1_title_2nd = 'p._1Cdl0'
        self.sec1_switcher_css = 'div._1EN96'
        self.sec1_icon_name_css = 'div._1zvVP'
        self.sec1_prices_css = 'div.EFjG8'
        self.sec1_bonuses = 'ul._34Q7P'
        self.sec1_button_try = 'div._31k7N'

    def screen_pricing_is_presented(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, "div.global-faq-accordion")

    def main_section_1_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section1_css)

    def main_section_2_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section2_css)

    def main_section_3_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section3_css)

    def main_section_4_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section4_css)

    def main_section_5_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section5_css)

    def main_section_6_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section6_css)

    def main_section_7_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section7_css)

    def main_section_8_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section8_css)

    def main_section_9_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section9_css)

    def main_section_10_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.section10_css)

    def sec1_title_top_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.title_top)

    def sec1_title_2nd_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.sec1_title_2nd)

    def sec1_switcher_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.sec1_switcher_css)

    def sec1_icon_name_is_presented(self):
        if len(self.app.general.find_elementS_and_return
                   (By.CSS_SELECTOR, self.sec1_icon_name_css)) == 4:
            return True
        else:
            return False

    def sec1_prices_is_presented(self):
        if len(self.app.general.find_elementS_and_return
                   (By.CSS_SELECTOR, self.sec1_prices_css)) == 3:
            return True
        else:
            return False

    def sec1_bonuses_list_is_presented(self):
        if len(self.app.general.find_elementS_and_return
                   (By.CSS_SELECTOR, self.sec1_bonuses)) == 4:
            return True
        else:
            return False

    def sec1_button_try_is_presented(self):
        if len(self.app.general.find_elementS_and_return
                   (By.CSS_SELECTOR, self.sec1_button_try)) == 4:
            return True
        else:
            return False

    def switcher_default_state_is_annual(self):

        el = self.app.general.find_element_and_return(By.CSS_SELECTOR, 'p[class="_3lW-D _3l3bp"]')
        if 'Annual' in el.text:
            return True


    def sec2_all_elements_texts(self):

        elements = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'p._2lT9G')
        texts = [x.text for x in elements]
        return texts

    def sec3_main_titles_3_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'h2._3Svjc')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec3_images_3_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'img._1wB1S')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True


    def sec3_subtitles_3_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'p._1yPQN')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec3_second_row_8el_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'li._1vVHM')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 8:
            return False
        return True

    def sec4_icon_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'svg._2jxhU')

    def sec4_top_title_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'h2._2PCtJ')

    def sec4_lower_title_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'p._3r0G0')

    def sec5_icons_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'div._1rLzo')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec5_top_titles_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'p._1UoJ0')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec5_lower_titles_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'p.pyqlO')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 3:
            return False
        return True

    def sec6and10_titles_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'h2.qMXHL')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 2:
            return False
        return True

    def sec6and10_buttons_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'a._35klt')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 2:
            return False
        return True

    def sec7_titles_are_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'h2.APSOh')

    def sec7_reviews_are_presented(self):
        elements = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'li._2hHoa')
        el_dict = {}
        el_dict['quotes'] = [self.app.general.element_is_displayed(
            By.CSS_SELECTOR, 'svg._3IIv8') for x in elements]
        el_dict['text'] = [self.app.general.element_is_displayed(
            By.CSS_SELECTOR, 'p._28t_a') for x in elements]
        el_dict['photo'] = [self.app.general.element_is_displayed(
            By.CSS_SELECTOR, 'div._15-bd') for x in elements]
        el_dict['name'] = [self.app.general.element_is_displayed(
            By.CSS_SELECTOR, 'p._1XJkU') for x in elements]
        el_dict['position'] = [self.app.general.element_is_displayed(
            By.CSS_SELECTOR, 'p._35P51') for x in elements]

        #el_dict['position'][0] = 'False'
        keys = el_dict.keys()
        for k in keys:
            for x in el_dict[k]:
                if x is not True:
                    return False

        return True

    def sec8_titles_are_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'h2._1UcFP')


    def sec8_projects_are_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'ul._2qkDP')

    def sec8_image_preview_are_presented(self):

        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(
                By.CSS_SELECTOR, 'img._3HPu6')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True
    def sec8_rating_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(
                By.CSS_SELECTOR, 'div[class="dv-star-rating dv-star-rating-non-editable _1mKjs"]')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True

    def sec8_counter_of_view_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(
                By.CSS_SELECTOR, 'div._6tuaY')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True

    def sec8_name_project_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(
                By.CSS_SELECTOR, 'p._3q1hj')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True

    def sec8_project_creator_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(
                By.CSS_SELECTOR, 'p._3tluy')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True

    def sec9_title_are_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'h2._1gbPJ')


    def sec9_faq_list8_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elementS_and_return(
                By.CSS_SELECTOR, 'button.panel__label')]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 5:
            return False
        return True

    def button_faq_rendompress(self):
        all_faq_but = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'button.panel__label')
        random_faq = all_faq_but[random.randint(0, len(all_faq_but)-1)]
        self.app.general.button_press_element(random_faq)

    def button_faq_is_expanded(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, 'div[aria-expanded="true"]')


import random
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class PricingHelper():

    def __init__(self, app):
        self.app = app
        self.file_pricing1 = 'slider'
        self.file_pricing2 = 'topics'
        self.file_pricing3 = "features"
        self.file_pricing4 = "quality-control"
        self.file_pricing5 = 'benefits'
        self.file_pricing6 = "subscription-cta"
        self.file_pricing7 = "reviews"
        self.file_pricing8 = "projects"
        self.file_pricing9 = "faq"
        self.file_pricing10 = 'slider'
        self.file_pricing11 = "annual-switcher"
        self.file_pricing12 = "plan-card"


        self.slider_section = {
            By.CSS_SELECTOR: "section[class^='{}__slider']".format(self.file_pricing1)}
        self.categories_section = {
            By.CSS_SELECTOR: "section[class^='{}__topics']".format(self.file_pricing2)}
        self.features_section = {
            By.CSS_SELECTOR: "section[class^='{}__features']".format(self.file_pricing3)}
        self.quality_control_section = {
            By.CSS_SELECTOR: "section[class^='{}__quality']".format(self.file_pricing4)}
        self.benefits_section = {
            By.CSS_SELECTOR: "section[class^='{}__benefits']".format(self.file_pricing5)}

        self.subscription_cta_sections = {
            By.CSS_SELECTOR: "section[class^='{}__subscription-cta']".format(self.file_pricing6)}
        self.reviews_section = {
            By.CSS_SELECTOR: "section[class^='{}__reviews']".format(self.file_pricing7)}
        self.projects_section = {
            By.CSS_SELECTOR: "div[class^='{}__projects']".format(self.file_pricing8)}
        self.faq_section = {
            By.CSS_SELECTOR: "section[class^='{}__faq']".format(self.file_pricing9)}

        self.sec1_title = {
            By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_pricing10)}
        self.sec1_text = {
            By.CSS_SELECTOR: "p[class^='{}__text']".format(self.file_pricing10)}
        self.sec1_switcher = {
            By.CSS_SELECTOR: "span[class^='{}__switcher']".format(self.file_pricing11)}
        self.sec1_icons = {
            By.CSS_SELECTOR: "div[class^='{}__header']".format(self.file_pricing12)}
        self.sec1_prices = {
            By.CSS_SELECTOR: "div[class^='{}__price']".format(self.file_pricing12)}
        self.sec1_benefits = {
            By.CSS_SELECTOR: "div[class^='{}__benefits']".format(self.file_pricing12)}
        self.sec1_try_button = {
            By.CSS_SELECTOR: "a[class^='{}__button']".format(self.file_pricing12)}
        self.sec1_switcher_active = {
            By.CSS_SELECTOR: "p[class*='{}__active']".format(self.file_pricing11)}
        self.sec2_categories_titles = {
            By.CSS_SELECTOR: "p[class^='{}__title']".format(self.file_pricing2)}
        self.sec5_icons = {
            By.CSS_SELECTOR: "div[class^='{}__illustration']".format(self.file_pricing5)}
        self.sec5_titles = {
            By.CSS_SELECTOR: "p[class^='{}__title']".format(self.file_pricing5)}
        self.sec5_titles_lower = {
            By.CSS_SELECTOR: "p[class^='{}__text']".format(self.file_pricing5)}
        self.sec4_icon = {
            By.CSS_SELECTOR: "svg[class^='{}__icon']".format(self.file_pricing4)}
        self.sec4_title = {
            By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_pricing4)}
        self.sec4_text = {
            By.CSS_SELECTOR: "p[class^='{}__text']".format(self.file_pricing4)}
        self.sec6_10_titles = {
            By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_pricing6)}
        self.sec6_10_buttons = {
            By.CSS_SELECTOR: "a[class^='{}__cta']".format(self.file_pricing6)}
        self.sec7_title = {
            By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_pricing7)}
        self.sec7_item_icons = {
            By.CSS_SELECTOR: "svg[class^='{}']".format(self.file_pricing7)}
        self.sec7_item_text = {
            By.CSS_SELECTOR: "p[class^='{}__item-text']".format(self.file_pricing7)}
        self.sec7_item_user_avatar = {
            By.CSS_SELECTOR: "div[class^='{}__item-user-avatar']".format(self.file_pricing7)}
        self.sec7_item_user_name = {
            By.CSS_SELECTOR: "p[class^='{}__item-user-name']".format(self.file_pricing7)}
        self.sec7_item_user_position = {
            By.CSS_SELECTOR: "p[class^='{}__item-user-position']".format(self.file_pricing7)}
        self.sec7_items = {
            By.CSS_SELECTOR: "li[class^='{}__item']".format(self.file_pricing7)}
        self.sec8_title = {
            By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_pricing8)}
        self.sec8_list = {
            By.CSS_SELECTOR: "ul[class^='{}__list']".format(self.file_pricing8)}
        self.sec9_title = {
            By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_pricing9)}
        self.expended_faq = {By.CSS_SELECTOR: 'div[aria-expanded="true"]'}

    # item-icon-svg
    def screen_pricing_is_presented(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, "div.global-faq-accordion")

    def main_section_1_is_presented(self):
        return self.app.general.el_is_displayed(self.slider_section)

    def main_section_2_is_presented(self):
        return self.app.general.el_is_displayed(self.categories_section)

    def main_section_3_is_presented(self):
        return self.app.general.el_is_displayed(self.features_section)

    def main_section_4_is_presented(self):
        return self.app.general.el_is_displayed(self.quality_control_section)

    def main_section_5_is_presented(self):
        return self.app.general.el_is_displayed(self.benefits_section)

    def main_section_6_is_presented(self):
        els = self.app.general.find_elS_and_return(self.subscription_cta_sections)
        return self.app.general.element_is_displayed_by_element(els[0])

    def main_section_7_is_presented(self):
        return self.app.general.el_is_displayed(self.reviews_section)

    def main_section_8_is_presented(self):
        return self.app.general.el_is_displayed(self.projects_section)

    def main_section_9_is_presented(self):
        return self.app.general.el_is_displayed(self.faq_section)

    def main_section_10_is_presented(self):
        els = self.app.general.find_elS_and_return(self.subscription_cta_sections)
        return self.app.general.element_is_displayed_by_element(els[1])

    def sec1_title_top_is_presented(self):
        return self.app.general.el_is_displayed(self.sec1_title)

    def sec1_title_2nd_is_presented(self):
        return self.app.general.el_is_displayed(self.sec1_text)

    def sec1_switcher_is_presented(self):
        return self.app.general.el_is_displayed(self.sec1_switcher)

    def sec1_icon_name_is_presented(self):
        return len(self.app.general.find_elS_and_return(self.sec1_icons)) == 4

    def sec1_prices_is_presented(self):
        return len(self.app.general.find_elS_and_return(self.sec1_prices)) == 3


    def sec1_bonuses_list_is_presented(self):
        return len(self.app.general.find_elS_and_return
                   (self.sec1_benefits)) == 4


    def sec1_button_try_is_presented(self):
        return len(self.app.general.find_elS_and_return
                   (self.sec1_try_button)) == 4


    def switcher_default_state_is_annual(self):

        el = self.app.general.find_el_and_return(self.sec1_switcher_active)
        return 'Annual' in el.text


    def sec2_all_elements_texts(self):

        elements = self.app.general.find_elS_and_return(self.sec2_categories_titles)
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
        return self.app.general.el_is_displayed(self.sec4_icon)

    def sec4_top_title_is_presented(self):
        return self.app.general.el_is_displayed(self.sec4_title)

    def sec4_lower_title_is_presented(self):
        return self.app.general.el_is_displayed(self.sec4_text)

    def sec5_icons_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elS_and_return(self.sec5_icons)]
        if all(elements_disp) and len(elements_disp) == 3:
            return True
    def sec5_top_titles_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elS_and_return(self.sec5_titles)]
        if all(elements_disp) and len(elements_disp) == 3:
            return True


    def sec5_lower_titles_is_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elS_and_return(self.sec5_titles_lower)]
        if all(elements_disp) and len(elements_disp) == 3:
            return True

    def sec6and10_titles_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elS_and_return(self.sec6_10_titles)]
        if all(elements_disp) and len(elements_disp) == 2:
            return True

    def sec6and10_buttons_are_presented(self):
        elements_disp = [self.app.general.element_is_displayed_by_element(x)
                         for x in self.app.general.find_elS_and_return(self.sec6_10_buttons)]
        res = [x for x in elements_disp if not x]
        if res and len(elements_disp) == 2:
            return False
        return True

    def sec7_titles_are_presented(self):
        return self.app.general.el_is_displayed(self.sec7_title)

    def sec7_reviews_are_presented(self):
        elements = self.app.general.find_elS_and_return(self.sec7_items)
        el_dict = {}
        el_dict['quotes'] = [self.app.general.el_is_displayed(self.sec7_item_icons) for x in elements]
        el_dict['text'] = [self.app.general.el_is_displayed(self.sec7_item_text) for x in elements]
        el_dict['photo'] = [self.app.general.el_is_displayed(self.sec7_item_user_avatar) for x in elements]
        el_dict['name'] = [self.app.general.el_is_displayed(self.sec7_item_user_name) for x in elements]
        el_dict['position'] = [self.app.general.el_is_displayed(self.sec7_item_user_position) for x in elements]

        #el_dict['position'][0] = 'False'
        keys = el_dict.keys()
        for k in keys:
            for x in el_dict[k]:
                if x is not True:
                    return False

        return True

    def sec8_titles_are_presented(self):
        return self.app.general.el_is_displayed(self.sec8_title)


    def sec8_projects_are_presented(self):
        return self.app.general.el_is_displayed(self.sec8_list)

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
        return self.app.general.el_is_displayed(self.sec9_title)


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
        return self.app.general.el_is_displayed(self.expended_faq)


from time import sleep
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class ProjectRequestHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.request_project_button_css = 'button._31VgI'
        self.main_menu_section_css = "nav._3iCnJ"
        self.filters_section_css = "div._23IZv"
        self.requests_list_section_css = "div._305lF"
        self.instruction_section_css = "div._31Uzu"
        self.pagination_section_css = "div.NV12W"
        self.main_cat_filters_css = "ul._30W_k"
        self.subcategory_filter_css = "div.css-1rtrksz"
        self.popularity_latest_sorting = "div.css-va7pk8"
        self.difficulty_filter_css = 'div.css-1492t68'
        self.language_filter_css = 'div.css-1rtrksz'
        self.main_cat_buttonS_css = 'button._1owzv'
        self.main_cat_buttonS_xpath = '//button[@class="_1owzv"]'
        self.main_cat_iconS_xpath = "//button[@class='_1owzv']/*"
        self.main_cat_icons_css = "button[class='_1owzv'] svg"
        self.request_iconS_xpath = "//p[@class='_2CRit _2gT0V']/*"
        self.request_iconS_css = "p[class='_2CRit _2gT0V'] svg"
        self.button_next_css = 'a._1fZI7'
        self.filter_all_css = 'div.css-1oxma2j'
        self.project_request_css = 'li.PHJ5f'
        self.buttons_in_filter_css = 'div.css-1ep9fjw'
        self.button_all_main_cat = 'button._1owzv'
        self.sub_cat_filter = 'div._1QGiN'




    def screen_project_requests_is_presented(self):
        return self.app.general.element_is_presented(By.CSS_SELECTOR, self.request_project_button_css)

    def main_menu_section_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.main_menu_section_css)

    def filters_section_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.filters_section_css)

    def requests_list_section_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.requests_list_section_css)

    def instruction_section_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.instruction_section_css)

    def pagination_section_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.pagination_section_css)


    def main_cat_filters_is_presented(self, main_cat_filters):

        filters = self.app.general.find_element_and_return(By.CSS_SELECTOR, self.main_cat_filters_css)
        if self.app.general.element_is_displayed_by_element(filters):
            all_filters = self.app.general.find_elements_in_element(filters, By.CSS_SELECTOR, self.main_cat_buttonS_css)

            buttons_text = [self.app.general.get_text_of_element_by_element(x)
                            for x in self.app.general.find_elements_in_element(filters, By.CSS_SELECTOR, self.main_cat_buttonS_css)]

                            # for x in filters.find_elements_by_css_selector(self.main_cat_buttonS_css)]
            for text in buttons_text:
                if text in main_cat_filters:
                    main_cat_filters.remove(text)
            if len(main_cat_filters) == 0:
                return True
        else:
            return False


    def subcategory_filters_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.subcategory_filter_css)

    def popularity_latest_sorting_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.popularity_latest_sorting)

    def difficulty_filter_section_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.difficulty_filter_css)

    def language_filter_is_presented(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.language_filter_css)

    def list_of_requests_related_to_each_selected_category(self):
        ic_but_list = self.get_button_plus_icon_data_id()
        for category in ic_but_list:
            category['button'].click()
            sleep(1)
            requests_icons_id = \
                [x.get_attribute("data-id") for x in self.app.general.find_elementS_and_return(
                    By.CSS_SELECTOR, self.request_iconS_css)]
            page_no = self.get_no_pages()
            for page in range(1, page_no):

                for x in requests_icons_id:
                    if x != category['icon_dataid']:
                        return False
                self.button_next_click()
                sleep(0.5)

        return True




    def get_button_plus_icon_data_id(self):
        list_of_cat_buttons = self.app.general.find_elementS_and_return(By.XPATH, self.main_cat_buttonS_xpath)

        list_of_cat_icons = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, self.main_cat_icons_css)
        ic_but_list = []
        for x in range(0, len(list_of_cat_buttons)):
            ic_but_list.append({
                'button': list_of_cat_buttons[x],
                'icon_dataid':list_of_cat_icons[x].get_attribute("data-id")})

        return ic_but_list

    def button_next_click(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.button_next_css)

    def get_no_pages(self):
        if len(self.app.general.find_elementS_and_return(By.CSS_SELECTOR, self.button_next_css)) == 0:
            return 1
        else:
            last_page_el = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, 'a.rcIUX')[-1]
            value = int(last_page_el.text)
        return value

    def get_list_of_sub_cat(self):
        response = self.app.api.general_get(app=self.app, route=self.app.route.categories)

        sub_cat = [{'name' :x['name'], 'slug': x['slug']} for x in response['results']]
        return sub_cat

    def get_list_of_topics(self):
        response = self.app.api.general_get(app=self.app, route=self.app.route.topics)

        sub_cat = [{'name' :x['name'], 'slug': x['slug']} for x in response['results']]
        return sub_cat
#TODO#continue
    def requests_are_related_to_sub_categories(self, dict_of_subcategories):
        dict_of_subcategories = [random.choice(dict_of_subcategories) for x in range(10)]

        for sb in dict_of_subcategories:

            symbol = ""
            if sb['name'] in ['Java', 'C', '.NET', 'C++', 'C#', 'R', 'Go', 'D', 'CSS', 'Android']:
                continue
               # symbol = " "
            if sb['name'] in ["C++", 'C']:
                continue

            self.subcategory_enter_value_and_tap_enter(sb, symbol)
            page_no = self.get_no_pages()
            for page in range(0, page_no):
                els = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, self.project_request_css)
                if len(els) == 0:
                    continue
                requests_atr = [x.get_attribute('data-category') for x in els]
                for atr in requests_atr:
                    if atr != sb['slug']:
                        print(atr)
                        print(sb['slug'])
                        return False
                if page != page_no-1:
                    self.button_next_click()
                    sleep(1)
        return True

    def subcategory_enter_value_and_tap_enter(self, sb, symbol):

        self.app.general.button_press(By.CSS_SELECTOR, "div._1QGiN")
        el = self.app.general.find_elementS_and_return(By.XPATH, "//input")
        self.app.general.send_key_by_element(el[1], sb['name'] + symbol)
        self.app.general.send_key_by_element(el[1], u'\ue007')

        sleep(1)

    def select_main_category(self, main_cat):
        buttons = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, self.main_cat_buttonS_css)
        but = [x for x in buttons if x.text == main_cat]
        self.app.general.button_press_element(but[0])


    def all_requests_related_to_sub_and_main_cat(self, main_cat, sub_cat):
        all_sub_cat = self.get_list_of_sub_cat()
        all_main_cat = self.get_list_of_topics()
        slug_sub_cat = [x['slug'] for x in all_sub_cat if x['name'] == sub_cat]
        slug_main_cat = [x['slug'] for x in all_main_cat if x['name'] == main_cat]
        self.select_main_category(main_cat)
        self.subcategory_enter_value_and_tap_enter({'name':sub_cat}, "")
        page_no = self.get_no_pages()
        for page in range(0, page_no):
            els = self.app.general.find_elementS_and_return(By.CSS_SELECTOR, self.project_request_css)
            if len(els) == 0:
                continue
            requests_atr = [{'sub_category': x.get_attribute('data-category'),
                             'category': x.get_attribute('data-topic')} for x in els]
            for atr in requests_atr:
                if atr['sub_category'] != slug_sub_cat[0] or atr['category'] != slug_main_cat[0]:
                    return False
            if page != page_no - 1:
                self.button_next_click()
                sleep(1)
        return True
    # TODO
    def close_x_button_is_presented(self, field):
        subcat_filter = self.app.general.find_element_and_return(By.CSS_SELECTOR, self.sub_cat_filter)
        self.app.general.button_press(By.CSS_SELECTOR, "div._31Uzu")
        buttons = self.app.general.find_elements_in_element(subcat_filter, By.CSS_SELECTOR, field)
        if len(buttons)!=2:
            return False
        else:
            return True

    def select_and_enter_random_subcategory(self):
        subcat = random.choice(self.get_list_of_sub_cat())
        self.subcategory_enter_value_and_tap_enter(subcat, "")


    def button_all_is_selected(self):
        self.app.general.element_is_presented(By.CSS_SELECTOR, "button[class='_1owzv _1bHrQ']")

    def get_filter_by_text(self, text):
        element = self.app.general.get_element_by_text(text, By.CSS_SELECTOR, self.filter_all_css)
        return element

    def close_x_button_click(self, filter):
        self.app.general.button_press(By.CSS_SELECTOR, 'div.zmR57')
        button = self.app.general.find_elements_in_element(
            filter, By.CSS_SELECTOR, self.buttons_in_filter_css)[0]

        self.app.general.button_press_element(button)







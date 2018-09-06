from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



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
        self.request_iconS_xpath = "//p[@class='_2CRit _2gT0V']/*"
        self.button_next_css = 'a._1fZI7'
        self.filter_all_css = 'div.css-1rtrksz'





    def screen_project_requests_is_presented(self):
        elements = self.driver.find_elements_by_css_selector(self.request_project_button_css)

        if len(elements) > 0:
            if elements[0].text == 'Request a Project':
                return True

        else:
            return False

    def main_menu_section_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.main_menu_section_css))

    def filters_section_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.filters_section_css))
    def requests_list_section_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.requests_list_section_css))

    def instruction_section_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.instruction_section_css))

    def pagination_section_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.pagination_section_css))

    def main_cat_filters_is_presented(self, main_cat_filters):
        filters = self.driver.find_element_by_css_selector(self.main_cat_filters_css)
        if self.app.general.element_is_displayed(filters):
            buttons_text = [x.text for x in filters.find_elements_by_css_selector(self.main_cat_buttonS_css)]
            for text in buttons_text:
                if text in main_cat_filters:
                    main_cat_filters.remove(text)
            if len(main_cat_filters) == 0:
                return True
        else:
            return False


    def subcategory_filters_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.subcategory_filter_css))

    def popularity_latest_sorting_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.popularity_latest_sorting))

    def difficulty_filter_section_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.difficulty_filter_css))

    def language_filter_is_presented(self):
        return self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                     (self.language_filter_css))

    def list_of_requests_related_to_each_selected_category(self):
        ic_but_list = self.get_button_plus_icon_data_id()
        for category in ic_but_list:
            category['button'].click()
            sleep(1)
            requests_icons_id = \
                [x.get_attribute("data-id") for x in self.driver.find_elements_by_xpath(self.request_iconS_xpath)]
            page_no = self.get_no_pages()
            for page in range(1, page_no):

                for x in requests_icons_id:
                    if x != category['icon_dataid']:
                        return False
                self.button_next_click()
                sleep(0.5)

        return True




    def get_button_plus_icon_data_id(self):
        list_of_cat_buttons = self.driver.find_elements_by_xpath(self.main_cat_buttonS_xpath)
        list_of_cat_icons = self.driver.find_elements_by_xpath(self.main_cat_iconS_xpath)
        ic_but_list = []
        for x in range(0, len(list_of_cat_buttons)):
            ic_but_list.append({
                'button': list_of_cat_buttons[x],
                'icon_dataid':list_of_cat_icons[x].get_attribute("data-id")})

        return ic_but_list

    def button_next_click(self):
        self.driver.find_element_by_css_selector(self.button_next_css).click()

    def get_no_pages(self):
        if len(self.driver.find_elements_by_css_selector(self.button_next_css)) == 0:
            return 1
        else:
            last_page_el = self.driver.find_elements_by_css_selector('a.rcIUX')[-1]
            value = int(last_page_el.text)
        return value

    def get_list_of_sub_cat(self):
        response = self.app.api.general_get(app=self.app, route=self.app.route.categories)

        sub_cat = [x['name'] for x in response['results']]
        return sub_cat

    def requests_are_related_to_sub_categories(self, list_of_subcategories):
        filter = self.driver.find_element_by_css_selector("div._1QGiN")
        for sb in list_of_subcategories:
            filter.click()
            self.driver.find_elements_by_xpath("//input")[1].send_keys(sb)
            self.driver.find_elements_by_xpath("//input")[1].send_keys(u'\ue007')
            sleep(0.5)





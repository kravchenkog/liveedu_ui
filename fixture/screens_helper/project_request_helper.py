from time import sleep
import random
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common import keys



class ProjectRequestHelper():


    def __init__(self, app):
        self.app = app
        self.general = self.app.general
        self.file_pr1 = 'modal-triger'
        self.file_pr2 = 'category-filter'
        self.file_pr3 = 'requests-list'
        self.file_pr4 = 'directory-paginator'
        self.file_pr5 = 'topics-filter'
        self.file_pr6 = 'sort-filter'
        self.file_pr7 = 'requests-cta'
        self.file_pr8 = 'site-navigation'
        self.file_pr9 = 'directory-filter'
        self.file_pr10 = 'project-requests'
        self.file_pr11 = 'requests-card'
        self.file_pr12 = 'modal-content'
        self.file_pr13 = 'requests-form'
        self.file_pr14 = "site-header"


        self.request_project_button = {
            By.CSS_SELECTOR: 'button[class^="{}__modal-button"]'.format(self.file_pr1)}
        self.sub_cat_filter = {
            By.CSS_SELECTOR: 'div[class^="{}__categories"]'.format(self.file_pr2)}
        self.project_request = {
            By.CSS_SELECTOR: "li[class^='{}__item']".format(self.file_pr3)}
        self.input_fields = {
            By.CSS_SELECTOR: "input", By.XPATH: "//input"}
        self.button_next = {
            By.CSS_SELECTOR: 'a[class^="{}__next"]'.format(self.file_pr4)}
        self.buttons_main_filters = {
            By.CSS_SELECTOR: 'button[class^="{}__button"]'.format(self.file_pr5)}
        self.main_cat_filters = {
            By.CSS_SELECTOR: 'ul[class^="{}__topics"]'.format(self.file_pr5)}
        self.three_right_filters_alternative = {
            By.CSS_SELECTOR: "div[class^='css-10nd86i {}__select']".format(self.file_pr6)}
        self.three_right_filters_alternative2 = {
            By.CSS_SELECTOR: "div[class^='{}__sort']".format(self.file_pr6)}
        self.three_right_filters = {
            By.CSS_SELECTOR: "div[class='{}__select']".format(self.file_pr6)}
        self.instruction_section = {
            By.CSS_SELECTOR: "div[class^={}__illustration]".format(self.file_pr7)}
        self.main_menu_section = {
            By.CSS_SELECTOR: "nav[class^='{}__navigation']".format(self.file_pr8)}
        self.filters_section = {
            By.CSS_SELECTOR: "div[class^='{}__container']".format(self.file_pr9)}
        self.requests_list_section = {
            By.CSS_SELECTOR: "div[class^='{}__content']".format(self.file_pr10)}
        self.like_section = {
            By.CSS_SELECTOR: "div[class^='{}__votes']".format(self.file_pr11)}
        self.project_request_titles = {
            By.CSS_SELECTOR: "p[class^='{}__title']".format(self.file_pr11)}
        self.likes_counter = {
            By.CSS_SELECTOR: "div[class^='{}__votes']".format(self.file_pr11)}
        self.likes_button = {
            By.CSS_SELECTOR: 'button[class^="{}__votes-button"]'.format(self.file_pr11)}
        self.pr_popup = {
            By.CSS_SELECTOR: "div[class^='{}__modal']".format(self.file_pr12)}
        self.close_popup_button = {
            By.CSS_SELECTOR: "button[class^='{}__modal-close']".format(self.file_pr12)}
        self.pr_popup_main_title = {
            By.CSS_SELECTOR: "div[class^='{}__modal-title']".format(self.file_pr12)}
        self.pr_popup_pname = {
            By.CSS_SELECTOR: "input[class^='{}__form-input']".format(self.file_pr13)}
        self.pr_popup_subcategory = {
            By.CSS_SELECTOR: "div[class^='css-1sontr1']"}
        self.pr_popup_description = {
            By.CSS_SELECTOR: "textarea[name='description']"}
        self.pr_popup_cat_dif_lang = {
            By.CSS_SELECTOR: "div[class*='requests-form__select']"}
        self.pr_popup_submit_button = {
            By.CSS_SELECTOR: "button[class^='{}__form-button']".format(self.file_pr13)}
        self.create_this_project =  {
            By.CSS_SELECTOR: 'button[class^="{}__create-button"]'.format(self.file_pr11)}
        self.main_title = {
            By.CSS_SELECTOR: 'h2[class^="{}__title"]'.format(self.file_pr14)}
        self.last_page_no = {
            By.CSS_SELECTOR: 'a[class^="{}__link"]'.format(self.file_pr4)}






        self.pagination_section = {By.CSS_SELECTOR: "div.NV12W"}

        self.subcategory_filter = {By.CSS_SELECTOR: "div.css-1rtrksz"}
        self.popularity_latest_sorting = {By.CSS_SELECTOR: "div._3octD"}
        self.difficulty_filter = {By.CSS_SELECTOR: 'div.css-1492t68'}
        self.language_filter = {By.CSS_SELECTOR: 'div.css-1rtrksz'}
        self.main_cat_buttonS = {By.CSS_SELECTOR: 'button._1owzv',
                                 By.XPATH: '//button[@class="_1owzv"]'}
        self.main_cat_iconS = {By.CSS_SELECTOR: "button[class='_1owzv'] svg",
                               By.XPATH: "//button[@class='_1owzv']/*"}
        self.request_iconS = {By.CSS_SELECTOR: "p[class='_2CRit _2gT0V'] svg",
                              By.XPATH: "//p[@class='_2CRit _2gT0V']/*"}

        self.filter_all = {By.CSS_SELECTOR: 'div.css-1oxma2j'}

        self.buttons_in_filter = {By.CSS_SELECTOR: 'div.css-1ep9fjw'}



        self.choose_a_category = {By.CSS_SELECTOR: 'div.css-1ep9fjw'}





        self.button_all_selected = {By.CSS_SELECTOR: "button[class='_1owzv _1bHrQ']"}



        self.date_of_proj_request = {By.CSS_SELECTOR: 'p._1kv2c'}

        self.difficulty_text = {By.CSS_SELECTOR: "div.css-va7pk8"}

        self.description_of_pr = {By.CSS_SELECTOR: "p._3B9_Q"}
        self.language_title = {By.CSS_SELECTOR: "p[class='_1A-k7 _2gT0V']"}
        self.subcategory_icon = {By.CSS_SELECTOR: "p[class='_23KRX _2gT0V']"}
        self.creator_name = {By.CSS_SELECTOR: "span._2-jmN"}


        self.make_section_icon = {By.CSS_SELECTOR: 'div._3octD'}
        self.make_section_title = {By.CSS_SELECTOR: 'p._2QuCm'}
        self.make_section_text = {By.CSS_SELECTOR: "p._9YIIf"}



        self.pr_popup_main_cat_input ={By.CSS_SELECTOR: "input"}
        self.pr_popup_drodowns = {By.CSS_SELECTOR: 'div.css-1oxma2j'}
        self.pr_popup_drodowns2 = {By.CSS_SELECTOR: 'div.css-1rtrksz'}





    def screen_project_requests_is_displayed(self):
        return self.general.el_is_presented(self.request_project_button)

    def main_menu_section_is_displayed(self):
        return self.general.el_is_displayed(self.main_menu_section)

    def filters_section_is_displayed(self):
        return self.general.el_is_displayed(self.filters_section)

    def requests_list_section_is_displayed(self):
        return self.general.el_is_displayed(self.requests_list_section)

    def instruction_section_is_presented(self):
        return self.general.el_is_displayed(self.instruction_section)

    def pagination_section_is_presented(self):
        return self.general.el_is_displayed(self.pagination_section)


    def main_cat_filters_is_presented(self, main_cat_filters):

        filters = self.general.find_el_and_return(self.main_cat_filters)
        if self.general.element_is_displayed_by_element(filters):
            all_filters = self.general.find_elS_in_element(filters, self.main_cat_buttonS)

            buttons_text = [self.general.get_text_of_element_by_element(x)
                            for x in self.general.find_elS_in_element(filters, self.buttons_main_filters)]

                            # for x in filters.find_elements_by_css_selector(self.main_cat_buttonS_css)]
            for text in buttons_text:
                if text in main_cat_filters:
                    main_cat_filters.remove(text)
            if len(main_cat_filters) == 0:
                return True
        else:
            return False

    def sort_filter_is_presented(self, filter_name):
        return self.general.element_is_displayed_by_element(
            self.general.get_el_by_text(text=filter_name, element=self.three_right_filters_alternative))

    def subcategory_filters_is_presented(self):
        return self.general.el_is_displayed(self.subcategory_filter)

    # def popularity_latest_sorting_is_presented(self):
    #     return self.general.el_is_displayed(self.popularity_latest_sorting)
    #
    # def difficulty_filter_section_is_presented(self):
    #     return self.general.el_is_displayed(self.difficulty_filter)
    #
    # def language_filter_is_presented(self):
    #     return self.general.el_is_displayed(self.language_filter)

    def list_of_requests_related_to_each_selected_category(self):
        ic_but_list = self.get_button_plus_icon_data_id()
        for category in ic_but_list:
            category['button'].click()
            sleep(1)
            requests_icons_id = \
                [x.get_attribute("data-id") for x in self.general.find_elS_and_return(self.request_iconS)]
            page_no = self.get_no_pages()
            for page in range(1, page_no):

                for x in requests_icons_id:
                    if x != category['icon_dataid']:
                        return False
                sleep(0.5)
                self.button_next_click()
                sleep(0.5)

        return True




    def get_button_plus_icon_data_id(self):
        list_of_cat_buttons = self.general.find_elS_and_return(self.main_cat_buttonS, 1)

        list_of_cat_icons = self.general.find_elS_and_return(self.main_cat_iconS)
        ic_but_list = []
        for x in range(0, len(list_of_cat_buttons)):
            ic_but_list.append({
                'button': list_of_cat_buttons[x],
                'icon_dataid':list_of_cat_icons[x].get_attribute("data-id")})

        return ic_but_list

    def button_next_click(self):
        self.general.wait_presence_of_el(self.button_next, 5)
        self.general.but_press(self.button_next)

    def get_no_pages(self):
        if len(self.general.find_elS_and_return(self.button_next)) == 0:
            return 1
        else:
            last_page_el = self.general.find_elS_and_return(self.last_page_no)[-1]
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

    def requests_are_related_to_sub_categories(self, dict_of_subcategories):
        dict_of_subcategories = [random.choice(dict_of_subcategories) for x in range(10)]

        for sb in dict_of_subcategories:

            symbol = ""
            if sb['name'] in ['Java', 'C', '.NET', 'C++', 'C#', 'R', 'Go', 'D', 'CSS', 'Android']:
                continue
               # symbol = " "
            if sb['name'] in ["C++", 'C']:
                continue
            main_el = self.general.find_el_and_return(self.sub_cat_filter)
            input = self.get_input_field_by_main_element(main_el, 0)
            self.enter_value_to_filter_and_tap_enter(main_el, sb['name'], input)
            sleep(1)
            page_no = self.get_no_pages()
            for page in range(0, page_no):
                els = self.general.find_elS_and_return(self.project_request)
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


    def select_main_category(self, main_cat):
        buttons = self.general.find_elS_and_return(self.buttons_main_filters)
        but = [x for x in buttons if x.text == main_cat]
        self.general.button_press_element(but[0])


    def all_requests_related_to_sub_and_main_cat(self, main_cat, sub_cat):
        all_sub_cat = self.get_list_of_sub_cat()
        all_main_cat = self.get_list_of_topics()
        slug_sub_cat = [x['slug'] for x in all_sub_cat if x['name'] == sub_cat]
        slug_main_cat = [x['slug'] for x in all_main_cat if x['name'] == main_cat]
        self.select_main_category(main_cat)

        main_el = self.general.find_el_and_return(self.sub_cat_filter)
        input_field = self.get_input_field_by_main_element(main_el, 0)
        self.enter_value_to_filter_and_tap_enter(main_el, sub_cat, input_field)

        page_no = self.get_no_pages()
        for page in range(0, page_no):
            sleep(1)
            els = self.general.find_elS_and_return(self.project_request)
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

    def close_x_button_is_presented(self, field, main_el=None):
        if main_el == None:
            main_filter = self.general.find_el_and_return(self.sub_cat_filter)
        else:
            main_filter = main_el
        self.general.but_press(self.instruction_section)
        buttons = self.general.find_elS_in_element(main_filter, field)
        if len(buttons)!=2:
            return False
        else:
            return True

    def select_and_enter_random_subcategory(self):
        subcat = random.choice(self.get_list_of_sub_cat())['name']
        main_el = self.general.find_el_and_return(self.sub_cat_filter)
        input_field = self.get_input_field_by_main_element(main_el, 0)
        self.enter_value_to_filter_and_tap_enter(main_el, subcat, input_field)



    def button_all_is_selected(self):
        self.general.el_is_presented(self.button_all_selected)

    def get_filter_by_text(self, text):
        element = self.general.get_el_by_text(text, self.filter_all)
        return element

    def close_x_button_click(self, filter, button_press, el=0):
        if el==0:
            self.general.but_press(button_press)
        if el==1:

            self.general.but_press(self.instruction_section)
        self.general.but_press(self.instruction_section)
        button = self.general.find_elS_in_element(
            filter, self.buttons_in_filter)

        self.general.button_press_element(button[0])

    def select_value_in_right_filters(self, f_no, text):
        main_el = self.general.find_el_and_return(self.three_right_filters_alternative2)
        input = self.get_input_field_by_main_element(main_el, f_no)
        filter_to_press = self.get_filter_to_press(f_no)  #0=Popular/New 1=Difficulty 2=Language
        self.enter_value_to_filter_and_tap_enter(filter_to_press, text, input)
        return filter_to_press

    def get_input_field_by_main_element(self, main_element, f_no):
        inputs = self.general.find_elS_in_element(main_element, self.input_fields)
        return inputs[f_no]

    def get_filter_to_press(self, f_no):
        three_filters = self.general.find_elS_and_return(self.three_right_filters_alternative)
        return three_filters[f_no]


    def enter_value_to_filter_and_tap_enter(self, filtr, text, input, symbol=""):
        self.general.button_press_element(filtr)


        self.general.send_key_by_element(input, text + symbol)
        self.general.send_key_by_element(input, u'\ue007')

        sleep(1)

    def list_of_requests_sorted_by_popularity(self):
        list_of_el = self.general.find_elS_and_return(self.like_section)
        texts = self.general.get_list_of_texts_in_elements(list_of_el)
        int_texts = [int(x) for x in texts]
        for t in range(0, len(int_texts)-1):
            if int_texts[t] < int_texts[t+1]:
                return False

        return True

    def list_of_requests_sorted_by_latest(self):
        list_of_el = self.general.find_elS_and_return(self.date_of_proj_request)
        texts = self.general.get_list_of_texts_in_elements(list_of_el)
        dates = []
        for t in texts:
            dates.append(datetime.strptime(t, '%d %B %Y'))
        for d in range(0, len(dates)-1):
            if dates[d] < dates[d-1]:
                return False
        return True

    def get_list_of_requests_by_api(self, difficulty=None, language=None):
        self.clear_parans()
        if difficulty:
            self.app.env.params['difficulty'] = difficulty
        if language:
            self.app.env.params['language'] = language
        self.app.env.params['ordering'] = '-num_vote_up'
        self.app.env.params['limit'] = 10
        resp = self.app.api.general_get(app=self.app, route=self.app.route.projects_suggestions)
        titles = [x['title'] for x in resp['results']]
        return titles
    def clear_parans(self):
        self.app.env.params = {}

    def list_of_pr_req_related_to_api_list(self, list_api):
        pr_list_ui = self.general.get_list_of_texts_in_elements(
            self.general.find_elS_and_return(self.project_request_titles))
        for el in range(0, len(list_api)):
            if list_api[el] != pr_list_ui[el]:
                return False
        return True

    def get_difficulty_filter(self):
        return self.get_filter_to_press(1)

    def get_language_filter(self):
        return self.get_filter_to_press(2)

    def pr_element_is_displayed_in_each(self, element):
        resuslt = [self.general.element_is_displayed_by_element(x)
                   for x in self.general.find_elS_and_return(element)]
        if all(resuslt):
            return True
        else:
            return False

    def get_counter_of_likes(self, element_no):
        counter_value = int(self.general.get_text_of_element_by_element(
            self.general.find_elS_and_return(self.likes_counter)[element_no]
        ))
        return counter_value
    def press_likes_button(self, element_no):
        el  = self.general.find_elS_and_return(self.likes_button)[element_no]
        self.general.button_press_element(el)

    def press_random_create_this_proj_button(self):
        el  = random.choice(self.general.find_elS_and_return(self.create_this_project))
        self.general.button_press_element(el)

    def get_random_pr_data(self):
        data = {'pr_name': self.app.string.get_random_email(),
                'category': self.app.api.get_random_name_topic(self.app),
                'subcategory': random.choice(self.get_list_of_sub_cat())['name'],
                'difficulty': random.choice(['Beginner', 'Intermediate', 'Expert']),
                'language': random.choice(['English', 'Russian']),
                'description': self.app.string.get_random_email()}
        return data

    def choose_value_on_popup(self, value, dropdown):
        el = self.general.get_el_by_text(element=self.pr_popup_drodowns2, text=dropdown)
        input_f = self.general.find_elS_in_element(main_el=el, element=self.pr_popup_main_cat_input)[0]
        self.enter_value_to_filter_and_tap_enter(el, value['category'], input_f)








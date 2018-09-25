from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class LiveScreenHelper():
    def __init__(self, app):
        self.app = app
        self.general = self.app.general

        self.file_live1 = "site-navigation"
        self.file_live2 = "site-header"
        self.file_live3 = "main-layout"
        self.file_live4 = 'site-header'
        self.file_live5 = 'nav-dropdown'
        self.file_live6 = "nav-link"

        self.navigation_sec = {By.CSS_SELECTOR: "nav[class^='{}__navigation']".format(self.file_live1)}
        self.header_sec = {By.CSS_SELECTOR: "header[class^='{}__header']".format(self.file_live2)}
        self.main_sec = {By.CSS_SELECTOR: "main[class^='{}__app']".format(self.file_live3)}
        self.logo = {By.CSS_SELECTOR: "a[class^='{}__logo']".format(self.file_live1)}
        self.header_title = {By.CSS_SELECTOR: "h2[class^='{}__title']".format(self.file_live4)}
        self.button_more = {By.CSS_SELECTOR: "button[class^='{}__button']".format(self.file_live5)}
        self.nav_buttons = {By.CSS_SELECTOR: "a[class^='{}__link']".format(self.file_live6)}
        self.button_more_items = {By.CSS_SELECTOR: "a[class^='{}__link']".format(self.file_live5)}


    def screen_live_is_presented(self):
        return self.app.general.screen_is_presented_by_url("https://dev.liveedu.tv/live")

    def section_navigation_is_displayed(self):
        return self.general.el_is_displayed(self.navigation_sec)

    def section_header_is_displayed(self):
        return self.general.el_is_displayed(self.header_sec)

    def section_main_is_displayed(self):
        return self.app.general.el_is_displayed(self.main_sec)

    def navigation_button_is_displayed(self, button_text):
        buttons = self.app.general.find_elS_and_return(self.nav_buttons)
        buttons.append(self.app.general.find_el_and_return(self.button_more))
        texts = self.app.general.get_list_of_texts_in_elements(buttons)

        for text in texts:
            if button_text in text:
                return True
        return False

    def navigation_button_press(self, button_text):
        buttons = self.app.general.find_elS_and_return(self.nav_buttons)
        buttons.append(self.app.general.find_el_and_return(self.button_more))
        texts = self.app.general.get_list_of_texts_in_elements(buttons)

        counter = 0
        for text in texts:

            if button_text in text:
                self.app.general.button_press_element(buttons[counter])
                continue

            else:
                counter+=1

    def navigation_button_logo_is_displayed(self):
        return self.app.general.el_is_displayed(self.logo)


    def navigation_button_logo_press(self):
        self.general.but_press(self.logo)
        sleep(1)


    def navigation_button_more_press(self):
        self.app.general.but_press(self.button_more)
        sleep(1)

    def screen_live_navigation_is_selected_button(self, title):
        buttons = self.app.general.find_elS_and_return(self.nav_buttons)
        buttons.append(self.app.general.find_el_and_return(self.button_more))


        for but in buttons:
            a = but.value_of_css_property("background-color")
            if a == 'rgb(251, 251, 251)':
                if title in but.text:
                    return True
                else:
                    return False
            return False


    def navigation_screen_is_changed_to(self, title):
        text = self.app.general.get_txt_of_el(self.header_title)
        if title.lower() in text.lower():
            return True
        else:
            return False

    def navigation_more_sub_elements_are_presented(self, butons):
        buttons_titles = [x.text for x in self.app.general.find_elS_and_return(self.button_more_items)]
        for b in buttons_titles:
            if b not in butons:
                return False
        if len(buttons_titles) == len(butons):
            return True






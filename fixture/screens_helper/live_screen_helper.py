from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class LiveScreenHelper():
    def __init__(self, app):
        self.app = app
        self.navigation_sec_css = 'nav._3iCnJ'
        self.header_sec_css = 'header._28RNe'
        self.main_sec_css = 'main._2pzbf'
        self.but_live_now_xpath = "//ul[@class='_4CGHb _2k_rN']//li[1]/a"
        self.but_logo_css = 'a.P80aM'
        self.but_projects_xpath = "//ul[@class='_4CGHb _2k_rN']//li[2]/a"
        self.but_guides_xpath = "//ul[@class='_4CGHb _2k_rN']//li[3]/a"
        self.but_schedule_xpath = "//ul[@class='_4CGHb _2k_rN']//li[4]/a"
        self.but_requests_xpath = "//ul[@class='_4CGHb _2k_rN']//li[5]/a"
        self.but_subscribe_xpath = "//ul[@class='_4CGHb _3zRnY']//li[1]/a"
        self.but_more_xpath = "//ul[@class='_4CGHb _3zRnY']//li[2]"
        self.main_title_h2_css = 'h2._2odmM'
        self.buttons_more_css = "li[class='i_Fzp']"

    def screen_live_is_presented(self):
        return self.app.general.screen_is_presented_by_url("https://dev.liveedu.tv/live")

    def section_navigation_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.navigation_sec_css)

    def section_header_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.header_sec_css)

    def section_main_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.main_sec_css)

    def navigation_button_logo_is_displayed(self):
        return self.app.general.element_is_displayed(By.CSS_SELECTOR, self.but_logo_css)

    def navigation_button_live_now_is_presented(self, should):
        text = self.app.general.get_text_of_element(By.XPATH, self.but_live_now_xpath)
        return should in text

    def navigation_button_projects_is_presented(self, should):
        text = self.app.general.get_text_of_element(By.XPATH, self.but_projects_xpath)
        return should in text

    def navigation_button_guides_is_presented(self, should):
        text = self.app.general.get_text_of_element(By.XPATH, self.but_guides_xpath)
        return should in text

    def navigation_button_schedule_is_presented(self, should):
        text = self.app.general.get_text_of_element(By.XPATH, self.but_schedule_xpath)
        return should in text

    def navigation_button_requests_is_presented(self, should):
        text = self.app.general.get_text_of_element(By.XPATH, self.but_requests_xpath)
        return should in text

    def navigation_button_subscribe_is_presented(self, should):
        text = self.app.general.get_text_of_element(By.XPATH, self.but_subscribe_xpath)
        return should in text

    def navigation_button_more_is_presented(self, should):
        text = self.app.general.get_text_of_element(By.XPATH, self.but_more_xpath)
        return should in text

    def navigation_button_logo_press(self):
        self.app.general.button_press(By.CSS_SELECTOR, self.but_logo_css)
        sleep(1)

    def navigation_button_livenow_press(self):

        self.app.general.button_press(By.XPATH, self.but_live_now_xpath)
        sleep(1)

    def navigation_button_projects_press(self):

        self.app.general.button_press(By.XPATH, self.but_projects_xpath)
        sleep(1)

    def navigation_button_guides_press(self):
        self.app.general.button_press(By.XPATH, self.but_guides_xpath)
        sleep(1)

    def navigation_button_schedule_press(self):
        self.app.general.button_press(By.XPATH, self.but_schedule_xpath)
        sleep(1)

    def navigation_button_requests_press(self):
        self.app.general.button_press(By.XPATH, self.but_requests_xpath)
        sleep(1)

    def navigation_button_subscribe_press(self):
        self.app.general.button_press(By.XPATH, self.but_subscribe_xpath)
        sleep(1)

    def navigation_button_more_press(self):
        self.app.general.button_press(By.XPATH, self.but_more_xpath)
        sleep(1)

    def screen_live_navigation_is_selected_button(self, title):
        list_of_buttons = [self.but_live_now_xpath, self.but_projects_xpath, self.but_guides_xpath,
                           self.but_schedule_xpath, self.but_requests_xpath]

        for x in range(0, len(list_of_buttons)-1):
            el = self.app.general.find_element_and_return(By.XPATH, list_of_buttons[x])
            text = el.text
            if title in text:
                a = el.value_of_css_property("background-color")
                if a == 'rgb(251, 251, 251)':
                    return True
                else:
                    return False

    def navigation_screen_is_changed_to(self, title):
        text = self.app.general.get_text_of_element(By.CSS_SELECTOR, self.main_title_h2_css)
        if title.lower() in text.lower():
            return True
        else:
            return False

    def navigation_more_sub_elements_are_presented(self, butons):
        buttons_titles = [x.text for x in self.app.general.find_elementS_and_return(By.CSS_SELECTOR, self.buttons_more_css)]
        for b in buttons_titles:
            if b not in butons:
                return False
        if len(buttons_titles) == len(butons):
            return True






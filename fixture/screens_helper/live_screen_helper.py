from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fixture.general_helper import GeneralHelper
from time import sleep


class LiveScreenHelper(GeneralHelper):
    navigation_sec_css = 'nav._3iCnJ'
    header_sec_css = 'header._28RNe'
    main_sec_css = 'main._2pzbf'
    but_live_now_xpath = "//ul[@class='_4CGHb _2k_rN']//li[1]/a"
    but_logo_css = 'a.P80aM'
    but_projects_xpath = "//ul[@class='_4CGHb _2k_rN']//li[2]/a"
    but_guides_xpath = "//ul[@class='_4CGHb _2k_rN']//li[3]/a"
    but_schedule_xpath = "//ul[@class='_4CGHb _2k_rN']//li[4]/a"
    but_requests_xpath = "//ul[@class='_4CGHb _2k_rN']//li[5]/a"
    but_subscribe_xpath = "//ul[@class='_4CGHb _3zRnY']//li[1]/a"
    but_more_xpath = "//ul[@class='_4CGHb _3zRnY']//li[2]"
    main_title_h2_css = 'h2._2odmM'
    buttons_more_css = "li[class='i_Fzp']"

    def screen_live_is_presented(self):
        return self.screen_is_presented_by_url("https://dev.liveedu.tv/live")

    def section_navigation_is_presented(self):
        return self.element_is_displayed(self.find_element_by(By.CSS_SELECTOR, self.navigation_sec_css))

    def section_header_is_presented(self):
        return self.element_is_displayed(self.find_element_by(By.CSS_SELECTOR, self.header_sec_css))

    def section_main_is_presented(self):
        return self.element_is_displayed(self.find_element_by(By.CSS_SELECTOR, self.main_sec_css))

    def navigation_button_logo_is_presented(self):
        return self.element_is_displayed(self.find_element_by(By.CSS_SELECTOR, self.but_logo_css))

    def navigation_button_live_now_is_presented(self, should):
        text = self.find_element_by(By.XPATH, self.but_live_now_xpath).text
        return should in text

    def navigation_button_projects_is_presented(self, should):
        text = self.find_element_by(By.XPATH, self.but_projects_xpath).text
        return should in text

    def navigation_button_guides_is_presented(self, should):
        text = self.find_element_by(By.XPATH, self.but_guides_xpath).text
        return should in text

    def navigation_button_schedule_is_presented(self, should):
        text = self.find_element_by(By.XPATH, self.but_schedule_xpath).text
        return should in text

    def navigation_button_requests_is_presented(self, should):
        text = self.find_element_by(By.XPATH, self.but_requests_xpath).text
        return should in text

    def navigation_button_subscribe_is_presented(self, should):
        text = self.find_element_by(By.XPATH, self.but_subscribe_xpath).text
        return should in text

    def navigation_button_more_is_presented(self, should):
        text = self.find_element_by(By.XPATH, self.but_more_xpath).text
        return should in text

    def navigation_button_logo_press(self):
        self.find_element_by(By.CSS_SELECTOR, self.but_logo_css).click()
        sleep(1)

    def navigation_button_livenow_press(self):
        self.find_element_by(By.XPATH, self.but_live_now_xpath).click()
        sleep(1)

    def navigation_button_projects_press(self):
        self.find_element_by(By.XPATH, self.but_projects_xpath).click()
        sleep(1)

    def navigation_button_guides_press(self):
        self.find_element_by(By.XPATH, self.but_guides_xpath).click()
        sleep(1)
    def navigation_button_schedule_press(self):
        self.find_element_by(By.XPATH, self.but_schedule_xpath).click()
        sleep(1)

    def navigation_button_requests_press(self):
        self.find_element_by(By.XPATH, self.but_requests_xpath).click()
        sleep(1)

    def navigation_button_subscribe_press(self):
        self.find_element_by(By.XPATH, self.but_subscribe_xpath).click()
        sleep(1)

    def navigation_button_more_press(self):
        self.find_element_by(By.XPATH, self.but_more_xpath).click()
        sleep(1)

    def screen_live_navigation_is_selected_button(self, title):
        list_of_buttons = [self.but_live_now_xpath, self.but_projects_xpath, self.but_guides_xpath,
                           self.but_schedule_xpath, self.but_requests_xpath]

        for x in range(0, len(list_of_buttons)-1):
            el = self.find_element_by(By.XPATH, list_of_buttons[x])
            text = el.text
            if title in text:
                a = el.value_of_css_property("background-color")
                if a == 'rgb(251, 251, 251)':
                    return True
                else:
                    return False

    def navigation_screen_is_changed_to(self, title):
        text = self.find_element_by(By.CSS_SELECTOR, self.main_title_h2_css).text
        if title.lower() in text.lower():
            return True
        else:
            return False

    def navigation_more_sub_elements_are_presented(self, butons):
        buttons_titles = [x.text for x in self.find_elements_by(By.CSS_SELECTOR, self.buttons_more_css)]
        for b in buttons_titles:
            if b not in butons:
                return False
        if len(buttons_titles) == len(butons):
            return True






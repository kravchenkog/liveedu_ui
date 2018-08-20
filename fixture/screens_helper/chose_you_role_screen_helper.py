from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class ChoseYourRoleHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def screen_choseyourrole_is_presented(self):
        elements = self.driver.find_elements_by_css_selector("button[class='_1Dk7f']")
        if len(elements) > 0:
            return True
        else:
            return False

    def title_top_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('h2.ygWV5'))

    def title_below_top_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('p._16y2Q'))

    def button_study_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('button._1Dk7f'))

    def button_create_project_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('button._1Dk7f'))

    def title_lower_is_presented(self):
        return self.app.general.element_is_displayed(
            self.app.driver.find_element_by_css_selector('p._16y2Q'))



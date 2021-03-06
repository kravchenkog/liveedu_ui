from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GeneralHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver


    def el_is_displayed(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        if el.is_displayed():
            return True
        else:
            return False

    def element_is_displayed_by_element(self, element):

        if element.is_displayed():
            return True
        else:
            return False

    def find_element_by(self, locator, value):
        return self.driver.find_element(locator, value)

    def find_elements_by(self, locator, value):
        return self.driver.find_elements(locator, value)

    def screen_is_presented_by_url(self, url):
        if self.driver.current_url == url:
            return True
        else:
            return False

    def logout_perform(self):
        if not self.app.login.user_menu_is_opened():
            self.driver.find_element_by_css_selector("button[class^='user-menu__button']").click()
        self.driver.find_element_by_css_selector("button[class^='user-menu__link']").click()
        sleep(0.5)

    def button_press(self, locator, button):
        self.driver.find_element(locator, button).click()

    def but_press(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        self.driver.find_element(locator_type, locator_value).click()

    def button_press_element(self, button):
        button.click()

    def element_is_presented(self, locator, element):
        el = self.driver.find_elements(locator, element)
        if len(el) > 0:
            return True
        else:
            return False

    def el_is_presented(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_elements(locator_type, locator_value)
        if el:
            return True
        return False

    def get_element_by_text(self, text, loc_type, elements):
        els = self.driver.find_elements(loc_type, elements)
        el = [x for x in els if x.text == text][0]
        return el

    def get_el_by_text(self, text, element, arg=0):
        text = text.lower()
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        els = self.driver.find_elements(locator_type, locator_value)
        counter = 0
        try:

            el = [x for x in els if text in x.text.lower()][0]

        except IndexError:
            el = False
            print("!!!!!!!!!!!____index error___!!!!!!!!!!!!!!")
            # sleep(0.5)
            # if counter < 6:
            #     counter += 1
            #     return self.get_el_by_text(text, element, arg=arg)

        return el

    def find_elements_in_element(self, main_el, locator, element):

        elements = main_el.find_elements(locator, element)
        return elements


    def find_elS_in_element(self, main_el, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        elements = main_el.find_elements(locator_type, locator_value)
        return elements


    def go_to_url(self, url):
        self.driver.get(url)

    def wait_presence_of_element(self, locator, element, time):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((locator, element)))

    def wait_presence_of_el(self, element, time, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((locator_type, locator_value)))

    def wait_presence_of_elS(self, element, time, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located((locator_type, locator_value)))

    def send_key(self, locator, element, string):
        self.driver.find_element(locator, element).send_keys(string)

    def send_k(self, element, string, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        self.driver.find_element(locator_type, locator_value).send_keys(string)

    def send_key_by_element(self, element, string):
        element.send_keys(string)

    def get_text_of_element(self, locator, element):
        el = self.driver.find_element(locator, element)
        return el.text

    def get_txt_of_el(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        return el.text

    def get_list_of_texts_in_elements(self, elements_list):

        text = [x.text for x in elements_list]
        return text

    def get_text_of_element_by_element(self, el):

        return el.text

    def find_element_and_return(self, locator_type, element):
        el = self.driver.find_element(locator_type, element)
        return el

    def find_el_and_return(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        return el


    def find_elementS_and_return(self, locator_type, element):
        el = self.driver.find_elements(locator_type, element)
        return el
    def find_elS_and_return(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_elements(locator_type, locator_value)
        return el

    def field_clear(self, locator, field):
        el = self.driver.find_element(locator, field)
        el.clear()

    def fld_clear(self, element, arg=0):
        locator_type = list(element.keys())[arg]
        locator_value = list(element.values())[arg]
        el = self.driver.find_element(locator_type, locator_value)
        el.clear()

    def get_el_by_name(self, name, locator):
        el = self.get_el_by_text(text=name, element=locator)
        return el










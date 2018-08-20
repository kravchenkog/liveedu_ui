from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class LoginHelper():

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def button_login_press_and_wait(self):
        self.driver.find_element_by_css_selector('a[href="/login"]').click()
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='username']")))

    def screen_login_is_presented(self):
        return  self.app.general.element_is_displayed(self.driver.find_element_by_css_selector
                                                      ('input[name="username"]'))

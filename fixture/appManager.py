
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


from fixture.screens_helper.home_screen_elements_helper import HomeElements
from fixture.screens_helper.login_helper import LoginHelper
from fixture.general_helper import GeneralHelper
from fixture.screens_helper.signup_helper import SignUpHelper
from fixture.string_generator_helper import StringGeneratoHelper
from fixture.screens_helper.username_screen_helper import UsernameHelper
from fixture.screens_helper.chose_you_role_screen_helper import ChoseYourRoleHelper
from fixture.screens_helper.add_contact_inf_helper import AddYouContactsInformationHelper
from fixture.screens_helper.pricing_screen_helper import PricingHelper
from fixture.property_user_factory import UserData
from fixture.api_helpers.route_helper import Route
from fixture.api_helpers.api_user_helper import APIHelper
from fixture.screens_helper.live_screen_helper import LiveScreenHelper
from fixture.screens_helper.verify_email_screen_helper import VerifyEmailHelper
from fixture.screens_helper.select_topics_to_learn_helper import SelectTopicstoLearnHelper
from fixture.api_helpers.api_environment_helper import Environment

class AppManager:
    def __init__(self, browser):
        self.env = Environment(1)  # dev
        if browser == 'firefox':

            self.profile = webdriver.FirefoxProfile()
            self.profile.set_preference('network.http.phishy-userpass-length', 255)
            self.driver = webdriver.Firefox()
            # self.driver.get("https://livecodingtv:csEAMHPfoetWUyY3hxwNPXuM@dev.liveedu.tv/")


            self.driver.get(self.env.base_url)
            wait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.send_keys('livecodingtv' + Keys.TAB + 'csEAMHPfoetWUyY3hxwNPXuM')
            alert.accept()


        else:
            print('incorrect browser')

        self.driver.set_window_size(1024, 768)
        self.driver.implicitly_wait(0.5)
        self.home_el = HomeElements(self)
        self.login = LoginHelper(self)
        self.signup = SignUpHelper(self)
        self.general = GeneralHelper(self)
        self.string = StringGeneratoHelper()
        self.username = UsernameHelper(self)
        self.chose_role = ChoseYourRoleHelper(self)
        self.cont_inf = AddYouContactsInformationHelper(self)
        self.pricing = PricingHelper(self)
        self.user_data = UserData()
        self.route = Route()
        self.api = APIHelper()
        self.live = LiveScreenHelper(self)
        self.verify_email = VerifyEmailHelper(self)
        self.select_topic_learn = SelectTopicstoLearnHelper(self)





    def destroy(self):
        self.driver.quit()
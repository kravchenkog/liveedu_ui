import pytest
fixture = None
from fixture.appManager import AppManager
from selenium.webdriver.common.by import By
import time

browser = 'firefox'

# @pytest.fixture(scope='function')
# def login_creator(request):
#     global user
#         if user_is_not_logged_in():
#             perform_login(creator)
#
#         elif logged_user = student:
#             perform_logout()
#             perform_login(creator)
#
#     return fixture

@pytest.fixture(scope='function')
def app_home(request):
    global fixture
    if fixture is None:
        fixture = AppManager(browser=browser)
    smart_start(fixture)
    return fixture

@pytest.fixture(scope='function')
def app_signup(request):
    global fixture
    if fixture is None:
        fixture = AppManager(browser=browser)
    smart_start_and_go_to_sign_up(fixture)
    return fixture

@pytest.fixture(scope='function')
def app_pr_r(request):
    global fixture
    if fixture is None:
        fixture = AppManager(browser=browser)
    smart_start_and_go_to_project_requests(fixture)
    return fixture


@pytest.fixture(scope='function')
def app_login(request):
    global fixture
    if fixture is None:
        fixture = AppManager(browser=browser)
    smart_start_and_go_to_login(fixture)
    return fixture


@pytest.fixture(scope='function')
def app_pricing(request):
    global fixture
    if fixture is None:
        fixture = AppManager(browser=browser)
    smart_start_and_go_to_pricing(fixture)
    return fixture



@pytest.fixture(scope='function')
def app_live(request):
    global fixture
    if fixture is None:
        fixture = AppManager(browser=browser)
    smart_start_and_go_to_live_screen(fixture)
    return fixture


@pytest.fixture(scope='function')
def app_test_users(request):
    global fixture
    if fixture is None:
        fixture = AppManager(browser=browser)
    if fixture.user_creator == None:
        fixture.user_creator = fixture.api.get_confirmed_user(fixture, fixture.user_creator, role='streamer')
        fixture.user_student = fixture.api.get_confirmed_user(fixture, fixture.user_student, role='viewer')
    return fixture

def smart_start_and_go_to_sign_up(fixture):

    if fixture.signup.screen_signup_is_presented() is not True:
        fixture.home_el.logout_go_home_and_wait()
        fixture.signup.button_signup_press_and_wait()

    else:
        fixture.signup.fields_clear()
    return fixture

def smart_start_and_go_to_login(fixture):
    if not fixture.login.screen_login_is_presented():


        fixture.home_el.logout_go_home_and_wait()
        fixture.login.button_login_press_and_wait()
    else:
        fixture.login.fields_clear()

def smart_start_and_go_to_pricing(fixture):
    if fixture.pricing.screen_pricing_is_presented() is not True:
        fixture.home_el.logout_go_home_and_wait()
        fixture.home_el.button_pricing_click()

def smart_start_and_go_to_live_screen(fixture):
    if not fixture.live.screen_live_is_presented():
        fixture.home_el.logout_go_home_and_wait()
        fixture.home_el.button_learnlive_click()

def smart_start_and_go_to_project_requests(fixture):
    if not fixture.request_project.screen_project_requests_is_displayed():
        fixture.home_el.logout_go_home_and_wait()
        fixture.home_el.button_learnlive_click()
        fixture.live.navigation_button_requests_press()
    # if fixture.request_project.button_all_is_selected() is True:
    fixture.general.but_press(fixture.request_project.button_all_main)
    check_filter_difficulty()
    check_filter_sorting()

    return fixture


def smart_start(fixture):

    if not fixture.home_el.home_screen_is_presented():
        fixture.home_el.logout_go_home_and_wait()


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return request



def check_filter_difficulty():
    filter_difficulty = fixture.request_project.get_difficulty_filter()
    if fixture.request_project.close_x_button_is_presented(
            fixture.request_project.buttons_in_filter, filter_difficulty):
        fil = fixture.request_project.get_filter_to_press(1)
        fixture.request_project.close_x_button_click(filter_difficulty, fil, 1)

def check_filter_sorting():
    if fixture.general.get_text_of_element_by_element(
            fixture.general.find_el_and_return(
                fixture.request_project.difficulty_text)) != 'Most Popular':
        fixture.request_project.select_value_in_right_filters(0, 'Most Popular')
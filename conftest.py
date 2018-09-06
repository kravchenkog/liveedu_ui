import pytest
fixture = None
from fixture.appManager import AppManager
import time

browser = 'firefox'

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
def app_project_requests(request):
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
    if not fixture.request_project.screen_project_requests_is_presented():
        fixture.home_el.logout_go_home_and_wait()
        fixture.home_el.button_learnlive_click()
        fixture.live.navigation_button_requests_press()
        return fixture


def smart_start(fixture):

    if fixture.home_el.home_screen_is_presented() is not True:
        fixture.home_el.logout_go_home_and_wait()


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return request
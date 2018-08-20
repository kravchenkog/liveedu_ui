import pytest
fixture = None
from fixture.appManager import AppManager

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

def smart_start_and_go_to_sign_up(fixture):

    if fixture.signup.screen_signup_is_presented() is not True:
        fixture.signup.button_signup_press_and_wait()
    else:
        fixture.signup.fields_clear()


def smart_start_and_go_to_pricing(fixture):
    if fixture.pricing.screen_pricing_is_presented() is not True:
        fixture.home_el.go_to_home_screen_and_wait()
        fixture.home_el.button_pricing_click()

def smart_start_and_go_to_live_screen(fixture):
    if not fixture.live.screen_live_is_presented():
        fixture.home_el.go_to_home_screen_and_wait()
        fixture.home_el.button_learnlive_click()

def smart_start(fixture):

    if fixture.home_el.home_screen_is_presented() is not True:
        fixture.home_el.go_to_home_screen_and_wait()


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return request
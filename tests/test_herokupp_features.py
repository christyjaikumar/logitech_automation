import pytest
import getpass
import os
from test_libs.authentication import Scenario_1
from test_libs.authentication import Scenario_2
from logging_module import logger


"""
test_herokupp_features
===============
This class covers herokupp features test cases

"""
global CHROME_PATH, HOME_PAGE, NAUKRI_APP
user_name = getpass.getuser()
CHROME_PATH = os.path.join("C:\\","Users",user_name, "PycharmProjects","logitech_automation", "drivers", "chromedriver.exe")
HOME_PAGE = 'http://the-internet.herokuapp.com/'
NAUKRI_APP = 'https://www.naukri.com/'


#@pytest.mark.usefixtures("OneTimeSetUp")
#class Test_setup:
    #@pytest.fixture(scope='class', autouse=True)
    #def initial_setup(self):
sc1 = Scenario_1(CHROME_PATH, HOME_PAGE)
sc2 = Scenario_2(CHROME_PATH, NAUKRI_APP)
logger = logger.get_logger()

#class Test_herokupp(Test_setup):
    #test = Test_setup.initial_setup()

@pytest.mark.t1
@pytest.mark.herokupp
def test_t1_verify_form_authentication():

    assert sc1.t1_verify_form_authentication()

@pytest.mark.t2
@pytest.mark.herokupp
def test_t2_verify_dynamic_loading():
    assert sc1.t2_verify_dynamic_loading()
    #assert self.initial_setup.sc1.t2_verify_dynamic_loading()

@pytest.mark.t3
@pytest.mark.herokupp
def test_t3_verify_form_authentication():
    assert sc1.t3_verify_multiple_windows()
    #
    # assert self.sc1.t3_verify_multiple_windows()

@pytest.mark.t4
@pytest.mark.herokupp
def test_t4_verify_drag_drop():
    assert sc1.t4_verify_drag_drop()

@pytest.mark.t5
@pytest.mark.herokupp
def test_t5_verify_frames():
    assert sc1.t5_verify_frames()

@pytest.mark.t6
@pytest.mark.herokupp
def test_t6_verify_javascript_alerts():
    text_to_verify = "You clicked: Cancel"
    assert sc1.t6_verify_javascript_alerts(text_to_verify)


@pytest.mark.naukri
def test_verify_naukri_app():
    assert sc2.launch_naukri_app()
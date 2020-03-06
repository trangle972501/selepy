import pytest
import logging

from selenpy.support import browser
from selenpy.helper.data_test import get_data
from tests.pages.ta_home_page import TestArchitectHomePage
from tests.pages.ta_new_page import TestArchitectNewPage

class TestBase():
    
    test_data = get_data("DATA")
    ta_home_page = TestArchitectHomePage()
    ta_new_page = TestArchitectNewPage()

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))                
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        browser.open_url(self.test_data["url"])
        # Close all browsers when tests have been finished
        yield        
        browser.quit_all_browsers()
    
    @pytest.fixture()
    def logout(self):
        yield
        self.ta_home_page.logout()
        
    @pytest.fixture()
    def close_alert(self):
        yield
        browser.accept_alert()
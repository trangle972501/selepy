from tests.testcases.test_base import TestBase
from tests.pages.ta_login_page import TestArchitectLoginPage
from tests.pages.ta_home_page import TestArchitectHomePage
from tests.pages.ta_panel_page import TestArchitectPanelPage
from selenpy.support import browser
import logging
import pytest

class TestArchitectPanel(TestBase):
    
    ta_login_page = TestArchitectLoginPage()
    ta_home_page = TestArchitectHomePage()
    ta_panel_page = TestArchitectPanelPage()
    
    _str_username = TestBase.test_data["test_user"]
    _str_password = TestBase.test_data["test_pass"]
    _str_same_repo = "SampleRepository"
    
    def test_DA_LOGIN_TC001(self):
        logging.info("Verify that user can login specific repository successfully via Dashboard login page with correct credentials")
        
        logging.info("Step 1: Log in Dashboard")
        self.ta_login_page.login(self._str_username, self._str_password,self._str_same_repo)
        
        logging.info("Step 2: Navigate to Panels page")
        self.ta_home_page.go_to_data_profile("Panels")
        
        logging.info("Step 3: Click on 'Add New'")
        self.ta_panel_page.go_to_panel_page()
        
        
from tests.testcases.test_base import TestBase
from tests.pages.ta_login_page import TestArchitectLoginPage
from tests.pages.ta_home_page import TestArchitectHomePage
from tests.pages.ta_data_profile import TestArchitectDataProfilePage
from tests.pages.ta_profile_page import TestArchitectProfilePage
from selenpy.support import browser
import logging
import pytest

class TestArchitectProfile(TestBase):
    
    ta_login_page = TestArchitectLoginPage()
    ta_home_page = TestArchitectHomePage()
    ta_data_profile_page = TestArchitectDataProfilePage()
    ta_profile_page = TestArchitectProfilePage()
    
    _str_username = TestBase.test_data["test_user"]
    _str_password = TestBase.test_data["test_pass"]
    _str_same_repo = "SampleRepository"
    _str_mess = "Please input profile name."
    _str_special_characters = '/:*?<>|"#[ ]{}=%;'
    _str_error_special_characters = 'Invalid name. The name cannot contain high ASCII characters or any of the following characters: /:*?<>|"#[]{}=%;'
    _str_data_profile_name = "a"
    _str_error_duplicate_name = "Data profile name already exists."
    _list_data= ['Test Modules', 'Test Cases', 'Test Objectives', 'Data Sets', 'Actions', 'Interface Entities', 'Test Results', 'Test Case Results', 'Test Suites', 'Bugs']
    
    def test_DA_LOGIN_TC001(self, close_alert):
        logging.info("Verify that user can login specific repository successfully via Dashboard login page with correct credentials")
        
        logging.info("Step 1: Log in Dashboard")
        self.ta_login_page.login(self._str_username, self._str_password,self._str_same_repo)
        
        logging.info("Step 2: Navigate to Data Profiles page")
        self.ta_home_page.go_to_data_profile("Data Profiles")
        
        logging.info("Step 3: Click on 'Add New'")
        self.ta_data_profile_page.go_to_add_profile()
        
        logging.info("Step 4: Click on 'Next Button'")
        self.ta_profile_page.click_button("Next")
        
        logging.info("Step 5: Check dialog message 'Please input profile name' appears")
        assert self._str_mess == browser.get_alert_message()
        browser.accept_alert()
        
        logging.info("Step 6: Click on 'Finish Button'")
        self.ta_profile_page.click_button("Finish")
        
        logging.info("Step 7: Check dialog message 'Please input profile name' appears")
        assert self._str_mess == browser.get_alert_message()
    
    def test_DA_DP_TC070(self, close_alert):
        logging.info("Verify that special characters ' /:*?<>|' #[ ]{}=%; 'is not allowed for input to 'Name *' field")
        
        logging.info("Step 1: Log in Dashboard")
        self.ta_login_page.login(self._str_username, self._str_password,self._str_same_repo)
        
        logging.info("Step 2: Navigate to Data Profiles page")
        self.ta_home_page.go_to_data_profile("Data Profiles")
        
        logging.info("Step 3: Click on 'Add New''")
        self.ta_data_profile_page.go_to_add_profile()
        
        logging.info("Step 4: Input special character")
        self.ta_profile_page.create_profile(self._str_special_characters)
        self.ta_profile_page.click_button("Finish")
        
        logging.info("Step 5: Check dialog message indicates invalid characters: /:*?<>|'#[ ]{}=%; is not allowed as input for name field appears")
        assert self._str_error_special_characters == browser.get_alert_message()
        
    def test_DA_DP_TC071(self, test_DA_DP_TC071_precondition):
        logging.info("Verify that Data Profile names are not case sensitive")
        
        logging.info("Step 1: Log in Dashboard")
        logging.info("Step 2: Navigate to Data Profiles page")
        logging.info("Step 3: Click on 'Add New''")
        self.ta_data_profile_page.go_to_add_profile()
        
        logging.info("Step 4: Input charater 'A' into 'Name *' field")
        self.ta_profile_page.create_profile(self._str_data_profile_name)
        
        logging.info("Step 5: Click 'Next' button ")
        self.ta_profile_page.click_button("Next")
        
        logging.info("Step 6: Check dialog message 'Data Profile name already exists'")
        assert self._str_error_duplicate_name == browser.get_alert_message()
    
    def test_DA_DP_TC072(self):
        logging.info("Verify that all data profile types are listed under 'Item Type' dropped down menu")
        
        logging.info("Step 1: Navigate to Dashboard login page")
        logging.info("Step 2: Select a specific repository")
        logging.info("Step 3: Enter valid Username and Password")
        logging.info("Step 4: Click Login")
        self.ta_login_page.login(self._str_username, self._str_password,self._str_same_repo)
        
        logging.info("Step 5: Click Administer->Data Profiles")
        self.ta_home_page.go_to_data_profile("Data Profiles")
        
        logging.info("Step 6: Click 'Add New' link")
        self.ta_data_profile_page.go_to_add_profile()
        
        logging.info("Step 7: Check all data profile types are listed under 'Item Type' dropped down menu in create profile page")
        assert (self.ta_profile_page.do_items_exist(self._list_data))
  
    @pytest.fixture()
    def test_DA_DP_TC071_precondition(self):
        logging.info("Step 1: Log in Dashboard")
        self.ta_login_page.login(self._str_username, self._str_password,self._str_same_repo)
        
        logging.info("Step 2: Navigate to Data Profiles page")
        self.ta_home_page.go_to_data_profile("Data Profiles")
        
        logging.info("Step 3: Click on 'Add New''")
        self.ta_data_profile_page.go_to_add_profile()
        
        logging.info("Step 4: Input charater 'A' into 'Name *' field")
        self.ta_profile_page.create_profile(self._str_data_profile_name)
        self.ta_profile_page.click_button("Finish")
        
        yield
        browser.accept_alert()
        self.ta_profile_page.click_button("Cancel")
        self.ta_data_profile_page.delete_data_profile(self._str_data_profile_name)
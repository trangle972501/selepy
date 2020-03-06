from tests.pages.ta_home_page import TestArchitectHomePage
from tests.pages.ta_login_page import TestArchitectLoginPage
from tests.pages.ta_new_page import TestArchitectNewPage
from tests.testcases.test_base import TestBase
from selenpy.support import browser
import logging
import pytest

class TestArchitectHome(TestBase):
    ta_home_page = TestArchitectHomePage()
    ta_login_page = TestArchitectLoginPage()
    ta_new_page = TestArchitectNewPage()
    
    _str_username = TestBase.test_data["test_user"]
    _str_password = TestBase.test_data["test_pass"]
    _str_repository = "SampleRepository"
    _str_page1 = "Page 1"
    _str_page2 = "Page 2"
    _str_page3 = "Page 3"
    _str_page4 = "Page 4"
    _str_page = "Test"
    _str_child_page = "Test Child 1"
    _error_message = "%s already exists. Please enter a different name."%(_str_child_page)
        
    def test_DA_MP_TC021(self, test_DA_MP_TC021_clean_up):
        logging.info("Verify that user is able to edit the name of the page (Parent/Sibbling) successfully")
        
        logging.info("Step 1: Navigate to Dashboard login page")
        logging.info("Step 2: Login with valid account")
        self.ta_login_page.login(self._str_username, self._str_password, self._str_repository)
        
        logging.info("Step 3: Go to Global Setting -> Add page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        
        logging.info("Step 4: Enter info into all required fields on New Page dialog")
        self.ta_new_page.add_new_page(self._str_page1, "Overview")
        
        logging.info("Step 5: Go to Global Setting -> Add page")
        self.ta_new_page.go_to_global_setting()
        self.ta_new_page.select_menu("Add Page")
        
        logging.info("Step 6: Enter info into all required fields on New Page dialog")
        self.ta_new_page.add_new_page(self._str_page2,self._str_page1)
        
        logging.info("Step 7: Go to the first created page")
        self.ta_new_page.go_to_page("Overview/"+ self._str_page1)
        
        logging.info("Step 8: Click Edit link")
        self.ta_new_page.go_to_global_setting()
        self.ta_new_page.go_to_edit_page()
    
        logging.info("Step 9: Enter another name into Page Name field")
        logging.info("Step 10: Click Ok button on Edit Page dialog")
        self.ta_new_page.edit_page(self._str_page3)
        
        logging.info("Step 11: Observe the current page")
        assert self.ta_new_page.get_title_page() == self._str_page3
        
        logging.info("Step 12: Go to the second created page")
        self.ta_new_page.go_to_page("Overview/" + self._str_page3 + "/" + self._str_page2)
        
        logging.info("Step 13: Click Edit link")
        self.ta_new_page.go_to_global_setting()
        self.ta_new_page.go_to_edit_page()
        
        logging.info("Step 14: Enter another name into Page Name field")
        logging.info("Step 15: Click Ok button on Edit Page dialog")
        self.ta_new_page.edit_page(self._str_page4)
        
        logging.info("Step 16: Observe the current page")
        assert self.ta_new_page.get_title_page() == self._str_page4
        
    def test_DA_MP_TC022(self, test_DA_MP_TC022_clean_up):
        logging.info("Verify that user is unable to duplicate the name of sibbling page under the same parent page")
        
        logging.info("Step 1: Navigate to Dashboard login page")
        logging.info("Step 2: Login with valid account")
        self.ta_login_page.login(self._str_username, self._str_password, self._str_repository)
        
        logging.info("Step 3: Add a new page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        self.ta_new_page.add_new_page(self._str_page)
        
        logging.info("Step 4: Add a sibling page of new page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        self.ta_new_page.add_new_page(self._str_child_page, self._str_page)
        
        logging.info("Step 5: Go to Global Setting -> Add page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        
        logging.info("Step 6: Enter Page Name")
        logging.info("Step 7: Click on  Parent Page dropdown list")
        logging.info("Step 8: Select a parent page")
        logging.info("Step 9: Click OK button")
        self.ta_new_page.add_new_page(self._str_child_page, self._str_page)
        
        logging.info("Step 10: Check warning message 'Test child already exist. Please enter a diffrerent name' appears")
        assert browser.get_alert_message() == self._error_message
        
        
    def test_DA_MP_TC023(self, test_DA_MP_TC023_clean_up):
        logging.info("Verify that user is able to edit the parent page of the sibbling page successfully")
        
        logging.info("Step 1: Navigate to Dashboard login page")
        logging.info("Step 2: Login with valid account")
        self.ta_login_page.login(self._str_username, self._str_password, self._str_repository)
        
        logging.info("Step 3: Go to Global Setting -> Add page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        
        logging.info("Step 4: Enter info into all required fields on New Page dialog")
        self.ta_new_page.add_new_page(self._str_page1, "Overview")
        
        logging.info("Step 5: Go to Global Setting -> Add page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        
        logging.info("Step 6: Enter info into all required fields on New Page dialog")
        self.ta_new_page.add_new_page(self._str_page2, self._str_page1)
        
        logging.info("Step 7: Go to the first created page")
        self.ta_new_page.go_to_page("Overview/" + self._str_page1)
        
        logging.info("Step 8: Click Edit link")
        self.ta_new_page.go_to_global_setting()
        self.ta_new_page.go_to_edit_page()
        
        logging.info("Step 9: Enter another name into Page Name field")
        logging.info("Step 10: Click Ok button on Edit Page dialog")
        self.ta_new_page.edit_page(self._str_page3)
        
        logging.info("Step 11: Observe the current page")
        assert self.ta_new_page.get_title_page() == self._str_page3
    
    def test_DA_MP_TC024(self, test_DA_MP_TC024_clean_up):
        logging.info("Verify that 'Bread Crums' navigation is correct")
        
        logging.info("Step 1: Navigate to Dashboard login page")
        logging.info("Step 2: Login with valid account")
        self.ta_login_page.login(self._str_username, self._str_password, self._str_repository)
        
        logging.info("Step 3: Go to Global Setting -> Add page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        
        logging.info("Step 4: Enter info into all required fields on New Page dialog")
        self.ta_new_page.add_new_page(self._str_page1, "Overview")
        
        logging.info("Step 5: Go to Global Setting -> Add page")
        self.ta_home_page.go_to_global_setting()
        self.ta_home_page.select_menu("Add Page")
        
        logging.info("Step 6: Enter info into all required fields on New Page dialog")
        self.ta_new_page.add_new_page(self._str_page2, self._str_page1)
        
        logging.info("Step 7: Click the first breadcrums")
        self.ta_new_page.go_to_page("Overview/" + self._str_page1)
        
        logging.info("Step 8: Observe the current page")
        assert self.ta_new_page.get_title_page() == self._str_page1
        
        logging.info("Step 9: Click the second breadcrums")
        self.ta_new_page.go_to_page("Overview/" + self._str_page1 + "/" + self._str_page2)
        
        logging.info("Step 10: Observe the current page")
        assert self.ta_new_page.get_title_page() == self._str_page2
        
    @pytest.fixture()
    def test_DA_MP_TC021_clean_up(self):
        yield
        self.ta_new_page.delete_page("Overview/" + self._str_page3 + "/" + self._str_page4)
        self.ta_new_page.delete_page("Overview/" + self._str_page3)
    
    @pytest.fixture()
    def test_DA_MP_TC022_clean_up(self):
        yield
        browser.accept_alert()
        self.ta_new_page.cancel_page()
        self.ta_new_page.delete_page(self._str_page + "/" + self._str_child_page)
        self.ta_new_page.delete_page(self._str_page)
    
    @pytest.fixture()
    def test_DA_MP_TC023_clean_up(self):
        yield
        self.ta_new_page.delete_page("Overview/" + self._str_page3 + "/" + self._str_page2)
        self.ta_new_page.delete_page("Overview/" + self._str_page3)
        
    @pytest.fixture()
    def test_DA_MP_TC024_clean_up(self):
        yield
        self.ta_new_page.delete_page("Overview/" + self._str_page1 + "/" + self._str_page2)
        self.ta_new_page.delete_page("Overview/" + self._str_page1)
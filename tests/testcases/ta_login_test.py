from tests.testcases.test_base import TestBase
from tests.pages.ta_login_page import TestArchitectLoginPage
from tests.pages.ta_home_page import TestArchitectHomePage
from selenpy.element.base_element import BaseElement
from selenpy.support import browser
import logging


class TestArchitectLogin(TestBase):
    
    ta_login_page = TestArchitectLoginPage()
    ta_home_page = TestArchitectHomePage()
    
    _str_username = TestBase.test_data["username"]
    _str_password = TestBase.test_data["password"]
    _str_same_repo = "SampleRepository"
    _str_invalid_username = "abc"
    _str_invalid_password = "abc"
    _str_error_invalid_credential = "Username or password is invalid"
    
    def test_DA_LOGIN_TC001(self, logout):
        logging.info("Verify that user can login specific repository successfully via Dashboard login page with correct credentials")
        self.ta_login_page.login(self._str_username, self._str_password,self._str_same_repo)
        _str_actual = BaseElement("xpath=//div[@id='header']//a[text()='" + self._str_username + "']")
        _str_expect = self._str_username
        assert _str_actual.get_text() == _str_expect
    
    def test_DA_LOGIN_TC002(self, close_alert):
        logging.info("Verify that user fails to login specific repository successfully via Dashboard login page with incorrect credentials")
        self.ta_login_page.login(self._str_invalid_username, self._str_invalid_password, self._str_same_repo)
        _str_actual = browser.get_alert_message()
        _str_expect = self._str_error_invalid_credential
        assert _str_actual == _str_expect
        
    def test_DA_LOGIN_TC003(self, close_alert):
        logging.info("Verify that user fails to log in specific repository successfully via Dashboard login page with correct username and incorrect password")
        self.ta_login_page.login(self._str_username, self._str_invalid_password, self._str_same_repo)
        _str_actual = browser.get_alert_message()
        _str_expect = self._str_error_invalid_credential
        assert _str_actual == _str_expect 
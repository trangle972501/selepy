from selenpy.element.base_element import BaseElement
from tests.pages.ta_home_page import TestArchitectHomePage
from tests.common import constant
from selenpy.support import browser

class TestArchitectDataProfilePage():
    
    ta_home_page = TestArchitectHomePage()
    
    _txt_add_new = BaseElement("xpath=//form[@id='form1']//a[text()='Add New']")
    _dynamic_string = "//a[text()='{}']//ancestor::tr//a[text()='{}']"
    
    def go_to_add_profile(self):
        self._txt_add_new.click()
    
    def delete_data_profile(self, data):
        browser.wait_for_page_load_by_ajax()
        _txt_delete = BaseElement(self._dynamic_string.format(data, 'Delete'))
        _txt_delete.wait_for_clickable(constant.MEDIUM_TIME_OUT/6)
        _txt_delete.click()
        browser.accept_alert()
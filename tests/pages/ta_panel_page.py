from selenpy.element.base_element import BaseElement
from tests.pages.ta_home_page import TestArchitectHomePage
from tests.common import constant
from selenpy.support import browser

class TestArchitectPanelPage():
    
    ta_home_page = TestArchitectHomePage()
    
    _txt_add_new = BaseElement("xpath=//form[@id='form1']//a[text()='Add New']")
    
    def go_to_panel_page(self):
        self._txt_add_new.click()
    
    def is_disable(self):
from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be,have
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.check_box import CheckBox
from selenpy.element.button import Button
from tests.pages.ta_home_page import TestArchitectHomePage
from selenpy.support import browser
from tests.common import constant

class TestArchitectNewPage(TestArchitectHomePage):
    _txt_title = BaseElement("xpath=//div[@id='div_popup']//h2[text()='New Page']")
    _txt_page_name = TextBox("id=name")
    _cbo_parent_page = ComboBox("id=parent")
    _bnt_ok = Button("id=OK")
    _bnt_cancel = Button("id=Cancel")
    _chk_public = CheckBox("id=ispublic")
    _str_delete_page = "Delete"
    _str_edit_page = "Edit"
    
    def select_combox_menu(self, item):
        self._txt_title.wait_until(be.visible)
        self._cbo_parent_page.select_by_visible_text(item)
    
    def fill_on_fields(self, name_page, parent_page=None, number_of_page=None, display_after=None, check=None):
        
        self._txt_page_name.clear_text()
        self._txt_page_name.send_keys(name_page)
        self._txt_page_name.wait_until(have.value(name_page))
        
        if parent_page != None:
            self.select_parent_dropdown(parent_page)
        if number_of_page != None:
            self.select_combox_menu(number_of_page)
        if display_after != None:
            self.select_combox_menu(display_after)
        if check != None:
            self._chk_public.click()
        
    def add_new_page(self, name_page, parent_page=None, number_of_col=None, display_after=None,public_check=None):
        self.fill_on_fields(name_page, parent_page, number_of_col, display_after,public_check)
        self._bnt_ok.wait_for_clickable(constant.MEDIUM_TIME_OUT/6)
        self._bnt_ok.click()
        
    def go_to_edit_page(self):
        TestArchitectHomePage.select_menu(self, self._str_edit_page)
        
    def go_to_delete_page(self):
        TestArchitectHomePage.select_menu(self, self._str_delete_page)
        
    def edit_page(self,name_page, parent_page=None, number_of_col=None, display_after=None,public_check=None):
        self.fill_on_fields(name_page, parent_page, number_of_col, display_after,public_check )
        self._bnt_ok.wait_for_clickable(constant.MEDIUM_TIME_OUT/5)
        self._bnt_ok.click()
    
    def delete_page(self, page_path):
        TestArchitectHomePage.go_to_page(self, page_path)
        TestArchitectHomePage.go_to_global_setting(self)
        self.go_to_delete_page()
        browser.accept_alert()
        
    def get_title_page(self):
        browser.wait_for_page_load_by_ajax()
        title = browser.get_title()
        spl_title = title.split("-")
        title = spl_title[-1] 
        return title.strip()
    
    def cancel_page(self):
        self._bnt_cancel.wait_for_clickable(constant.MEDIUM_TIME_OUT/5)
        self._bnt_cancel.click()
        
    def select_parent_dropdown(self, item):
        self._cbo_parent_page.click()
        browser.wait_for_page_load_by_ajax()
        elements = self._cbo_parent_page.options()
        for element in elements:
            if element.text.strip() == item:
                element.click()
                break        
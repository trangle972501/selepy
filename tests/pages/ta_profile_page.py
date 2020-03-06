from selenpy.element.base_element import BaseElement
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from tests.common import constant
from selenpy.support import browser

class TestArchitectProfilePage():
    
    _txt_name_profile = TextBox("id=txtProfileName")
    _cbo_item_type = ComboBox("id=cbbEntityType")
    _cb_related_data = ComboBox("id=cbbSubReport")
    dynamic_string = "//input[@value='{}']"
    
    def create_profile(self, profile_name, item_type=None, related_data=None):
        
        self._txt_name_profile.clear_text()
        self._txt_name_profile.send_keys(profile_name)
        
        if item_type != None:
            self._cbo_item_type.select_by_visible_text(item_type)
        
        if related_data != None:
            self._cb_related_data.select_by_visible_text(related_data)
     
    def click_button(self, button_name):
        browser.wait_for_page_load_by_ajax()
        _btn_button_name = BaseElement(self.dynamic_string.format(button_name))
        _btn_button_name.wait_for_clickable(constant.MEDIUM_TIME_OUT/6)
        _btn_button_name.click()
        
    def get_all_options_item_type(self):
        self._cbo_item_type.click()
        browser.wait_for_page_load_by_ajax()
        items = self._cbo_item_type.options()
        list_items = []
        
        for item in items:
            list_items.append(item.text)
        return list_items
    
    def do_items_exist(self, list_data):
        result =  all(elem in list_data for elem in self.get_all_options_item_type())
        return result
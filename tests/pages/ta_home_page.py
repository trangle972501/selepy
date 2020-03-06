from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be
from selenpy.support import browser
from tests.common import constant

class TestArchitectHomePage():
    
    dynamic_string = "xpath=//a[translate(text(),'\u00A0', '')='{}']"
    _txt_logout = BaseElement("xpath=//div[@id='header']//a[text()='Logout']")
    _txt_username = BaseElement("xpath=//div[@id='header']//a[@href='#Welcome']")
    _icon_setting = BaseElement("xpath=//div[@id='main-menu']//li[@class='mn-setting']")
    _txt_data_profile = BaseElement("xpath=//div[@class = 'container']//a[text()='Administer']")
    
    def logout(self):
        self._txt_username.click()
        self._txt_logout.wait_until(be.visible)
        self._txt_logout.click()
        
    def select_menu(self, item):
        element = BaseElement(self.dynamic_string.format(item))
        element.wait_until(be.visible)
        element.click()
        
    def go_to_global_setting(self):
        browser.wait_for_page_load_by_ajax()
        self._icon_setting.wait_for_visible(constant.MEDIUM_TIME_OUT/6)
        self._icon_setting.click()

    def go_to_page(self, page_path):
        browser.wait_for_page_load_by_ajax()
        nodes = page_path.split("/")
        for node in nodes:
            page_button = BaseElement("xpath = //div[@class = 'container']//a[text()='{}']".format(node.replace(" ","\u00a0")))
            page_button.move_to_element()
        page_button.click()

    def go_to_data_profile(self, item):
        self._txt_data_profile.click()
        self.select_menu(item)

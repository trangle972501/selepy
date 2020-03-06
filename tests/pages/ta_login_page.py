from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.base_element import BaseElement
from selenpy.support import browser
from selenpy.support.conditions import have

class TestArchitectLoginPage():
    
    _txt_username = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("xpath=//div[@class='btn-login']")
    _combox_repository = ComboBox("id=repository")
    _str_title = "TestArchitect"
    
    def login(self, username, password, repository):
        browser.wait_until(have.title(self._str_title))
        self._combox_repository.select_by_value(repository)
        self._txt_username.clear_text()
        self._txt_username.send_keys(username)
        self._txt_password.clear_text()
        self._txt_password.send_keys(password)
        self._btn_login.click()
from selenpy.support import factory
from selenpy.common import config
from selenpy.helper.wait import wait_for
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging
from tests.common import constant

def get_driver():
    return factory.get_shared_driver()

def get_title():
    return get_driver().title

def maximize_browser():
    get_driver().maximize_window()

        
def open_url(url):
    get_driver().get(url)    


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_browser():
    factory.close_browser()


def quit_all_browsers():
    factory.quit_all_browsers()


def start_driver(name, remote_host, key="default"):
    factory.start_driver(name, remote_host, key)


def wait_until(webdriver_condition, timeout=None, polling=None):
    if timeout is None:
        timeout = config.timeout
    if polling is None:
        polling = config.poll_during_waits

    return wait_for(get_driver(), webdriver_condition, timeout, polling)

def wait_for_alert():
    return WebDriverWait(get_driver(), constant.MEDIUM_TIME_OUT/6).until(expected_conditions.alert_is_present())
    
def accept_alert():
    return wait_for_alert().accept()
    
def get_alert_message():
    return wait_for_alert().text

def wait_for_page_load_by_ajax():
    wait = WebDriverWait(get_driver(), constant.MEDIUM_TIME_OUT)
    try:
        wait.until(lambda driver: get_driver().execute_script('return document.readyState') == 'complete')
        wait.until(lambda driver: get_driver().execute_script('return jQuery.active') == 0)    
    except Exception as e:
        logging.info(str(e))
        pass
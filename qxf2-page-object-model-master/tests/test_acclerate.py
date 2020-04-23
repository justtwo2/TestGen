import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.mobile_bitcoin_conf as conf
import conf.testrail_caseid_conf as testrail_file
import pytest
from page_objects.Mobile_Base_Page import Mobile_Base_Page
import time
from appium import webdriver
class AccleratePage(Mobile_Base_Page):

    def start(self):
        "Use this method to go to specific URL -- if needed"
        pass


@pytest.mark.MOBILE
def test_mobile_bitcoin_price(test_mobile_obj):
    time.sleep(10)
if __name__ == '__main__':
    desired_caps = {

        "deviceName": "HLR4C19802004725",
        "automationName": "appium",
        "platformName": "Android",
        "platformVersion": "9",
        #"app":r"D:\雨燕\package\yyjs-android-test-pr-r-49.apk",
        "appPackage":"cn.yyjs",
        "appActivity": "cn.yyjs.MainActivity",
        "noReset" : True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    test_mobile_obj = AccleratePage(driver)

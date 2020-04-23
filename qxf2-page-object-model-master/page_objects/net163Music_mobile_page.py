"""
This class models the first dummy page needed by the framework to start.
URL: None
Please do not modify or delete this page
"""
import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .Mobile_Base_Page import Mobile_Base_Page
from utils.Wrapit import Wrapit
import conf.locators_mobile_acclerate_conf as locators
import conf.mobile_app_conf as app_conf

class Net163Music_Mobile_Page(Mobile_Base_Page):
    app_conf = app_conf.app_net126Music
    netease_userAgreement = locators.netease_userAgreement
    netease_trial = locators.netease_trial
    netease_rand = locators.netease_rand
    netease_search = locators.netease_search
    netease_search_text = locators.netease_search_text
    netease_search_button = locators.netease_search_button
    netease_search_result1 = locators.netease_search_result1
    netease_error = locators.netease_error
    def start(self):
        "Use this method to go to specific URL -- if needed"
        print("start")
        pass

    @Wrapit._screenshot
    def click_netease_userAgreement(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.netease_userAgreement):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click userAgreement',
                negative='Failed to click userAgreement',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def click_netease_trial(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.netease_trial):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click trial',
                negative='Failed to click trial',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def click_netease_rand(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.netease_rand):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click netease_rand',
                negative='Failed to click netease_rand',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def click_netease_netease_search(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.netease_search):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click netease_search',
                negative='Failed to netease_search',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag
    
    @Wrapit._screenshot
    def input_netease_search_text(self,text):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.set_text(self.netease_search_text,text):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='input netease_search_text',
                negative='Failed to input netease_search_text',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def click_netease_search_button(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.netease_search_button):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click netease_search_button',
                negative='Failed to netease_search_button',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def click_netease_netease_search_result1(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.netease_search_result1):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click netease_search_result1',
                negative='Failed to netease_search_result1',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def check_result_errror(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.check_element_displayed(self.netease_error):
                result_flag = False
            else:
                result_flag = True    
            self.conditional_write(result_flag,
                positive='check area limit',
                negative='Failed to check area limit',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag 
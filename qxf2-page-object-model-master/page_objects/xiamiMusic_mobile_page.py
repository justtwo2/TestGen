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

class XiamiMusic_Mobile_Page(Mobile_Base_Page):
    app_conf = app_conf.app_xiamiMusic
    xiamiMusic_search = locators.xiamiMusic_search
    xiamiMusic_search_text = locators.xiamiMusic_search_text
    xiamiMusic_search_button = locators.xiamiMusic_search_button
    #吴亦凡 极光
    xiamiMusic_WYFJG_2 = locators.xiamiMusic_WYFJG_2
    xiamiMusic_error = locators.xiamiMusic_error
    def start(self):
        "Use this method to go to specific URL -- if needed"
        print("start")
        pass

    @Wrapit._screenshot
    def click_xiamiMusic_search(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.xiamiMusic_search):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click xiamiMusic_search',
                negative='Failed to click xiamiMusic_search',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def click_xiamiMusic_search_button(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.xiamiMusic_search_button):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click xiamiMusic_search_button',
                negative='Failed to click xiamiMusic_search_button',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

   
    def input_xiamiMusic_search_text(self,text):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.set_text(self.xiamiMusic_search_text,text):
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
    def click_xiamiMusic_WYFJG_2(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.xiamiMusic_WYFJG_2):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click netease_search_result1',
                negative='Failed to xiamiMusic_WYFJG_2',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def check_result_errror(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.check_element_displayed(self.xiamiMusic_error):
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
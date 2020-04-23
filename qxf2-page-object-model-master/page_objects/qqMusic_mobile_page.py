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

class QQMusic_Mobile_Page(Mobile_Base_Page):
    app_conf = app_conf.app_qqMusic
    qqMusic_cancleLogin = locators.qqMusic_cancleLogin
    qqMusic_YYG = locators.qqMusic_YYG #音乐馆
    qqMusic_rand = locators.qqMusic_rand
    qqMusic_soaringList = locators.qqMusic_soaringList
    qqMusic_error = locators.qqMusic_error
    checkList = [locators.qqMusic_soaringList1,locators.qqMusic_soaringList2,locators.qqMusic_soaringList3,locators.qqMusic_soaringList4,locators.qqMusic_soaringList5]
    def start(self):
        "Use this method to go to specific URL -- if needed"
        print("start")
        pass

    @Wrapit._screenshot
    def click_qqMusic_cancleLogin(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.qqMusic_cancleLogin):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='cancle login',
                negative='Failed to cancle login',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag

    @Wrapit._screenshot
    def click_qqMusic_YYG(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.qqMusic_YYG):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='点击 音乐馆',
                negative='进入音乐馆失败',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def click_qqMusic_rand(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.qqMusic_rand):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='点击排行榜',
                negative='进入排行榜失败',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def click_qqMusic_soaringList(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.qqMusic_rand):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='查看飙升榜',
                negative='打开飙升版失败',
                level='debug')
        except Exception as e:
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def check_qqMusic_soaringList(self):
        try:
            # Click on real time price page button.
            result_flag = True
            for check in self.checkList:
                self.write(check)
                self.click_element(check)
                if self.check_element_displayed(self.qqMusic_error):
                    result_flag = False
                    break
                else:
                    self.write("QQMusic check_qqMusic_soaringList success")
        except Exception as e:
            self.write(str(e),level="error")
        return result_flag
    
   
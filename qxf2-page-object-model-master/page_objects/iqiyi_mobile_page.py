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
class Iqiyi_Mobile_Page(Mobile_Base_Page):
    app_conf = app_conf.app_iqiyi
    iqiyi_search_begin = locators.iqiyi_search_begin
    iqiyi_search_input = locators.iqiyi_search_input
    iqiyi_search_click = locators.iqiyi_search_click
    iqiyi_QYN_1 = locators.iqiyi_QYN_1
    iqiyi_error = locators.iqiyi_error
    def start(self):
        "Use this method to go to specific URL -- if needed"
        print("start")
        pass

    @Wrapit._screenshot
    def click_search_begin(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.iqiyi_search_begin):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='click_search_begin',
                negative='Failed to click_search_begin',
                level='debug')

        except Exception as e:
            self.write("点击爱奇艺搜索框失败")  
            self.write(str(e))
        return result_flag
    
    @Wrapit._screenshot
    def input_search_text(self,text):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.set_text(self.iqiyi_search_input,text):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='iqiyi input search text',
                negative='iqiyi Failed to input search text',
                level='debug')

        except Exception as e:
            self.write("输入搜索文本失败")  
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def click_search_button(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.iqiyi_search_click):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='爱奇艺确认搜索点击搜索按钮',
                negative='爱奇艺点击搜索按钮失败',
                level='debug')

        except Exception as e:
            self.write("爱奇艺点击搜索按钮失败")  
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def select_QYN_series(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.iqiyi_QYN_1):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='选择搜索结果第一集',
                negative='选择剧集失败',
                level='debug')

        except Exception as e:
            self.write("Exception while clicking on the bitcoin real time price button.")  
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def play_video(self,time):
        try:
            for i in range (0,time):
                self.wait(1)
            result_flag = True
            self.conditional_write(result_flag,
                positive='爱奇艺视频播放，进行等待操作',
                negative='爱奇艺视频播放出错',
                level='debug')
        except Exception as e:
            self.write("等待出错！")
            result_flag = False
        return result_flag
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
class TecentVideo_Mobile_Page(Mobile_Base_Page):
    app_conf = app_conf.app_tecentVIdeo
    tecentVideo_search = locators.tecentVideo_search
    tecentVideo_search_text_clear = locators.tecentVideo_search_text_clear
    tecentVideo_search_text = locators.tecentVideo_search_text
    tecentVideo_search_button = locators.tecentVideo_search_button
    tecentVideo_QYN_1 = locators.tecentVideo_QYN_1
    tecentVideo_error = locators.tecentVideo_error

    def start(self):
        "Use this method to go to specific URL -- if needed"
        print("start")
        pass

    @Wrapit._screenshot
    def click_search_begin(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.tecentVideo_search):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='click_search_begin',
                negative='Failed to click_search_begin',
                level='debug')

        except Exception as e:
            self.write("点击腾讯视频搜索框失败")  
            self.write(str(e))
        return result_flag
    
    @Wrapit._screenshot
    def input_search_text(self,text):
        # try :
        #     self.click_element(self.tecentVideo_search_button)
        # except Exception as e:
        #     self.write("腾讯视频跳过搜索框点击搜索失败")
        # self.wait(2)
        #     # self.click_element(self.tecentVideo_search_text)
        # try:
        #     self.touch_tap(600,100)
        # except Exception as e:
        #     self.write("点击X失败")
        #     self.wait(1)
        try:
            # Click on real time price page button.
            result_flag = None

            if self.set_text(self.tecentVideo_search_text,text):
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
            if self.click_element(self.tecentVideo_search_button):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='腾讯视频确认搜索点击搜索按钮',
                negative='腾讯视频点击搜索按钮失败',
                level='debug')

        except Exception as e:
            self.write("腾讯视频点击搜索按钮失败")  
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def select_QYN_series(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.tecentVideo_QYN_1):
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
        self.wait(time)
        self.write("腾讯视频视频播放，进行等待操作")  
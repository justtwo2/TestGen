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

class Bilibili_Mobile_Page(Mobile_Base_Page):
    app_conf = app_conf.app_bilibili
    bilibili_search = locators.bilibili_search
    bilibili_search_text = locators.bilibili_search_text
    bilibili_BNA_1 = locators.bilibil_BNA_1
    bilibili_search_select = locators.bilibili_search_select

    def start(self):
        "Use this method to go to specific URL -- if needed"
        print("start")
        pass

    @Wrapit._screenshot
    def click_search_begin(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.bilibili_search):
                result_flag = True
            else:
                result_flag = False    
            self.conditional_write(result_flag,
                positive='click_search_begin',
                negative='Failed to click_search_begin',
                level='debug')

        except Exception as e:
            self.write("点击B站视频搜索框失败")  
            self.write(str(e))
        return result_flag
    
    @Wrapit._screenshot
    def input_search_text(self,text):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.set_text(self.bilibili_search_text,text):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='bilibili input search text',
                negative='bilibili Failed to input search text',
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
            if self.click_element(self.bilibili_search_select):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='B站视频确认搜索点击搜索按钮',
                negative='B站视频点击搜索按钮失败',
                level='debug')

        except Exception as e:
            self.write("B站视频点击搜索按钮失败")  
            self.write(str(e))
        return result_flag
    @Wrapit._screenshot
    def select_DLDL_series(self):
        try:
            # Click on real time price page button.
            result_flag = None
            if self.click_element(self.bilibili_BNA_1):
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
        self.write("优酷视频视频播放，进行等待操作")  
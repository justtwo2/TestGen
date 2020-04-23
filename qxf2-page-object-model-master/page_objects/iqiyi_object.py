#coding=utf-8
"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""
import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Iqiyi_Object:
    "Page object for the Form"
    
    #locators
    name_field = locators.name_field
    email_field = locators.email_field
    phone_no_field = locators.phone_no_field
    click_me_button = locators.click_me_button
    gender_dropdown = locators.gender_dropdown
    gender_option = locators.gender_option
    tac_checkbox = locators.tac_checkbox
    iqiyi_videoQYN_check = locators.iqiyi_videoQYN_check
    iqiyi_ad_wait = locators.iqiyi_ad_wait
    iqiyi_ad_skip = locators.iqiyi_ad_skip
    iqiyi_copyright_error = locators.iqiyi_copyright_error
    redirect_title = "redirect"    


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def play_video(self,url,time=10):
        "打开视频链接"
        try:
            self.open(url,time)
            return True
        except Exception as e:
            print("Python says:%s"%str(e))
            return False
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def wait_ad(self,adInfo,vInfo,time = 120):
        "等待广告跳过"
        #检查视频
        videoInfo = str(self.get_text(self.iqiyi_videoQYN_check),encoding='utf-8')
        print(videoInfo,vInfo)
        assert videoInfo == vInfo ,"视频不匹配"
        
        #等待广告播发完成
        try:
            self.wait(30,self.iqiyi_ad_wait)
        except e:
            print(e)
        print("等广告播放")
        #点击跳过广告
        for i in range(0,3):
            try:
                self.click_element(self.iqiyi_ad_skip,30)
                return True
            except:
                print("跳过播放视频失败",i)
        return False



    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_copyright(self,info):
        self.wait(20)
        copyright=  self.get_elements(self.iqiyi_copyright_error)
        if copyright :
            text = self.get_text(self.iqiyi_copyright_error)
            if text == info:
                return False
        return True

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_video_copyright(self,copyright_info,copyright_path):
        self.wait(20)
        copyright=  self.get_elements(copyright_path)
        if copyright :
            text = self.get_text(self.iqiyi_copyright_error)
            if text == copyright_info:
                return False
        return True

        
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def wait_video_ad(self,vInfo,vpath,time = 120):
        "等待广告跳过"
        #检查视频
        videoInfo = str(self.get_text(vpath),encoding='utf-8')
        print(videoInfo,vInfo)
        try:
            assert videoInfo == vInfo ,"视频不匹配"
            #等待广告播发完成
            self.wait(time)
            return True
        except e:
            print(e)
            return False


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_name(self,name):
        "Set the name on the form"
        result_flag = self.set_text(self.name_field,name)
        self.conditional_write(result_flag,
            positive='Set the name to: %s'%name,
            negative='Failed to set the name in the form',
            level='debug')

        return result_flag 


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.email_field,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_phone(self,phone):
        "Set the phone on the form"
        result_flag = self.set_text(self.phone_no_field,phone)
        self.conditional_write(result_flag,
            positive='Set the phone to: %s'%phone,
            negative='Failed to set the phone in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_gender(self,gender,wait_seconds=1):
        "Set the gender on the form"
        result_flag = self.click_element(self.gender_dropdown)
        self.wait(wait_seconds)
        result_flag &= self.click_element(self.gender_option%gender)
        self.conditional_write(result_flag,
            positive='Set the gender to: %s'%gender,
            negative='Failed to set the gender in the form',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_me(self):
        "Click on 'Click Me' button"
        result_flag = self.click_element(self.click_me_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "click me" button',
            negative='Failed to click on "click me" button',
            level='debug')

        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def accept_terms(self):
        "Accept the terms and conditions"
        result_flag = self.select_checkbox(self.tac_checkbox)
        self.conditional_write(result_flag,
            positive='Accepted the terms and conditions',
            negative='Failed to accept the terms and conditions',
            level='debug')
            
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        if self.redirect_title in self.driver.title:
            result_flag = True
            self.switch_page("redirect")
        
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_form(self,username,email,phone,gender):
        "Submit the form"
        result_flag = self.set_name(username)
        result_flag &= self.set_email(email)
        result_flag &= self.set_phone(phone)
        result_flag &= self.set_gender(gender)
        result_flag &= self.accept_terms()
        result_flag &= self.click_me()
        result_flag &= self.check_redirect()

        return result_flag



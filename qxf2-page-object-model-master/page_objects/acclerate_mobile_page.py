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

class Acclerate_Mobile_Page(Mobile_Base_Page):
    "Page Object for the dummy page"
    weixin_sign_in = locators.weixin_sign_in
    turn_on_acclerate = locators.turn_on_acclerate
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        print("start")
        pass
    @Wrapit._screenshot
    def click_sign_in_by_wechat(self):
        try:
            # Click on real time price page button.
            result_flag = None
            #self.wait(wait_seconds=10,locator=self.weixin_sign_in)
            if self.click_element(self.weixin_sign_in):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='Click on weixin_sign_in button.',
                negative='Failed to click on the bitcoin real time price page button.',
                level='debug')

        except Exception as e:
            self.write("Exception while clicking on the bitcoin real time price button.")  
            self.write(str(e))

        return result_flag

    @Wrapit._screenshot
    def click_open_acclerate(self):
        try:
            # Click on real time price page button.
            result_flag = None
            #self.wait(wait_seconds=10,locator=self.turn_on_acclerate)
            if self.click_element(self.turn_on_acclerate):
                result_flag = True
            else:
                result_flag = False    

            self.conditional_write(result_flag,
                positive='Click on weixin_sign_in button.',
                negative='Failed to click on the bitcoin real time price page button.',
                level='debug')

        except Exception as e:
            self.write("Exception while clicking on the bitcoin real time price button.")  
            self.write(str(e))

        return result_flag

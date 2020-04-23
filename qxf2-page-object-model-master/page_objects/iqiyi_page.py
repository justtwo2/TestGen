import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .Base_Page import Base_Page
from .iqiyi_object import Iqiyi_Object 
from utils.Wrapit import Wrapit


class Iqiyi_Page(Base_Page,Iqiyi_Object):
    "Page Object for the tutorial's main page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'index.html'
        self.open(url)
        


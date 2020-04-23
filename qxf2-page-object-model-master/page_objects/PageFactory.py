#coding=utf-8
"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Tutorial main page
2. Tutorial redirect page
3. Contact Page
4. Bitcoin main page
5. Bitcoin price page
"""

import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.iqiyi_page import Iqiyi_Page
from page_objects.tecentVideo_page import TecentVideo_page
from page_objects.acclerate_mobile_page import Acclerate_Mobile_Page
from page_objects.iqiyi_mobile_page import Iqiyi_Mobile_Page
from page_objects.tecentVideo_mobile_page import TecentVideo_Mobile_Page
from page_objects.youkuVideo_mobile_page import YoukuVideo_Mobile_Page
from page_objects.bilibili_mobile_page import Bilibili_Mobile_Page
from page_objects.tudouVideo_mobile_page import TudouVideo_Mobile_Page
from page_objects.qqMusic_mobile_page import QQMusic_Mobile_Page
from page_objects.net163Music_mobile_page import Net163Music_Mobile_Page
from page_objects.xiamiMusic_mobile_page import XiamiMusic_Mobile_Page
import conf.base_url_conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        #page_name = page_name.lower() 小写。。。。
        #模板
        if  page_name == "iqiyi page":
            test_obj = Iqiyi_Page(base_url=base_url)
        elif page_name == "tecentVideo page":
            test_obj = TecentVideo_page(base_url=base_url)
        elif page_name == "acclerate mobile page":
            test_obj = Acclerate_Mobile_Page()
        elif page_name == "iqiyi mobile page":
            #print("爱奇艺")
            test_obj = Iqiyi_Mobile_Page()
        elif page_name == "tecentVideoMobilePage":
            test_obj = TecentVideo_Mobile_Page()
        elif page_name == "qqMusic mobile page":
            test_obj = QQMusic_Mobile_Page()
        elif page_name == "youkuVideo mobile page":
            test_obj = YoukuVideo_Mobile_Page()
        elif page_name == "tudouVideo mobile page":
            test_obj = TudouVideo_Mobile_Page()
        elif page_name == "bilibili mobile page":
            test_obj = Bilibili_Mobile_Page()
        elif page_name == "cctv mobile page":
            test_obj = Acclerate_Mobile_Page()
        elif page_name == "xiamiMusic mobile page":
            test_obj = XiamiMusic_Mobile_Page()
        elif page_name == "net126Music mobile page":
            test_obj = Net163Music_Mobile_Page()
        if test_obj == None:
            print('匹配失败')
        else:
            print(page_name," is used")
        return test_obj

    get_page_object = staticmethod(get_page_object)
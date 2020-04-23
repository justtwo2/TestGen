import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.mobile_bitcoin_conf as conf
import conf.testrail_caseid_conf as testrail_file
import conf.mobile_app_conf as app_conf
from utils.acclerate_email import Acclerate_email
import pytest




TEST_RESULT = {}


desired_caps = {
    "mobile_os_name" : "Android", #手机操作系统
    "mobile_os_version" : "9", #系统版本
    "device_name": "HLR4C19802004725", # 设备名 adb devices    6934066
    "app_package":"cn.yyjs", # APP包名
    "app_activity": "cn.yyjs.MainActivity", # app活动窗口
    "remote_flag":"N", # 是否启用远程连接 Y/N
    "device_flag":"Y", # 是否传APP Y/N
    "app_name":"", #app 名称
    "app_path":"", # app 路径
    "ud_id":"", #IOS特定传参
    "org_id":"", #IOS特定传参
    "signing_id":"", #IOS特定传参
    "no_reset_flag" : False  #IOS特定传参,是否重置APP
}
test_mobile_obj = PageFactory.get_page_object("acclerate mobile page") #acclerate mobile page

def setup_module():
    
    test_mobile_obj.register_driver(desired_caps["mobile_os_name"],desired_caps["mobile_os_version"],desired_caps["device_name"],desired_caps["app_package"],desired_caps["app_activity"],desired_caps["remote_flag"],desired_caps["device_flag"],desired_caps["app_name"],desired_caps["app_path"],desired_caps["ud_id"],desired_caps["org_id"],desired_caps["signing_id"],desired_caps["no_reset_flag"])
    test_mobile_obj.set_test_run_id(1)
    test_mobile_obj.register_tesults()

def teardown_module():
    email = Acclerate_email()
    email.send_testReport(TEST_RESULT)
    test_mobile_obj.wait(3)
    test_mobile_obj.teardown()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    ** 作者：上海-悠悠 QQ交流群：588402570**
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_youkuVideo.png"
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.mark.MOBILE
def test_android_acclerate():
    "Run the test."
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        start_time = int(time.time())
        time.sleep(9)
        assert test_mobile_obj.click_sign_in_by_wechat() == True
        assert test_mobile_obj.click_open_acclerate() == True
        time.sleep(1)
        test_mobile_obj.save_screenshot("result_acclerate")
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_mobile_obj.save_screenshot("result_acclerate")
    if actual_pass == 1:
        TEST_RESULT["acclerate_result"] = "success"
    else :
        TEST_RESULT["acclerate_result"] = "failed"
    TEST_RESULT["acclerate_img"] = path


@pytest.mark.MOBILE
def test_android_iqiyi():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("iqiyi mobile page") 
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity_main"])     
        #2. Setup and register a driver
        time.sleep(9)
        assert test_obj.click_search_begin()
        assert test_obj.input_search_text("庆余年")
        assert test_obj.click_search_button()
        assert test_obj.select_QYN_series()
        assert test_obj.play_video(10)
        time.sleep(1)
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_iqiyi")
    test_obj.close_app()
    if actual_pass == 1:
        TEST_RESULT["iqyi_result"] = "success"
    else :
        TEST_RESULT["iqyi_result"] = "failed"
    TEST_RESULT["iqiyi_img"] = path
@pytest.mark.MOBILE
def test_android_tecentVideo():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("tecentVideoMobilePage") 
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])     
        #2. Setup and register a driver
        time.sleep(10) #app 启动较慢
        assert test_obj.click_search_begin()
        assert test_obj.input_search_text("庆余年")
        assert test_obj.click_search_button()
        assert test_obj.select_QYN_series()
        test_obj.play_video(10)
        time.sleep(1)
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_tecentVideoE")
    if actual_pass == 1:
        TEST_RESULT["tecentVideo_result"] = "success"
    else :
        TEST_RESULT["tecentVideo_result"] = "failed"
    TEST_RESULT["tecentVideo_img"] = path

@pytest.mark.MOBILE
def test_android_youkuVideo():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("youkuVideo mobile page") 
        print(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])     
        #2. Setup and register a driver
        time.sleep(9) #app 启动较慢
        assert test_obj.click_search_begin()
        assert test_obj.input_search_text("斗罗大陆2")
        assert test_obj.click_search_button()
        assert test_obj.select_DLDL_series()
        test_obj.play_video(10)
        time.sleep(1)
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_youkuVideo")
    if actual_pass == 1:
        TEST_RESULT["youkuVideo_result"] = "success"
    else :
        TEST_RESULT["youkuVideo_result"] = "failed"
    TEST_RESULT["youkuVideo_img"] = path
@pytest.mark.MOBILE
def test_android_bilibili():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0


        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("bilibili mobile page") 
        print(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"],50)   
        time.sleep(10) #app 启动较慢
        # test_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity_main"],50)  
        # time.sleep(15) #app 启动较慢     
        #2. Setup and register a driver
        assert test_obj.click_search_begin()
        assert test_obj.input_search_text("动物新世代 / BNA")
        time.sleep(2)
        assert test_obj.click_search_button()
        assert test_obj.select_DLDL_series()
        test_obj.play_video(10)
        time.sleep(1)
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_bilibili")
    if actual_pass == 1:
        TEST_RESULT["bilibli_result"] = "success"
    else :
        TEST_RESULT["bilibli_result"] = "failed"
    TEST_RESULT["bilibli_img"] = path
@pytest.mark.MOBILE
def test_android_tudou():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("tudouVideo mobile page") 
        print(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])     
        #2. Setup and register a driver
        time.sleep(9) #app 启动较慢
        assert test_obj.click_search_begin()
        assert test_obj.input_search_text("斗罗大陆3")
        assert test_obj.click_search_button()
        assert test_obj.select_DLDL_series()
        test_obj.play_video(10)
        time.sleep(1)
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_tudouVideo")
    if actual_pass == 1:
        TEST_RESULT["tudouVideo_result"] = "success"
    else :
        TEST_RESULT["tudouVideo_result"] = "failed"
    TEST_RESULT["tudouVideo_img"] = path
@pytest.mark.MOBILE
def test_android_QQMusic():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("qqMusic mobile page") 
        print(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])     
        #2. Setup and register a driver
        time.sleep(9) #app 启动较慢
        test_obj.click_qqMusic_cancleLogin()
        assert test_obj.click_qqMusic_YYG()
        assert test_obj.click_qqMusic_rand()
        assert test_obj.click_qqMusic_soaringList()
        assert test_obj.check_qqMusic_soaringList()
        time.sleep(1)
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_QQMusic")
    if actual_pass == 1:
        TEST_RESULT["qqMusic_result"] = "success"
    else :
        TEST_RESULT["qqMusic_result"] = "failed"
    TEST_RESULT["qqMusic_img"] = path
@pytest.mark.MOBILE
def test_android_net126Music():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("net126Music mobile page") 
        print(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])     
        #2. Setup and register a driver
        time.sleep(15) #app 启动较慢
        test_obj.click_netease_userAgreement() #点击同意用户协议
        #test_obj.click_netease_trial() #点击试用
        #test_obj.click_netease_rand() #点击排行榜，网易云音乐排行榜地域限制歌曲较少，采用搜索指定歌曲
        assert test_obj.click_netease_netease_search()#点击搜索
        assert test_obj.input_netease_search_text("起风了") #输入搜索文本
        assert time.sleep(2)
        assert test_obj.click_netease_search_button() #点击搜索
        assert test_obj.click_netease_netease_search_result1() #点击搜索结果第一条
        assert test_obj.check_result_errror() #检查地域限制
        time.sleep(1)
        actual_pass = 1
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_net126Music")
    if actual_pass == 1:
        TEST_RESULT["net163_result"] = "success"
    else :
        TEST_RESULT["net163_result"] = "failed"
    TEST_RESULT["net163_img"] = path
@pytest.mark.MOBILE
def test_android_xiamiMusic():
    try:
        # Initalize flags for tests summary.
        expected_pass = 0
        actual_pass = -1
        #1. Create a test object.
        test_obj = PageFactory.get_page_object("xiamiMusic mobile page") 
        print(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])
        test_mobile_obj.start_activity(test_obj.app_conf["app_package"],test_obj.app_conf["app_activity"])     
        #2. Setup and register a driver
        time.sleep(9) #app 启动较慢
        assert test_obj.click_xiamiMusic_search()#点击搜索
        assert test_obj.input_xiamiMusic_search_text("吴亦凡 时间煮雨") #输入搜索文本
        time.sleep(2)
        assert test_obj.click_xiamiMusic_search_button() #点击搜索
        assert test_obj.click_xiamiMusic_WYFJG_2() #点击搜索结果第一条
        assert test_obj.check_result_errror() #检查地域限制
        time.sleep(1)
        actual_pass = 1
        test_obj.save_screenshot("result_xiamiMusic")
        test_obj.close_app()
    except Exception as e:
        print("Exception when trying to run iqiyi test:%s" % __file__)
        print("Python says:%s" % str(e))
    path = test_obj.save_screenshot("result_xiamiMusic")
    if actual_pass == 1:
        TEST_RESULT["xiamiMusic_result"] = "success"
    else :
        TEST_RESULT["xiamiMusic_result"] = "failed"
    TEST_RESULT["xiamiMusic_img"] = path
if __name__ == '__main__':
    pytest.main(["--html=report.html","test_android_acclerate.py"]) #,
    # # python -m pytest -k mobile_bitcoin_price -H $Emulator_OS_Version -I $Emulator_Name
    # # 命令行执行
    # # python -m pytest -k mobile_bitcoin_price -G Android -H 7.0 -I 6934066 -J cn.yyjs -K cn.yyjs.MainActivity -Q Y -D yyjs-android-normal-pr-pr-28.apk -N D:\acclerate_soft\
    # # Run  the test only if the options provided are valid.
    # desired_caps = {
    #     "mobile_os_name" : "Android", #手机操作系统
    #     "mobile_os_version" : "9", #系统版本
    #     "device_name": "HLR4C19802004725", # 设备名 adb devices    6934066
    #     "app_package":"cn.yyjs", # APP包名
    #     "app_activity": "cn.yyjs.MainActivity", # app活动窗口
    #     "remote_flag":"N", # 是否启用远程连接 Y/N
    #     "device_flag":"Y", # 是否传APP Y/N
    #     "app_name":"", #app 名称
    #     "app_path":"", # app 路径
    #     "ud_id":"", #IOS特定传参
    #     "org_id":"", #IOS特定传参
    #     "signing_id":"", #IOS特定传参
    #     "no_reset_flag" : False  #IOS特定传参,是否重置APP
    # }
    # test_mobile_obj = PageFactory.get_page_object("acclerate mobile page") #acclerate mobile page
    # test_mobile_obj.register_driver(desired_caps["mobile_os_name"],desired_caps["mobile_os_version"],desired_caps["device_name"],desired_caps["app_package"],desired_caps["app_activity"],desired_caps["remote_flag"],desired_caps["device_flag"],desired_caps["app_name"],desired_caps["app_path"],desired_caps["ud_id"],desired_caps["org_id"],desired_caps["signing_id"],desired_caps["no_reset_flag"])
    # test_mobile_obj.set_test_run_id(1)
    # test_mobile_obj.register_tesults()
    # # 开启雨燕加速
    # test_android_acclerate(test_mobile_obj)
    # # 爱奇艺视频播放
    # test_android_iqiyi(test_mobile_obj)
    # # 腾讯视频播放
    # test_android_tecentVideo(test_mobile_obj)
    # # 优酷视频
    # test_android_youkuVideo(test_mobile_obj)
    # # B站
    # test_android_bilibili(test_mobile_obj)
    # # 土豆视频
    # test_android_tudou(test_mobile_obj)
    # #QQ音乐
    # test_android_QQMusic(test_mobile_obj)
    # #网易云音乐
    # test_android_net126Music(test_mobile_obj)
    # #虾米音乐
    # test_android_xiamiMusic(test_mobile_obj)
    # test_mobile_obj.wait(3)
    # test_mobile_obj.teardown()
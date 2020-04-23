"""
This is an example automated test to help you learn Qxf2's framework
Our automated test will do the following:
    #Open Qxf2 selenium-tutorial-main page.
    #Print out the entire table 
    #Verify if a certain name is present in the table
"""

#The import statements import: standard Python modules,conf,credential files
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.example_table_conf as conf
import conf.testrail_caseid_conf as testrail_file
import pytest


@pytest.mark.GUI
def test_tecent_video(test_obj):

    "Run the test"
    try:        
        #1. Create a example table page object
        test_obj = PageFactory.get_page_object("iqiyi page",base_url="https://v.qq.com/")    

        #Set start_time with current time
        start_time = int(time.time())	


        # Turn on the highlighting feature
        test_obj.turn_on_highlight()
                
        #4. Get the test details from the conf file
        iqiyi_video_url = "/x/cover/m441e3rjq9kwpsc/m00253deqqo.html"

        #5. 打开视频加载三十秒
        result_flag = test_obj.play_video(iqiyi_video_url,30)
        #result_flag = test_obj.set_name(name) 
        test_obj.log_result(result_flag,
                            positive="打开腾讯视频成功",
                            negative="打开腾讯视频失败")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #6.等待视频广告加载结束
        result_flag = test_obj.wait_video_ad('斗罗大陆','xpath,//*[@id="container_player"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/h2/a')
        #result_flag = test_obj.set_name(name) 
        test_obj.log_result(result_flag,
                            positive="广告播放成功",
                            negative="广告播放失败")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #7.播放视频五分钟检查是否代理成功
        result_flag = test_obj.check_copyright("很抱歉，由于版权限制，您所在的地区暂时无法播放该视频",'xpath,//*[@id="txplayer_81b70aeb1244e5d19469394d732b5167"]/txpdiv[11]/txpdiv[1]/span[1]')
        test_obj.save_screenshot("tecentVideo_result")
        test_obj.log_result(result_flag,
                            positive="播放成功，无版权限制",
                            negative="播放失败，版权限制")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        #Turn off the highlighting feature
        test_obj.turn_off_highlight()

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))
    
    assert expected_pass == actual_pass, "Test failed: %s"%__file__

#---START OF SCRIPT
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options=options_obj.get_options()
                        
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)
        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'   
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()
        
        test_tecent_video(test_obj) 
        
        #teardowm
        test_obj.wait(3)
        test_obj.teardown()

    else:
        print('ERROR: Received incorrect input arguments')
        print(options_obj.print_usage())

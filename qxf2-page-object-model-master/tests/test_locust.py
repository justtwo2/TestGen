
import requests

from locust import HttpLocust, TaskSet, task
proxies = {
#   'http': 'http://localhost:1081',
#   'https': 'http://localhost:1081',
}

ERROR_COUNT = 0
# 定义用户行为
class UserBehavior(TaskSet):
    def on_start(self):
        print("start")

    # @task(1)
    # def bky_index(self):
    #     self.client.get("/")

    # @task(1)
    # def blogs(self):
    #     iqiyi_download_url = '/download/F/1/0/F10113F5-B750-4969-A255-274341AC6BCE/GRMSDKIAI_EN_DVD.iso'
    #     if proxies == {} or proxies == None:
    #         rsp = self.client.get(iqiyi_download_url)
    #     else:
    #         rsp = self.client.get(iqiyi_download_url,proxies=proxies)
        # print(rsp)
    # @task(2)
    # def blogs(self):
    #     iqiyi_download_url ='/download/A/6/A/A6AC035D-DA3F-4F0C-ADA4-37C8E5D34E3D/winsdk_web.exe'
    #     if proxies == {} or proxies == None:
    #         rsp = self.client.get(iqiyi_download_url)
    #     else:
    #         rsp = self.client.get(iqiyi_download_url,proxies=proxies)
        # rsp.raise_for_status()
        # try:
        #     response_size = len(rsp.text)
            
        #     #assert response_size == 484123 ,"包长不正确"
        # except Exception as e :
        #     print(response_size,e)
        #     ERROR_COUNT = ERROR_COUNT+1
        #     print("##########",ERROR_COUNT)
    @task(1)
    def blogs(self):
        iqiyi_download_url = 'hz/IQIYIsetup_z40.exe'
        if proxies == {} or proxies == None:
            rsp = self.client.get(iqiyi_download_url)
        else:
            rsp = self.client.get(iqiyi_download_url,proxies=proxies)
        # try:
        #     response_size = len(rsp.text)
        #     rsp.raise_for_status()
        #     #assert response_size == 484123 ,"包长不正确"
        # except :
        #     print(response_size)
        #     ERROR_COUNT = ERROR_COUNT+1
        #     print(ERROR_COUNT)

class WebsiteUser(HttpLocust):
    host = "http://dl.static.iqiyi.com/"#"https://download.microsoft.com/" #
    task_set = UserBehavior
    min_wait = 1500
    max_wait = 5000


# iqiyi_download_url = 'http://dl.static.iqiyi.com/hz/IQIYIsetup_z40.exe'


# file_name = r'D:\acclerate_soft\IQIYIsetup_z40.exe'
# down_res = requests.get("http://dl.static.iqiyi.com/hz/IQIYIsetup_z40.exe", proxies=proxies)
# print(down_res)
# with open(file_name,"wb") as code:
#     code.write(down_res.content)

# __author__ ='xjiao
# -*- coding:utf-8 -*-'

import os
import os.path
import time
import glob

#微信
WeChat_Package = "com.tencent.mm"
WeChat_Activity = "com.tencent.mm.ui.LauncherUI"

#QQ音乐
QQMusic_Package = "com.tencent.qqmusic"
QQMusic_Activity = "com.tencent.qqmusic.activity.AppStarterActivity"

#优酷视频
Youku_Package = "com.youku.phone"
Youku_Activity = "com.youku.phone.ActivityWelcome"

#土豆视频
TuDou_Package = 'com.tudou.android'
TuDou_Activity = 'com.tudou.android.ui.activity.welcome.WelcomeActivity'

#网易云音乐
WYMusic_Package = 'com.netease.cloudmusic'
WYMusic_Activity = 'com.netease.cloudmusic.activity.LoadingActivity'

#虾米音乐
xiami_Package = 'fm.xiami.main'
xiami_Activity = 'fm.xiami.main.SplashActivity'

#cctv5
cctv5_Package = 'com.cctv.cctv5ultimate'
cctv5_Activity = 'com.cctv.cctv5ultimate.activity.splash.StartUpActivity'



[
    {
        "name": "com.youku.phone",
        "desc": "优酷视频"
    },
    {
        "name": "com.tudou.android",
        "desc": "土豆视频"
    },
    {
        "name": "com.qiyi.video",
        "desc": "爱奇艺"
    },
    {
        "name": "com.tencent.qqlive",
        "desc": "腾讯视频"
    },
    {
        "name": "tv.danmaku.bili",
        "desc": "B站"
    },
        {
        "name": "com.qq.ac.android",
        "desc": "腾讯动漫"
    },
    {
        "name": "com.tencent.qqmusic",
        "desc": "QQ音乐"
    },
    {
        "name": "com.netease.cloudmusic",
        "desc": "网易云音乐"
    },
    {
        "name": "fm.xiami.main",
        "desc": "虾米音乐"
    },
    {
        "name": "com.cctv.cctv5ultimate",
        "desc": "央视体育"
    },
    {
        "name": "cn.cntv",
        "desc": "央视影音"
    }
]



# 删除已有测试cmd脚本
path = "E:\\monkey_test\\"
for file in glob.glob(os.path.join(path,'*.cmd')):
    os.remove(file)

# os.system("cls")具有清屏功能
os.system("cls")
# os.popen()执行系统命令并返回执行后的结果
rt = os.popen('adb devices').readlines()

n = len(rt) - 2
print "当前已连接待测手机数为：" + str(n)
aw = raw_input("是否要开始你的monkey测试，请输入（yes or no）:")

if aw == 'yes':
    print "monkey测试即将开始......"
    count = raw_input("请输入你要进行的monkey测试次数：")
    testmodel =  raw_input("请输入你是要进行单次测试还是多次连续测试，请输入（1-代表单次测试，2-代表多次连续测试）：")
    ds = rang(n)
    for i in range(n):
        nPos = rt[i+1].index("\t")
        ds[i] = rt[i+1].[:nPos]
        dev = ds[i]
        # 获取手机型号
        promodel = os.popen("adb -s " + dev +'shell cat /system/build.prop | find "ro.product.model="').readline()

        #modelname = ('').join(promodel)  #将list转为字符串
        modelname = promodel[0] #从list中取出第一个值
        model = modelname[17:].strip('\r\n')

        proname = os.popen("adb -s" + dev + 'shell cat /system/build.prop | find "ro.product.brand="').readlines() #获取手机名称

        roname = proname[0]
        name = roname[17].strip('\r\n')
        packagename = os.popen(
            "adb -s " + dev + ' shell pm list packages | find "xxx"').readlines()

        package = packagename[0]
        pk = package[8:].strip('\r\n')
        if pk == 'com.xxx':
            filedir = os.path.exists("E:\\monkey_test\\")
            if filedir:
                print "File Exist!"
            else:
                os.mkdir("E:\\monkey_test\\")

            devicedir = os.path.exists("E:\\monkey_test\\" + name + '-' + model + '-' + dev)

            if devicedir:
                print "File exist!"
            else:
                os.mkdir("E:\\monkey_test\\" + name + '-' + model + '-' + dev) #按设备ID生成日志目录文件夹

            w1 = open("E:\\monkey_test\\" + name + '- ' + model + '' + ds[i] + '-logcat' + '.cmd','w')
            # wl.write('adb -s ' + dev + ' logcat -v time ACRA:E ANRManager:E System.err:W *:S')

            wl.write('adb -s ' + dev + ' logcat -v time *:W')
            wl.write('> E:\\monkey_test\\' + '"'+ name  + '-'+ model + '-' + dev + '"' + '\\logcat_%random%.txt\n')
            wl.close()
            if testmodel == '1':
                wd = open("E:\\monkey_test\\" +name + '-' + model + '-' + ds[i] + '-device' + '.cmd', 'w')
                wd.write(
                    'adb -s ' + dev + ' shell monkey -p com.xxx --monitor-native-crashes --ignore-crashes --pct-syskeys 5 --pct-touch 55 --pct-appswitch 20 --pct-anyevent 20 --throttle 200 -s %random% -v ' + count)  # 选择设备执行monkey
                wd.write('> E:\\monkey_test\\' + '"'+ name  + '-'+ model + '-' + dev + '"' + '\\monkey_%random%.txt\n')
                wd.write('@echo 测试成功完成，请查看日志文件~')
                wd.close()
            elif testmodel == '2':
                wd = open("E:\\monkey_test\\" +name + '-' + model + '-' + ds[i] + '-device' + '.cmd', 'w')
                wd.write(':loop')
                wd.write('\nset /a num+=1')
                wd.write('\nif "%num%"=="4" goto end')
                wd.write(
                    '\nadb -s ' + dev + ' shell monkey -p com.xxx --monitor-native-crashes --ignore-crashes --pct-syskeys 5 --pct-touch 55 --pct-appswitch 20 --pct-anyevent 20 --throttle 200 -s %random% -v ' + count)  # 选择设备执行monkey
                wd.write('> E:\\monkey_test\\' + '"'+ name  + '-'+ model + '-' + dev + '"' + '\\monkey_%random%.txt\n')
                wd.write('@echo 测试成功完成，请查看日志文件~')
                wd.write('\nadb -s '+ dev +' shell am force-stop '+ pk)
                wd.write('\n@ping -n 15 127.1 >nul')
                wd.write('\ngoto loop')
                wd.write('\n:end')
                wd.close()
            else:
                print "请确认待测手机"+name + '-' + model +"未安装com.xxx~"

            # 执行上述生成的cmd脚本path='E:\\monkey_test\\'
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)) == True:
                if file.find('.cmd') > 0:
                    os.system('start ' + os.path.join(path, '"' + file + '"'))  # dos命令中文件名如果有空格，需加上双引号
                    time.sleep(1)
                elif aw == 'no':
                    print('请重新确认所有待测手机是否已通过adb命令连接至pc!')
                else:
                    print "测试结束，输入非法，请重新输入yes or no！"
import os,sys,time,imaplib,email,datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import conf.email_conf as conf_file
import smtplib  
from email.mime.text import MIMEText       #MIMEText()定义邮件正文  
from email.header import Header  
from utils.email_util import Email_Util
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
class Acclerate_email:
    imaphost = conf_file.imaphost #imap Host
    username = conf_file.username #邮箱账号
    app_password = conf_file.app_password #邮箱密码
    smtp_ssl_host = conf_file.smtp_ssl_host #stmp服务器 host
    smtp_ssl_port = conf_file.smtp_ssl_port #smtp 服务器端口
    sender = conf_file.sender #发送邮箱
    targets = conf_file.targets #接收邮箱


    def addimg(self,src,imgid):    # 添加图片函数，参数1：图片路径，参数2：图片id
        fp = open(src, 'rb')    # 打开文件
        msgImage = MIMEImage(fp.read())    # 创建MIMEImage对象，读取图片内容并作为参数
        fp.close()    # 关闭文件
        msgImage.add_header('Content-ID', imgid)    # 指定图片文件的Content-ID，imgid，<img>标签中的src用到
        return msgImage    # 返回msgImage对象

    def send_testReport(self,testResult):
        '''
        #数据模板格式
        test_result = {
            "acclerate_result":"pass",
            "acclerate_img":"url",
            "iqyi_result":"pass",
            "iqiyi_img":"",
            "tecentVideo_result":"pass",
            "tecentVideo_img":"",
            "youkuVideo_result":"pass",
            "youkuVideo_img":"",
            "bilibli_result":"pass",
            "bilibli_img":"",
            "tudouVideo_result":"pass",
            "tudouVideo_img":"",
            "qqMusic_result":"pass",
            "qqMusic_img":"",
            "xiamiMusic_result":"pass",
            "xiamiMusic_img":"",
            "net163_result":"pass",
            "net163_img":"",
            "cctv5_result":"pass",
            "cctv5_img":""
        }
        '''
        subject = '雨燕安卓自动化测试报告(测试版)' #邮件标题
        msg = MIMEMultipart('related') 
        #邮件正文模板
        msgText = MIMEText("""

                    <table color="CCCC33" width="800" border="1" cellspacing="0" cellpadding="5" text-align="center">

                            <tr>

                                    <td text-align="center" width="200">测试用例名称</td>

                                    <td text-align="center" width="200">执行结果</td>

                                    <td width="400">执行结果截图</td>
                            </tr>   

                            <tr>   

                                    <td text-align="center">雨燕加速启动</td>

                                    <td>%(acclerate_result)s</td>

                                    <td><image src="cid:acclerate_img" width="320" height="640"> </td>

                            </tr>
                            <tr>   

                                    <td text-align="center">爱奇艺视频播放 </td>

                                    <td>%(iqyi_result)s </td>

                                    <td><image src="cid:iqiyi_img" width="320" height="640"> </td>

                            </tr>
                            <tr>   

                                    <td text-align="center">腾讯视频播放 </td>

                                    <td>%(tecentVideo_result)s </td>

                                    <td><image src="cid:tecentVideo_img" width="320" height="640"> </td>
                            </tr>
                            <tr>   

                                    <td text-align="center">优酷视频播放 </td>

                                    <td>%(youkuVideo_result)s </td>

                                    <td><image src="cid:youkuVideo_img" width="320" height="640"> </td>
                            </tr>
                            <tr>   

                                    <td text-align="center">B站视频播放 </td>

                                    <td>%(bilibli_result)s </td>

                                    <td><image src="cid:bilibli_img" width="320" height="640"> </td>
                            </tr>
                            <tr>   

                                    <td text-align="center">土豆视频播放 </td>

                                    <td>%(tudouVideo_result)s </td>

                                    <td><image src="cid:tudouVideo_img" width="320" height="640"> </td>
                            </tr>
                            <tr>   

                                    <td text-align="center">QQ音乐播放 </td>

                                    <td>%(qqMusic_result)s </td>

                                    <td><image src="cid:qqMusic_img" width="320" height="640"> </td>
                            </tr>
                            <tr>   

                                    <td text-align="center">虾米音乐播放 </td>

                                    <td>%(xiamiMusic_result)s </td>

                                    <td><image src="cid:xiamiMusic_img" width="320" height="640"> </td>
                            </tr>
                            <tr>   
                                    <td text-align="center">网易云音乐播放 </td>

                                    <td>%(net163_result)s </td>

                                    <td><image src="cid:net163_img" width="320" height="640"> </td>
                            </tr>
                            <tr>   
                    </table>""" % testResult,"HTML")
        msg.attach(msgText)
        msg.attach(self.addimg(testResult["acclerate_img"],"acclerate_img"))
        msg.attach(self.addimg(testResult["iqiyi_img"],"iqiyi_img"))
        msg.attach(self.addimg(testResult["tecentVideo_img"],"tecentVideo_img"))
        msg.attach(self.addimg(testResult["youkuVideo_img"],"youkuVideo_img"))
        msg.attach(self.addimg(testResult["bilibli_img"],"bilibli_img"))
        msg.attach(self.addimg(testResult["tudouVideo_img"],"tudouVideo_img"))
        msg.attach(self.addimg(testResult["qqMusic_img"],"qqMusic_img"))
        msg.attach(self.addimg(testResult["xiamiMusic_img"],"xiamiMusic_img"))
        msg.attach(self.addimg(testResult["net163_img"],"net163_img"))
        msg['Subject'] = Header(subject,'utf-8')
        msg['from'] = "lizhihong@buckyos.com"  
        msg['to'] = "lizhihong@buckyos.com" 
        print(self.imaphost,self.username,self.app_password)
        #Initialize the email object
        email_obj = Email_Util()
        
        #Connect to the IMAP host
        email_obj.connect(self.imaphost)
        print("connect success")
        #Login
        if email_obj.login(self.username,self.app_password):
            print("PASS: Successfully logged in.")
        else:
            print("FAIL: Failed to login")
        email_obj.mail.sendmail(self.sender,self.targets,msg.as_string())  
if __name__=='__main__':
    test_result = {
            "acclerate_result":"pass",
            "acclerate_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "iqyi_result":"pass",
            "iqiyi_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "tecentVideo_result":"pass",
            "tecentVideo_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "youkuVideo_result":"pass",
            "youkuVideo_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "bilibli_result":"pass",
            "bilibli_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "tudouVideo_result":"pass",
            "tudouVideo_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "qqMusic_result":"pass",
            "qqMusic_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "xiamiMusic_result":"pass",
            "xiamiMusic_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "net163_result":"pass",
            "net163_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png",
            "cctv5_result":"pass",
            "cctv5_img":r"D:\bucky\QAFiles\accelerate\12-autoTest\qxf2-page-object-model-master\screenshots\setup_module\result_iqiyi.png"
        } 
    email = Acclerate_email()
    email.send_testReport(test_result)
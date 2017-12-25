# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import unittest
import HTMLTestRunner
import time, os


def send_mail(file_new):
    mail_from = '401172143@qq.com'
    mail_to = 'jolie.wu@ebestmobile.com'
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    '''邮件标题'''
    msg['Subject'] = u"自动化测试报告"
    #定义发送时间
    msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')
    #连接SMTP服务器
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    #此QQ账号暂未开通POP3/SMTP服务
    smtp.login(mail_from,'XXX')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out'


def send_report(testreport):
    result_dir = testreport
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
    print (u'最新测试生成的报告：' + lists[-1])
    file_new = os.path.join(result_dir, lists[-1])
    print file_new
    send_mail(file_new)


def createsuite():
    testunit = unittest.TestSuite()
    '''定义测试查找的目录'''
    dir = 'D:\\SFA6s\\SFA6s'
    '''定义discover方法的参数'''
    discover = unittest.defaultTestLoader.discover(dir, pattern='login*.py', top_level_dir=None)
    print discover
    '''discover筛选出的用例，循环添加到测试套件中'''
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    testreport = 'D:\\SFA6s\\SFA6s\\report\\'
    filename = testreport + now + 'result.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告',
                                           description=u'用例执行情况：')

    alltestnames = createsuite()
    runner.run(alltestnames)
    fp.close()
    #send_report(testreport)
